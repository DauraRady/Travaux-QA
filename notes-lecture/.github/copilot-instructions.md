# Règles communes du dépôt pour Copilot

1. Réponses en français.
2. Aucune donnée client réelle dans un prompt, un fichier ou un livrable : valeurs fictives (`ADM-TEST-01`, `ENT-TEST-01`, `DEM-TEST-01`).
3. Ne jamais inventer une règle métier, une valeur ou un message absent des sources. Ce qui manque devient une question.
4. Aucune écriture dans Azure DevOps sans aperçu et validation explicite de l'utilisateur.
5. Pour les tâches QA (analyse d'US, scénarios, anomalies, publication), utiliser l'agent « qc agent » et ses skills dans `.github/skills/`.
6. Gherkin toujours en français : Étant donné, Quand, Alors, Et, Mais.
