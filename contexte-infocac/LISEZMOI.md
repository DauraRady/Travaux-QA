# Contexte InfoCAC pour l'agent QA

| Fichier | Rôle |
|---|---|
| `CONTEXTE.md` | Contexte du projet, version 0.2 du 30/10/2026 : configuration Azure DevOps, rôles, comptes de test, objets, synonymes, statuts, règles des sprints 1 à 4, écrans, données, 25 points à confirmer, variations, flux |
| `sources/US-*.md` | Texte des US 417829 (sprint 1) et 429709, 426408, 426409, 429428 (sprint 4), pour que l'agent travaille sans accès à Azure DevOps. Les passages non lus sont marqués entre crochets |

Les US du sprint 3 sont connues par leurs cas de test (`cas-de-test/sprint-3/`), pas par leur texte : à exporter dans `sources/` pour une lecture complète.

## Installer dans le dépôt de l'équipe

1. Copier ce dossier vers `docs/projets/infocac/` (à côté de `docs/projets/_modele/`).
2. Copier `cas-de-test/` à la racine si l'agent doit retrouver les cas existants cités par le contexte.
3. Compléter l'Area Path (section 0) et l'écran d'arrivée (section 4), puis faire relire le fichier.

## Tester sur le sprint 4

1. `claude --agent qc`
2. `/coherence-sprint 429709 426408 426409 429428 sprint=4`
3. `/us-analysis 429428`, puis les autres dans l'ordre proposé par le rapport de cohérence
4. `/gherkin-test-generation <id>` sur les US prêtes
5. `/maj-contexte sprint-4`, puis `/maj-contexte <id>` après chaque US

Résultat d'un premier essai, le 30/10/2026 : `cas-de-test/sprint-4/coherence-sprint-4.md` et `cas-de-test/sprint-4/analyse-US-429709.md`.
