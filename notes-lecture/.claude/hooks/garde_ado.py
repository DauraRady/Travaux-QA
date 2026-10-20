#!/usr/bin/env python3
"""Garde-fou de l'agent QA, appelé par Claude Code avant chaque commande Bash.

1. Refuse les commandes qui afficheraient le PAT (env, printenv, set, echo ou cat de ADO_PAT).
2. Refuse toute suppression dans Azure DevOps (curl DELETE).
3. Demande confirmation à l'utilisateur pour toute écriture vers Azure DevOps
   (curl avec POST, PATCH, PUT ou un corps de requête), sauf la recherche WIQL,
   qui est une lecture.
4. Demande confirmation pour tout envoi de données vers un autre site
   (les sources du projet ne doivent pas quitter le dépôt).
5. Demande confirmation pour git commit et git push.

Ce contrôle lit le texte de la commande : il rattrape un oubli, il ne remplace ni
les règles de l'agent ni des droits de PAT limités au strict nécessaire.
"""
import json
import re
import sys

ADO_HOST = re.compile(r"(visualstudio\.com|dev\.azure\.com)", re.I)
WRITE = re.compile(
    r"(-X\s*|--request\s+)(POST|PATCH|PUT|DELETE)\b|(^|\s)(-d|--data|--data-binary|--data-raw|--data-urlencode|-F|--form|-T|--upload-file)(\s|=|@)",
    re.I,
)
DELETE = re.compile(r"(-X\s*|--request\s+)DELETE\b", re.I)
READ_ONLY_POST = re.compile(r"/_apis/wit/wiql", re.I)
SHOW_SECRET = [
    re.compile(r"(^|[;&|]\s*)(env|printenv|set)\s*($|[;&|])"),
    re.compile(r"(^|[;&|]\s*)printenv\b"),
    re.compile(r"\b(echo|printf|cat|print)\b[^;&|]*\$\{?ADO_PAT", re.I),
    re.compile(r"ADO_PAT[^;&|]*\|\s*(base64|xxd|od)\b", re.I),
]
GIT_WRITE = re.compile(r"(^|[;&|]\s*)git\s+(commit|push)\b")


def decide(decision, reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason,
        }
    }, ensure_ascii=False))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except (ValueError, OSError):
        sys.exit(0)
    if data.get("tool_name") != "Bash":
        sys.exit(0)
    cmd = (data.get("tool_input") or {}).get("command", "")

    for pattern in SHOW_SECRET:
        if pattern.search(cmd):
            decide("deny", "Commande refusée : elle afficherait le PAT ou les variables d'environnement.")

    if "curl" in cmd and ADO_HOST.search(cmd) and DELETE.search(cmd):
        decide("deny", "Suppression dans Azure DevOps refusée : l'agent ne supprime jamais rien.")

    if "curl" in cmd and ADO_HOST.search(cmd) and WRITE.search(cmd) and not READ_ONLY_POST.search(cmd):
        decide("ask", "Écriture dans Azure DevOps : vérifier que l'aperçu a été montré et validé.")

    if re.search(r"\b(curl|wget)\b", cmd) and not ADO_HOST.search(cmd) and WRITE.search(cmd):
        decide("ask", "Envoi de données vers un site autre qu'Azure DevOps : à confirmer.")

    if GIT_WRITE.search(cmd):
        decide("ask", "git commit ou git push : l'humain relit les différences avant.")

    sys.exit(0)


if __name__ == "__main__":
    main()
