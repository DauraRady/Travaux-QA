# Skills QA : contexte projet, analyse d'US et rédaction Gherkin

| Fichier | Rôle |
|---|---|
| `contexte-projet/MODELE_CONTEXTE_PROJET.md` | Modèle du fichier de contexte d'un projet : rôles, comptes de test, statuts, règles validées, données fictives, points à confirmer. À remplir une fois par projet et à tenir à jour |
| `init-contexte/SKILL.md` | Crée le contexte d'un projet à partir de ses sources (PRD, DAG, décisions), une ligne sourcée par règle |
| `maj-contexte/SKILL.md` | Ajoute au contexte ce que l'humain a validé après chaque US ou réponse du PO, après aperçu et « oui » |
| `us-analysis/SKILL.md` | Analyse une US avec le contexte projet, sans inventer : règles avec leur source et leur statut, préconditions, combinaisons, questions au PO, verdict |
| `gherkin-test-generation/SKILL.md` | Rédige les scénarios en français à partir de l'analyse : préconditions complètes, actions, résultats exacts ; version cas manuel pour Azure Test Plans |
| `gherkin-test-generation/references/guide-ecriture-gherkin.md` | Exemples bons et mauvais. Les règles sont dans le skill, les exemples dans le guide |

## Enchaînement

1. `init-contexte` : créer `docs/projets/<projet>/CONTEXTE.md` à partir des sources (une fois par projet), puis relire.
2. `us-analysis` sur l'US : analyse et propositions pour le contexte.
3. `gherkin-test-generation` sur la sortie de l'analyse.
4. `maj-contexte` : ce qui a été validé entre dans le contexte ; les réponses du PO ferment les points ouverts.
5. Relecture humaine avant tout usage ou publication.

## Ce qui a changé par rapport à la version précédente

1. Une seule source pour chaque règle : rien n'est répété entre les skills et le guide.
2. Trois statuts par règle (Rédigeable, À arbitrer, Exploratoire) : seule une règle Rédigeable produit un scénario.
3. L'analyse relève les préconditions (rôle connecté, écran, données) et le skill Gherkin les écrit toutes en Étant donné.
4. Quand peut être suivi de Et pour les actions d'un même parcours ; un scénario reste un seul comportement.
5. Plus de tags de traçabilité dans le Gherkin : un tableau de couverture en fin de rapport suffit.
6. Rapport en six sections pour l'analyse (dont les propositions pour le contexte) et trois pour la rédaction.
7. Le contexte s'enrichit après chaque US, seulement avec ce qu'un humain a validé.

## Installation

Copier les dossiers dans `.claude/skills/` du dépôt (lus par Claude Code et par GitHub Copilot dans VS Code), et le contexte rempli dans `docs/projets/<projet>/CONTEXTE.md`.

Aucune donnée client réelle dans les US : uniquement des valeurs fictives. Fichiers encodés en UTF-8.
