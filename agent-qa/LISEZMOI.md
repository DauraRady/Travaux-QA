# QC agent : un agent, quatre skills

## Ce que contient le pack

| Fichier | Rôle |
|---|---|
| `.github/agents/qc.agent.md` | L'agent : accès Azure DevOps, règles de sécurité, quel skill pour quelle demande |
| `.github/skills/analyse-us/SKILL.md` | Méthode d'analyse d'une US : sources, statut par critère, questions pour le PO |
| `.github/skills/redaction-gherkin/SKILL.md` | Méthode de rédaction des cas en Gherkin, avec le script de contrôle et le guide d'écriture |
| `.github/skills/publication-ado/SKILL.md` | Publication des cas relus dans Test Plans, après validation |
| `.github/skills/redaction-anomalie/SKILL.md` | Rédaction d'un bug sourcé, recherche de doublons, création après validation |
| `.github/copilot-instructions.md` | Règles communes à tout le dépôt |

## Installation (une fois, dans le dépôt de l'équipe)

1. Copier le dossier `.github/` à la racine du dépôt.
2. Ajouter `.qc-agent/` au `.gitignore`.
3. Pousser sur une branche et ouvrir une pull request pour relecture.

## Préparer son poste (une fois par personne)

1. Créer un PAT personnel dans Azure DevOps (User settings, Personal access tokens) avec les scopes Work Items Read & Write et Test Management Read & Write. Chacun utilise le sien : les créations apparaissent à son nom.
2. Le déclarer comme variable d'environnement `ADO_PAT` (Windows : Paramètres système, Variables d'environnement utilisateur), puis redémarrer VS Code.
3. Sous Windows, choisir Git Bash comme terminal par défaut de VS Code (les commandes de l'agent sont écrites en bash).
4. Vérifier que Python est installé (`python --version`).

Sur GitHub.com (onglet Agents), le PAT est enregistré une fois comme secret du dépôt par un administrateur.

## Utilisation

Dans VS Code, ouvrir le chat Copilot, choisir « qc agent » dans la liste des agents, puis :

| Je veux | Je tape |
|---|---|
| Analyser une US | `/analyse-us 1234` |
| Écrire les cas de test | `/redaction-gherkin 1234` |
| Publier les cas relus | `/publication-ado 1234` |
| Rédiger un bug | `/redaction-anomalie` puis ce que j'ai constaté |

Entre la rédaction et la publication, relire et corriger `qc-reports/US-<id>.md`. C'est ce fichier, tel quel, qui est publié.

## À valider avant le déploiement

1. L'administrateur Copilot de l'organisation autorise les agents et les skills du dépôt.
2. La politique IA autorise l'envoi du contenu des US à Copilot.
3. La Test Manager valide le plan par défaut et l'usage d'une suite par US.

## Non vérifié

Aucun appel n'a été fait sur l'Azure DevOps du projet. Le script de contrôle et l'exemple de rapport sont testés hors ligne. Le format des paramètres d'un cas paramétré est à vérifier sur un premier cas publié.
