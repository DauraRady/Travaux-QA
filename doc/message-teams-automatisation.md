# Message Teams : réponse sur le 100 % automatisé

Version à envoyer, mise à jour le 23/10/2026.

Bonjour [Prénom],

Pour le 100 % automatisé, je propose de ne pas démarrer l'automatisation tout de suite.

1. Les parcours ne sont pas encore finalisés : création de la demande de mandat, puis formulaire CAC. Des champs sont ajoutés à chaque sprint, donc des scripts écrits maintenant seraient à reprendre en continu.
2. La première passe sur une fonctionnalité nouvelle doit rester manuelle pour repérer ce que les US n'ont pas prévu. La recette métier restera de toute façon manuelle.
3. Côté environnement, la préprod est partagée avec le métier. La prod privatisée pourrait servir à quelques tests de vérification, mais pas à toute la recette.
4. Nous n'avons pas encore de comptes de test. Sans eux, aucun test automatisé n'est possible, quel que soit l'environnement.

Je propose de lancer l'automatisation vers le sprint 6 ou 7, une fois les parcours stabilisés. D'ici là, je prépare le terrain : identification des cas à automatiser en priorité, demande d'identifiants stables aux développeurs, et demande de comptes de test dédiés (un par profil utilisateur) pour qu'ils soient prêts à temps. C'est cohérent avec la vision d'automatisation présentée : un POC Playwright sur deux sprints, lancé dès que ces prérequis sont réunis, puis une suite ciblée de 5 à 10 scénarios plutôt qu'un pourcentage.

En parallèle, je peux tester l'agent QA sur les US de Conf Portal (analyse des US et génération des cas de test) pour voir ce qu'il apporte concrètement avant de l'étendre.

Une question : le formulaire repose-t-il sur une API que nous pouvons appeler directement ? Si oui, ce serait le premier niveau à automatiser.
