# Agent QA pour Claude Code : un agent, six skills, un contexte par projet

## Ce que contient le pack

| Fichier | Rôle |
|---|---|
| `CLAUDE.md` | Règles communes à toute session ouverte sur le dépôt |
| `.claude/agents/qc.md` | L'agent : étapes, règle d'attente, projet actif, sécurité, accès Azure DevOps |
| `.claude/settings.json` | Permissions de l'équipe et garde-fou avant chaque commande |
| `.claude/hooks/garde_ado.py` | Refuse l'affichage du PAT ; demande confirmation avant toute écriture dans Azure DevOps et avant `git commit` ou `git push` |
| `.claude/skills/init-contexte/` | Crée le contexte d'un projet à partir de ses sources |
| `.claude/skills/us-analysis/` | Analyse d'une US avec le contexte, propositions pour le contexte |
| `.claude/skills/gherkin-test-generation/` | Scénarios Gherkin en français, guide d'écriture, script de contrôle sans IA |
| `.claude/skills/maj-contexte/` | Met à jour le contexte après validation |
| `.claude/skills/publication-ado/` | Publication des scénarios relus, ou CSV à importer |
| `.claude/skills/redaction-anomalie/` | Rédaction et création d'un bug sourcé |
| `docs/projets/_modele/` | Modèle du contexte et consignes pour les sources |
| `qc-reports/` | Un rapport par US |

## Installation (une fois, dans le dépôt de l'équipe)

1. Copier `CLAUDE.md`, `.claude/`, `docs/` et `qc-reports/` à la racine du dépôt. Si un `CLAUDE.md` existe déjà, y ajouter les règles au lieu de l'écraser.
2. Ajouter au `.gitignore` : `.qc-agent/`, `.claude/settings.local.json`, `CLAUDE.local.md`.
3. Créer `docs/projets/<projet>/sources/` et y déposer le PRD, le DAG et les décisions, en Markdown, un fichier par chapitre pour les longs documents.
4. Pousser sur une branche et ouvrir une pull request pour relecture.

## Préparer son poste (une fois par personne)

1. Créer un PAT personnel dans Azure DevOps. Pour analyser : Work Items en lecture. Pour publier : Work Items et Test Management en lecture et écriture.
2. Le déclarer comme variable d'environnement `ADO_PAT` dans son profil de terminal, jamais dans un fichier du dépôt.
3. Vérifier `python3 --version`. Sous Windows, si seule la commande `python` existe, remplacer `python3` par `python` dans `.claude/settings.json` : sinon le garde-fou ne tourne pas.
4. Sous Windows, utiliser Git Bash.

## Utilisation

Lancer Claude Code avec l'agent comme agent principal :

```bash
claude --agent qc
```

L'agent doit être l'agent principal de la session, pas un sous-agent appelé en cours de route : un sous-agent rend son résultat d'un bloc et ne peut pas attendre ton « oui » avant une écriture.

| Étape | Je tape | Résultat |
|---|---|---|
| Une fois par projet | `/init-contexte <projet>` | `docs/projets/<projet>/CONTEXTE.md`, à relire et commiter |
| Analyser une US | `/us-analysis 1234` | `qc-reports/US-1234.md` : analyse et propositions pour le contexte |
| Écrire les scénarios | `/gherkin-test-generation 1234` | Scénarios ajoutés au rapport, contrôlés par le script |
| Enrichir le contexte | `/maj-contexte 1234` | Aperçu des lignes, puis écriture après « oui » |
| Intégrer une réponse du PO | `/maj-contexte po "<réponse>" (Prénom, 22/10)` | Le point ouvert devient une règle |
| Publier | `/publication-ado 1234` | Aperçu, puis création après « oui » |
| CSV à importer | `/publication-ado 1234 csv` | `qc-reports/US-1234-import.csv` |
| Rédiger un bug | `/redaction-anomalie <ce que j'ai vu>` | Aperçu, puis création après « oui » |

Un document déposé ou un texte collé sans commande ne déclenche rien : l'agent dit ce qu'il a reçu et attend.

Plusieurs projets dans le même dépôt : un dossier par projet sous `docs/projets/`, et `projet=<nom>` dans la demande.

## Les garde-fous, du plus fort au plus faible

| Garde-fou | Ce qu'il empêche | Limite |
|---|---|---|
| Droits du PAT | Une écriture impossible avec un PAT en lecture seule | Celui qui publie a besoin de l'écriture |
| Hook `garde_ado.py` | Affichage du PAT ; écriture ADO, commit ou push sans confirmation | Lit le texte de la commande : une écriture faite autrement que par `curl` lui échappe |
| `disable-model-invocation` sur les skills qui écrivent | L'agent ne lance pas seul `/publication-ado`, `/maj-contexte`, `/init-contexte`, `/redaction-anomalie` | Ne s'applique qu'aux skills |
| Règles de l'agent et de `CLAUDE.md` | Le reste : invention, données réelles, enchaînement d'étapes | Ce sont des consignes, pas un verrou |
| Relecture humaine et Git | Toute erreur restée dans un rapport ou le contexte | Demande de vraiment relire les différences |

## Avec GitHub Copilot dans VS Code

VS Code lit aussi les agents de `.claude/agents/` et les skills de `.claude/skills/`. Il ne lit pas `.claude/settings.json` ni le hook : sous Copilot, seuls les droits du PAT, la confirmation des commandes du terminal par VS Code et les règles de l'agent protègent. À tester avant de l'annoncer à l'équipe.

## Non vérifié

1. Le script de contrôle et le garde-fou sont testés hors ligne. Aucun appel n'a été fait sur un vrai Azure DevOps.
2. Le format des paramètres d'un cas paramétré est à vérifier sur un premier cas publié.
3. Le comportement de l'agent sous Copilot (outils disponibles, commandes `/`) est à vérifier au premier lancement.
