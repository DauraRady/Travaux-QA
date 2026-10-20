# Skills QA : analyse d'US et rédaction Gherkin

| Fichier | Rôle |
|---|---|
| `contexte-projet/MODELE_CONTEXTE_PROJET.md` | Modèle du fichier de contexte d'un projet : rôles, comptes de test, statuts, règles validées, données fictives, points à confirmer. À remplir une fois par projet et à tenir à jour |
| `us-analysis/SKILL.md` | Analyse une US avec le contexte projet, sans inventer : règles avec leur source et leur statut, préconditions, combinaisons, questions au PO, verdict |
| `gherkin-test-generation/SKILL.md` | Rédige les scénarios en français à partir de l'analyse : préconditions complètes, actions, résultats exacts ; version cas manuel pour Azure Test Plans |
| `gherkin-test-generation/references/guide-ecriture-gherkin.md` | Exemples bons et mauvais. Les règles sont dans le skill, les exemples dans le guide |

## Enchaînement

1. Remplir `CONTEXTE_PROJET_<projet>.md` à partir du modèle (une fois, puis à chaque décision).
2. `us-analysis` sur l'US.
3. Réponses du PO aux questions bloquantes.
4. `gherkin-test-generation` sur la sortie de l'analyse.
5. Relecture humaine avant tout usage ou publication.

## Ce qui a changé par rapport à la version précédente

1. Une seule source pour chaque règle : rien n'est répété entre les skills et le guide.
2. Trois statuts par règle (Rédigeable, À arbitrer, Exploratoire) : seule une règle Rédigeable produit un scénario.
3. L'analyse relève les préconditions (rôle connecté, écran, données) et le skill Gherkin les écrit toutes en Étant donné.
4. Quand peut être suivi de Et pour les actions d'un même parcours ; un scénario reste un seul comportement.
5. Plus de tags de traçabilité dans le Gherkin : un tableau de couverture en fin de rapport suffit.
6. Rapport en cinq sections pour l'analyse et trois pour la rédaction.

## Installation

Copier les dossiers dans `.github/skills/` (GitHub Copilot) ou `.claude/skills/` (Claude Code) du dépôt, et le fichier de contexte rempli à la racine du dépôt ou dans `docs/`.

Aucune donnée client réelle dans les US : uniquement des valeurs fictives. Fichiers encodés en UTF-8.
