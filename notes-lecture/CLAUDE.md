# Dépôt QA de l'équipe

Ce dépôt contient l'agent QA (`.claude/agents/qc.md`), ses skills (`.claude/skills/`) et le contexte de chaque projet (`docs/projets/<projet>/CONTEXTE.md`).

Pour une tâche QA sur une US, travailler avec l'agent : `claude --agent qc`.

Règles valables dans toute session ouverte sur ce dépôt, avec ou sans l'agent :

1. Réponses en français.
2. Aucune donnée client ou personnelle réelle dans un fichier ou un livrable : identifiants fictifs (`ADM-TEST-01`, `ENT-TEST-01`, `DEM-TEST-01`).
3. Ne jamais inventer une règle métier, une valeur ou un message absent des sources : ce qui manque devient une question.
4. Aucune écriture dans Azure DevOps sans aperçu exact et « oui » explicite.
5. Ne jamais afficher ni écrire le PAT (`ADO_PAT`).
6. Jamais de `git commit` ni de `git push` : l'humain relit et commite.
7. Gherkin toujours en français : Étant donné que, Quand, Alors, Et, Mais.
