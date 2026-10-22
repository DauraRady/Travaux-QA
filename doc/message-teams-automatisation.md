# Message Teams : réponse sur le 100 % automatisé

Bonjour [Prénom],

Pour le 100 % automatisé, je propose de ne pas automatiser tout de suite.

1. L'application est encore jeune : un seul formulaire, pas encore de validation. Des scripts écrits maintenant seraient à reprendre à chaque sprint.
2. Nous n'avons pas d'environnement dédié : la préprod est partagée avec le métier, qui teste après moi, et la prod est exclue.
3. La première passe sur une fonctionnalité nouvelle doit rester manuelle pour repérer ce que les US n'ont pas prévu. La recette métier restera de toute façon manuelle.

Je propose de lancer l'automatisation quand le premier parcours sera complet (de la création à la validation), stable sur un sprint, et que nous aurons un environnement ou des données de test maîtrisés. D'ici là, je prépare le terrain : identification des cas à automatiser en priorité et demande d'identifiants stables aux développeurs.

Une question : le formulaire CAC repose-t-il sur une API que nous pouvons appeler directement ? Si oui, ce serait le premier niveau à automatiser.
