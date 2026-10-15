# Skills QA pour Claude Code

| Skill | Ce qu'il fait | Quand l'utiliser |
|---|---|---|
| `us-analysis` | Analyse une US et ses AC sans inventer de règle, rend un verdict de préparation, les questions d'arbitrage et les pistes de test | Avant un affinage, un Three Amigos ou une génération de tests |
| `gherkin-test-generation` | Génère des scénarios Gherkin en français, traçables, avec les techniques de conception et la liste des éléments non couverts | Quand l'US est Prête ou Partiellement prête |

Le guide `gherkin-test-generation/references/guide-ecriture-gherkin.md` explique comment écrire un scénario, avec un exemple complet commenté.

## Installation

1. Copier les deux dossiers dans `.claude/skills/` du projet (partagé avec l'équipe via Git) ou dans `~/.claude/skills/` (pour soi seul).
2. Relancer Claude Code.
3. Coller l'US dans le chat : « analyse cette US », puis « génère les scénarios Gherkin ». Claude charge le skill d'après sa description.

## Enchaînement

1. `us-analysis` sur l'US collée.
2. Réponses du PO aux questions bloquantes.
3. `gherkin-test-generation` sur l'US et la sortie de l'analyse.
4. Relecture humaine des scénarios et des éléments non couverts avant tout usage.

Aucune donnée client réelle dans les US collées : remplacer par des valeurs fictives.

Fichiers encodés en UTF-8.
