# Message Teams : réponse sur le 100 % automatisé

Version à envoyer, mise à jour le 23/10/2026.

Bonjour [Prénom],

Pour le 100 % automatisé, je propose de ne pas démarrer l'automatisation tout de suite.

1. Beaucoup d'éléments de la création ne sont pas encore finalisés (demande de mandat, puis formulaire CAC) et des champs sont ajoutés à chaque sprint. Des scripts écrits maintenant seraient à reprendre en continu.
2. La première passe sur une fonctionnalité nouvelle doit rester manuelle pour repérer ce que les US n'ont pas prévu. La recette métier restera de toute façon manuelle.
3. Je n'ai pas d'environnement pour automatiser : pas d'ITG, et pas encore d'accès à la préprod, qui sera de toute façon partagée avec le métier. Lancés là, les tests échoueraient pour de mauvaises raisons (données modifiées, déploiements en cours) et créeraient des demandes visibles dans la recette métier.
4. Je n'ai pas encore de comptes de test. Sans un compte dédié par rôle (User, Admin, Super Admin), on ne peut ni tester les droits ni faire tourner les tests dans la CI, et utiliser des comptes nominatifs poserait un problème de sécurité et de traçabilité.

Je propose de lancer l'automatisation vers le sprint 6 ou 7, si les parcours sont stabilisés et ces prérequis obtenus. D'ici là, je prépare le terrain : identification des cas à automatiser en priorité, demande d'identifiants stables aux développeurs, demandes d'accès à la préprod, d'un environnement de test et de comptes dédiés. Le POC et le planning sont détaillés dans la présentation sur la vision d'automatisation.

En parallèle, je peux tester l'agent QA sur les US de Conf Portal (analyse des US et génération des cas de test) pour voir ce qu'il apporte concrètement avant de l'étendre.

Une question : le formulaire repose-t-il sur une API que nous pouvons appeler directement ? Si oui, ce serait le premier niveau à automatiser.

---

## Si elle demande des détails : les risques sans environnement ni comptes dédiés

Sans environnement dédié à l'automatisation :

| Risque | Ce qui se passe concrètement |
|---|---|
| Faux échecs | Une donnée modifiée par le métier ou un déploiement en cours fait échouer un test alors que l'application fonctionne. L'équipe perd confiance et finit par ignorer les échecs. |
| Pollution de la recette métier | Chaque exécution crée des demandes de mandat que le métier voit dans ses listes et ses tableaux de bord, et qui peuvent alimenter les applications aval (Déclaration d'Activités, MyRotations). |
| Détection tardive | La préprod est la dernière étape avant la prod. Une régression y est vue en fin de chaîne, au lieu du lendemain de la livraison. |
| Pas d'exécution maîtrisée | On ne choisit ni le moment ni la version déployée : impossible de lancer la suite chaque nuit ou à chaque déploiement de façon fiable. |
| Pas d'isolation | Impossible de remettre les données dans un état connu avant chaque test, ni d'exécuter des tests en parallèle sans collision. |

Sans comptes dédiés à l'automatisation :

| Risque | Ce qui se passe concrètement |
|---|---|
| Droits non testables | Avec un seul compte, on ne vérifie ni ce qu'un User ne doit pas pouvoir faire, ni ce que seuls l'Admin et le Super Admin peuvent faire. C'est l'un des trois risques majeurs du projet. |
| Sécurité et traçabilité | Un compte nominatif dans un pipeline expose ses identifiants, et les actions des tests sont attribuées à une vraie personne dans les traces. |
| Blocages techniques | Authentification forte, mot de passe expiré, compte verrouillé après des échecs : la suite s'arrête sans que l'application soit en cause. |
| Collisions | Un test et une personne connectés sur le même compte se déconnectent mutuellement ou modifient les mêmes données. |
| Dépendance à une personne | Si la suite repose sur mon compte, elle s'arrête à mon départ, ce qui rend la passation de fin décembre impossible. |
