# Pitch de la démo : agent QC, nouvelle version et pilote

Durée : 30 minutes, 15 slides. Le même texte est dans les notes de chaque slide (mode Présentateur de PowerPoint).

## À retenir par cœur

1. Ouverture : « Aujourd'hui, je vous montre la nouvelle version de l'agent QC, une démonstration sur une vraie US, et comment on la déploie. À la fin, je vous demanderai votre accord pour un pilote d'une semaine. »
2. Le message clé : « Il prépare, on décide. Ce qui n'est pas clair devient une question, pas un cas de test. »
3. La demande : « J'ai besoin de votre accord pour fusionner la pull request, d'une personne pour relire avec moi, de vérifier le PAT et d'un créneau avec le PO. Si ce n'est pas mieux, on revient en arrière en un clic. »

## Slide par slide

### 1. Agent QC : la nouvelle version et son pilote (0:00 à 0:30)

Bonjour à tous. Aujourd'hui, je vous montre la nouvelle version de l'agent QC : pourquoi on la propose, comment elle fonctionne, une démonstration sur une vraie US, puis comment on la déploie dans GitHub. À la fin, je vous demanderai votre accord pour un pilote d'une semaine sur le sprint 4.

### 2. Ce que je vais vous montrer (0:30 à 1:00)

On a cinq parties, une trentaine de minutes en tout. N'hésitez pas à m'interrompre. Si une question porte sur le déploiement, je vous propose d'y répondre dans la partie 4, c'est prévu.

### 3. Ce que l'agent actuel fait bien (1:00 à 2:30)

Je commence par ce qui marche. L'agent actuel parcourt bien l'écran : les rôles, le panneau, les champs. Il voit que Reprise n'apparaît pas en Renouvellement (TC-005), il teste les bornes du millésime (TC-010), et sa publication dans Azure DevOps est bien outillée. On ne repart pas de zéro : on garde tout ça.

### 4. Pourquoi l'agent actuel n'est pas fiable (2:30 à 5:00)

Le problème est ailleurs : dans la façon d'écrire les cas et de lire les règles. Je prends l'US 417829. Chaque cas tient sur une ligne, sans rôle et sans données : TC-005 dit seulement « le formulaire de création ouvert ». Pour l'exécuter, il faut le réécrire. Et la règle de validation décrit cinq situations, une seule est testée. La troisième colonne montre la cause : ce sont ses consignes, qui demandent une ligne par cas et ne prévoient aucune question au PO. Ce n'est ni l'IA ni les personnes : la consigne produit exactement ce qu'elle demande.

### 5. Ce qu'on propose (5:00 à 6:30)

On propose trois choses. Un : un contexte projet, un fichier du dépôt avec les rôles, les comptes de test, les règles validées et les points ouverts ; l'agent le lit avant chaque US. Deux : on sépare analyser et rédiger. On ne rédige que les règles claires, le reste devient une question au PO. Trois : un humain relit avant toute publication. Et une règle d'or : rien d'inventé.

### 6. Comment il est construit (6:30 à 8:00)

Concrètement, ce sont quatre éléments dans le dépôt. Le fichier de l'agent, à la même place que l'actuel : c'est le chef d'orchestre, il reçoit la demande, choisit l'étape et applique les règles de sécurité. Les skills : une méthode écrite par étape, il ne travaille jamais de tête. Le contexte : la mémoire du projet. Et qc-reports : tout ce qu'il produit est un fichier, qui arrive dans une pull request. Pour l'image : c'est un QC qui a ses fiches méthode et le classeur du projet.

### 7. Comment l'agent travaille (8:00 à 10:00)

Il fait une étape par demande, puis il s'arrête. On commence par la cohérence du sprint, puis l'analyse de chaque US, puis la rédaction des scénarios. Après chaque US, il propose des lignes pour le contexte, et c'est nous qui choisissons ce qui entre. Côté sécurité : aucune écriture dans Azure DevOps sans aperçu et sans « oui ». Sur GitHub, aucun script ne le bloque : le vrai verrou, c'est le PAT en lecture seule.

### 8. Les résultats comparés sur l'US 417829 (10:00 à 12:00)

Voici les résultats sur la même US, avec le même modèle. Le nouvel agent produit 25 cas exécutables, couvre les cinq situations de la règle de validation et pose 14 questions au PO, dont 4 bloquantes. Je précise une chose : il a fallu trois lancements pour régler les consignes, le premier était trop prudent. C'est pour ça que je vous propose de le mesurer sur un pilote, plutôt que de me croire sur parole.

### 9. La règle de validation (12:00 à 13:30)

Le détail de cette règle. En haut, le texte exact de l'US, paragraphe 4. Cinq situations : deux où la création passe, trois où elle est refusée. Si cette règle casse, une entité reçoit une deuxième demande alors qu'une autre est en cours, et aucun des cas actuels ne le verrait. À droite, un cas de refus du nouvel agent : il vérifie aussi que la demande existante n'a pas bougé.

### 10. Sprint 4 : comparer les US avant de les analyser (13:30 à 16:00)

Nouveau depuis la dernière version : avant d'analyser les US une par une, l'agent compare les US du sprint entre elles et avec les sprints précédents. Sur le sprint 4, il relève 27 écarts. Deux exemples. L'US 429428 marque « CHANGEMENT » sur le panneau de création décrit au sprint 1 : l'US 417829 est-elle remplacée sur ce point ? Et pour un engagement déjà utilisé, les US ne donnent ni la même condition ni le même message. Ce ne sont pas 27 erreurs : ce sont 27 questions, chacune avec ses deux sources. Les citations du sprint 3 viennent du contexte : je les vérifie avant d'aller voir le PO.

### 11. Démonstration : une US de bout en bout (16:00 à 22:00)

Je vous montre maintenant une boucle complète sur l'US 429709. Je lance l'analyse. Pendant qu'il travaille : il lit le contexte, il lit l'US, il classe chaque règle en rédigeable, à arbitrer ou exploratoire. Résultat : 15 règles, 8 rédigeables, 7 à arbitrer, 10 questions au PO, verdict « partiellement prête ». Pour la rédaction, je vous montre les 25 cas de l'US 417829 plutôt que d'attendre. Dernière étape : la mise à jour du contexte. Il affiche l'aperçu et me demande s'il applique. Je réponds non : rien n'est écrit. C'est le principe, il prépare et on décide. Si l'exécution est lente : « je vous montre le résultat du 30/10, même commande ».

### 12. Déploiement : remplacer l'agent actuel (22:00 à 25:00)

Pour déployer : une pull request qui remplace l'agent actuel, avec les skills, le contexte et le dossier des rapports. On la relit, on la fusionne sur main ; c'est seulement après la fusion que le nouvel agent est utilisé dans l'onglet Agents. On vérifie que le PAT est en lecture seule. Premier essai : la cohérence du sprint 4, que je compare au rapport que je viens de vous montrer. Et si ce n'est pas au niveau, on clique sur Revert : l'ancien agent revient tel quel.

### 13. Utiliser l'agent dans GitHub (25:00 à 27:00)

Pour l'équipe, rien ne change dans l'outil : onglet Agents, « qc agent », on écrit la demande. L'agent travaille sur une branche et ouvre une pull request avec son fichier. Pour l'étape suivante, on écrit @copilot suivi de la demande dans la même pull request : il garde le contexte des étapes précédentes. On relit, on fusionne.

### 14. Le pilote : une semaine sur le sprint 4 (27:00 à 29:00)

Je propose une semaine sur les quatre US du sprint 4, avec des critères mesurés : les écarts et questions jugés utiles, les cas gardés tels quels ou réécrits, le temps passé, le coût. Repères : dans Claude Code, environ 1,16 dollar et 5 minutes et demie par US pour trois étapes. Sur GitHub, on paie en crédits Copilot : je les mesurerai pendant le pilote. Deux cibles non négociables : zéro cas inventé et zéro écriture dans Azure DevOps sans « oui ».

### 15. Ce que je vous demande (29:00 à 30:00)

Pour lancer le pilote, j'ai besoin de quatre choses : votre accord pour fusionner la pull request, une personne pour relire avec moi pendant la semaine, la vérification des droits du PAT, et un créneau avec le PO pour les questions bloquantes du sprint 4. Et je le redis : si ce n'est pas mieux que l'existant, on revient en arrière en un clic. Merci, je prends vos questions.

## Questions probables

| Question | Réponse |
|---|---|
| Ça remplace les QC ? | Non. Il prépare l'analyse et les brouillons de cas. Les décisions, les questions au PO et la validation restent humaines. |
| Et si l'IA invente ? | Sa règle : ce que les sources ne disent pas devient une question. Chaque écart cite ses deux sources, et on vérifie. Le pilote mesure les cas inventés, cible zéro. |
| Pourquoi on ne le teste pas sur GitHub avant de remplacer ? | GitHub ne propose un agent custom qu'une fois fusionné sur main. Le premier essai se fait donc juste après la fusion, et le Revert permet de revenir en un clic. |
| Il peut écrire dans Azure DevOps ? | Seulement après un aperçu et un « oui ». Sur GitHub, le verrou technique est le PAT en lecture seule. |
| Ça coûte combien ? | Dans Claude Code, environ 1,16 $ par US pour trois étapes. Sur GitHub, en crédits Copilot : je les mesure pendant le pilote. |
| Les 27 écarts, c'est sûr ? | Ce sont 27 questions, pas 27 bugs. Les citations du sprint 3 viennent du contexte, je les vérifie avant d'aller voir le PO. |
| Qui maintient le contexte ? | L'agent propose après chaque US, un humain valide, Git garde l'historique. |
| Et les données client ? | Aucune. Seulement le texte des US, dans le Copilot du dépôt, comme l'agent actuel. |
| Je ne sais pas répondre | « Bonne question, je vérifie et je reviens vers toi aujourd'hui. » |

## Plan B

| Incident | Réaction |
|---|---|
| L'exécution en direct est lente ou plante | « Je vous montre le résultat du 30/10, même commande. » Ouvrir cas-de-test/sprint-4/analyse-US-429709.md |
| La présentation ne s'ouvre pas | Présenter avec doc/comparatif-agent-QC-US-417829.md et le rapport de cohérence |
| On te coupe avec des questions | Une phrase de réponse, puis « je vous montre ça dans deux minutes » |
| Quelqu'un critique durement l'agent actuel | « Il a de bonnes bases, c'est sa consigne qu'on change. » |

## Demain, à 9h

1. Présentation ouverte en mode Présentateur, fichiers de secours ouverts en local (pas Travaux-QA en ligne).
2. Notifications coupées, partage d'écran testé.
3. Relire les trois phrases à retenir.
