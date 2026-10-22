# Message Teams : réponse sur le 100 % automatisé

Bonjour [Prénom],

Pour le 100 % automatisé : oui pour démarrer l'automatisation dès maintenant, non pour viser zéro test manuel.

1. La recette métier restera manuelle : les équipes métier testent sur la préprod après moi. L'automatisation porte donc sur la validation QA en amont.
2. La préprod est partagée avec le métier et la prod est exclue. Des tests automatisés y créeraient des données visibles dans leur recette, sauf avec des données identifiables et un nettoyage systématique (ou une exécution sur le dev).
3. L'application est encore jeune (un seul formulaire, pas de validation) : des scripts écrits maintenant seraient à reprendre à chaque sprint.

Ma proposition : poser dès maintenant le framework, la CI et les tests API si c'est possible, faire une première passe manuelle sur chaque US, puis automatiser les cas stables pour construire la régression.

Deux questions pour avancer :
1. Le formulaire CAC repose-t-il sur une API que nous pouvons appeler directement ?
2. Pouvons-nous exécuter nos tests automatisés sur le dev, ou à quelles conditions sur la préprod ?
