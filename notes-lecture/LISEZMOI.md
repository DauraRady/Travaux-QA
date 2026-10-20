# QC agent : un contexte projet, quatre skills

## Ce que contient le pack

| Fichier | Rôle |
|---|---|
| `.github/agents/qc.agent.md` | L'agent : accès Azure DevOps, règles de sécurité, quel skill pour quelle demande |
| `.github/copilot-instructions.md` | Règles communes à tout le dépôt |
| `.github/skills/us-analysis/SKILL.md` | Analyse d'une US : règles avec leur source et leur statut, préconditions, combinaisons, questions au PO, verdict |
| `.github/skills/gherkin-test-generation/SKILL.md` | Rédaction des scénarios en français, préconditions complètes, actions, résultats exacts |
| `.github/skills/gherkin-test-generation/references/guide-ecriture-gherkin.md` | Exemples bons et mauvais |
| `.github/skills/gherkin-test-generation/scripts/build_tc.py` | Contrôle des scénarios sans IA, construction des cas pour Azure DevOps (API ou CSV) |
| `.github/skills/publication-ado/SKILL.md` | Publication des scénarios relus, après validation |
| `.github/skills/redaction-anomalie/SKILL.md` | Rédaction d'un bug sourcé, recherche de doublons, création après validation |
| `docs/CONTEXTE_PROJET_modele.md` | Modèle du fichier de contexte du projet |

## Installation (une fois, dans le dépôt de l'équipe)

1. Copier `.github/` et `docs/` à la racine du dépôt.
2. Créer `docs/CONTEXTE_PROJET_<projet>.md` à partir du modèle : rôles, comptes de test, statuts, règles validées. Le faire relire par l'équipe.
3. Ajouter `.qc-agent/` au `.gitignore`.
4. Pousser sur une branche et ouvrir une pull request pour relecture.

## Préparer son poste (une fois par personne)

1. Créer un PAT personnel dans Azure DevOps avec les droits Work Items (lecture et écriture) et Test Management (lecture et écriture).
2. Le déclarer comme variable d'environnement `ADO_PAT`, puis redémarrer VS Code.
3. Sous Windows, choisir Git Bash comme terminal par défaut de VS Code.
4. Vérifier que Python est installé (`python --version`). Il sert seulement au script de contrôle, qui ne fait aucun appel réseau.

## Utilisation

Dans VS Code, ouvrir le chat Copilot, choisir « qc agent », puis :

| Je veux | Je tape |
|---|---|
| Analyser une US | `/us-analysis 1234` |
| Écrire les scénarios | `/gherkin-test-generation 1234` |
| Publier les scénarios relus | `/publication-ado 1234` |
| Obtenir un CSV à importer dans Test Plans | `/publication-ado 1234 csv` |
| Rédiger un bug | `/redaction-anomalie` puis ce que j'ai constaté |

Entre la rédaction et la publication, relire et corriger `qc-reports/US-<id>.md`. C'est ce fichier, tel quel, qui est publié.

## Ce qui change par rapport à la version précédente

1. Gherkin en français, une ligne par précondition, action et résultat : `Étant donné que` et `Et que` pour tout ce qui doit être vrai avant (rôle connecté, écran, données), `Quand` et `Et` pour les actions, `Alors` et `Et` pour chaque résultat.
2. Un fichier de contexte projet relu, pour que chaque US ne soit plus traitée isolément.
3. Chaque règle de l'US a un statut : seule une règle claire donne un scénario, les autres deviennent des questions au PO.
4. Plus de tags de traçabilité dans le Gherkin : un tableau de couverture en fin de rapport.
5. Le script accepte les `Et` après `Quand` et refuse les mots-clés anglais.

## À valider avant le déploiement

1. L'administrateur Copilot de l'organisation autorise les agents et les skills du dépôt.
2. La politique IA autorise l'envoi du contenu des US à Copilot.
3. La Test Manager valide le plan par défaut et l'usage d'une suite par US.

## Non vérifié

Le script est testé hors ligne. Aucun appel n'a été fait sur l'Azure DevOps du projet ; le format des paramètres d'un cas paramétré est à vérifier sur un premier cas publié.
