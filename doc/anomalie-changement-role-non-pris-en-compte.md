# Changement de rôle non pris en compte en recette

Date : 29/10/2026
Statut : en cours de qualification
À compléter avant envoi : les passages entre crochets [ ].

## 1. En une phrase

Après un passage du rôle Super admin au rôle User le 28/10 vers 20 h 30, l'application affichait encore l'ancien rôle le 29/10 à 11 h, soit plus de 14 h 30 plus tard, malgré une nouvelle connexion et le vidage du cache du navigateur.

## 2. Ce qui se passe, expliqué simplement

Quand un utilisateur se connecte, l'application doit savoir quel est son rôle pour afficher les bons écrans et autoriser les bonnes actions. Pour ne pas interroger la base à chaque clic, cette information est souvent conservée quelque part pendant un certain temps. Il existe trois endroits possibles :

| Où le rôle peut être conservé | Ce que ça donne | Ce qui le remet à jour |
|---|---|---|
| Le navigateur (cache HTTP, cookies, stockage local) | L'ancien rôle reste visible sur ce poste uniquement | Vider le cache et les cookies, navigation privée |
| La session ou le jeton d'authentification (SSO, jeton JWT) | L'ancien rôle revient même après reconnexion, tant que la session SSO ou le jeton est valide | Expiration du jeton, déconnexion complète du SSO |
| Le serveur (cache applicatif) | L'ancien rôle reste visible pour tout le monde et partout, jusqu'à expiration du cache | Purge du cache côté serveur, ou fin de sa durée de vie |

Ce que mes observations permettent déjà de dire :

1. Le vidage du cache du navigateur n'a rien changé : le cache HTTP du navigateur est peu probable.
2. La nouvelle connexion du 29/10 à 9 h 30 n'a rien changé : une simple session applicative expirée chaque soir est peu probable.
3. Il reste deux causes possibles : une session SSO ou un jeton de longue durée, ou un cache côté serveur. Il en existe une troisième, à ne pas oublier : le changement de rôle n'a peut-être jamais été enregistré.

## 3. Chronologie des faits

| Date et heure | Action | Constat |
|---|---|---|
| 28/10, vers 12 h | Tests avec le rôle [préciser] | [préciser] |
| 28/10, après 12 h | Passage au rôle Super admin | Rôle Super admin effectif |
| 28/10, vers 20 h 30 | Passage au rôle User [préciser comment : sélecteur dans l'application, modification par un administrateur, groupe d'annuaire] | [heure de la dernière vérification de la soirée] : ancien rôle toujours affiché |
| 29/10, 9 h 30 | Nouvelle connexion à l'application | L'affichage correspond toujours à l'ancien rôle : [élément observé, par exemple bouton « Nouvelle demande » présent ou absent] |
| 29/10, 9 h 30 à 11 h | Vidage du cache du navigateur | Aucun changement |
| 29/10, après 11 h | [à compléter] | [rôle User effectif ou toujours pas, et à quelle heure] |

Délai observé : le rôle User n'était toujours pas pris en compte plus de 14 h 30 après le changement. Je n'ai pas vérifié pendant la nuit, je ne peux donc pas donner une durée exacte.

## 4. Ce que j'ai vérifié et ce qui reste

| Vérification | Fait | Résultat |
|---|---|---|
| Vider le cache du navigateur | Oui | Aucun effet |
| Se reconnecter le lendemain | Oui | Aucun effet |
| Navigation privée | Oui | Aucun effet |
| Déconnexion de toutes les applications puis reconnexion | Oui | Aucun effet |
| Vérifier dans l'écran d'administration que le compte porte bien le rôle User | Non | [à faire, ou demander à un dev] |
| Mesurer le délai exact (changement en début de journée, vérification toutes les heures) | Non | Optionnel |

Le contrôle dans l'écran d'administration est le plus important. Si l'administration affiche encore Super admin, il ne s'agit pas d'un cache : c'est le changement de rôle qui ne s'enregistre pas. Le bug change alors complètement de nature.

## 5. Hypothèses

| Hypothèse | Ce qui la soutient | Ce qui la confirmerait |
|---|---|---|
| Cache serveur des droits avec une durée de vie longue | La reconnexion et le vidage du cache navigateur n'ont pas d'effet | Les devs retrouvent un cache sur les droits, avec une durée de 12 h ou plus |
| Session SSO ou jeton de longue durée qui garde l'ancien rôle | Même constat | En navigation privée, avec saisie complète des identifiants, le bon rôle apparaît |
| Le changement de rôle n'a pas été enregistré | Aucun élément ne l'exclut pour l'instant | L'écran d'administration affiche encore Super admin |

Ce sont des hypothèses. Le corps du ticket ne contient que des faits, les hypothèses vont en commentaire.

## 6. Impact

En recette : chaque changement de rôle bloque les tests du nouveau rôle pendant plus d'une demi-journée. Avec trois rôles à couvrir, la campagne devient très lente. Elle produit aussi de faux bugs : un test lancé « en User » est en réalité joué avec un autre rôle.

En production : les utilisateurs ont chacun leur compte, donc ils ne changent pas de rôle au quotidien. Mais les rôles changent quand même : changement de poste, départ d'une équipe, retrait d'un droit. Mon scénario est justement un retrait de droits (Super admin vers User). Si le même mécanisme existe en production, un utilisateur garderait des droits d'administration pendant plusieurs heures après leur retrait. C'est un sujet de sécurité.

## 7. Ticket Azure DevOps prêt à créer

| Champ | Contenu |
|---|---|
| Titre | Changement de rôle : l'ancien rôle reste appliqué plus de 14 h après le passage de Super admin à User, au lieu d'être pris en compte à la connexion suivante |
| Environnement | [environnement], [navigateur et version], compte de test [identifiant fictif], déploiement du [date] |
| Préconditions | Compte de test disposant du rôle Super admin. Rôle effectif constaté avant le test. |
| Étapes | 1. Le 28/10 vers 20 h 30, passer le compte au rôle User [préciser comment]. 2. Se déconnecter. 3. Le 29/10 à 9 h 30, se reconnecter. 4. Observer [élément de l'écran qui dépend du rôle]. 5. Vider le cache du navigateur et recharger. 6. Observer à nouveau. |
| Résultat obtenu | À 9 h 30 puis jusqu'à 11 h, [élément observé], ce qui correspond au rôle Super admin. Le vidage du cache du navigateur ne change rien. |
| Résultat attendu | Les droits du rôle User s'appliquent au plus tard à la connexion suivant le changement. Source : [US ou règle de gestion des habilitations, ou à confirmer avec le PO si rien n'est écrit] |
| Fréquence | Constaté 1 fois sur 1, à rejouer |
| Gravité proposée | 2 - High : bloque la recette des rôles et fausse les résultats, avec un contournement possible (un compte par rôle). À passer en 1 - Critical si le même mécanisme s'applique aux retraits de droits en production. |
| Liens | Related vers les 3 bugs du 28/10 sur le rôle User, et vers l'US des habilitations si elle existe |

Commentaire à ajouter après création (hypothèses) : « Vidage du cache navigateur et reconnexion sans effet. Pistes : cache serveur des droits, session SSO ou jeton de longue durée, ou rôle non enregistré. Pouvez-vous indiquer où le rôle est stocké ou mis en cache, et avec quelle durée de vie ? »

Point d'attention sur le résultat attendu : si aucune US ni règle n'indique quand un changement de rôle doit s'appliquer, c'est d'abord une question au PO. La formulation « au plus tard à la connexion suivante » est ma proposition, pas une règle existante.

## 8. Les 3 bugs créés le 28/10 sur le rôle User

Le 28/10, j'ai créé 3 bugs sur le rôle User en pensant que les habilitations n'étaient pas correctement implémentées. Il est possible que ces tests aient en réalité été joués avec l'ancien rôle. Ce n'est pas encore prouvé : les habilitations peuvent aussi être réellement fausses.

| Option | Avis | Pourquoi |
|---|---|---|
| Les supprimer | Non | On perd la trace de ce qui a été constaté, et la suppression demande souvent des droits particuliers dans Azure DevOps |
| Les fermer tout de suite en doublon | Non | La cause n'est pas confirmée. Si les habilitations sont vraiment fausses, on fermerait de vrais bugs |
| Les garder ouverts, les lier au nouveau bug et les requalifier après un nouveau test | Oui | On garde la traçabilité et on décide sur des faits |

Démarche :

1. Créer le bug principal de la section 7.
2. Sur chacun des 3 bugs, ajouter un lien Related vers le bug principal et ce commentaire : « Requalification en cours : ce test a pu être joué alors que le rôle User n'était pas encore effectif (voir bug #[id]). Je le rejoue dès que le rôle est confirmé. »
3. Si l'équipe utilise un tag ou un état d'attente (par exemple « À requalifier »), l'appliquer.
4. Rejouer les 3 scénarios avec un rôle User confirmé (vérifié dans l'administration ou par un dev).
5. Si l'écart disparaît : fermer le bug avec la raison prévue par le processus de l'équipe (Duplicate ou équivalent) et un lien Duplicate Of vers le bug principal, en écrivant « Écart non reproduit avec le rôle User effectif, causé par le bug #[id] ».
6. Si l'écart persiste : le bug est confirmé, le laisser suivre son cours en précisant « Rejoué avec rôle User confirmé le [date] ».

## 9. Message aux devs (Teams)

> Bonjour, je vous signale un comportement qui bloque ma recette des rôles et qui a peut-être faussé 3 bugs que j'ai ouverts hier.
>
> Hier vers 20 h 30, mon compte de test est passé de Super admin à User. Ce matin à 9 h 30, après reconnexion, l'application appliquait encore le rôle Super admin, et c'était toujours le cas à 11 h. Vider le cache du navigateur ne change rien. J'ouvre un bug avec le détail.
>
> Deux questions pour avancer :
> 1. Où le rôle est-il stocké ou mis en cache (serveur, session SSO, jeton), et avec quelle durée de vie ?
> 2. Pouvez-vous vérifier que le rôle User est bien enregistré sur mon compte ?
>
> Concernant mes 3 bugs d'hier sur le rôle User : je les lie à ce nouveau bug et je les rejoue dès que le rôle est confirmé. Je ferme ceux qui ne se reproduisent pas.
>
> Pour ne pas bloquer la recette, serait-il possible d'avoir un compte de test par rôle, ou un moyen de purger ce cache en recette ?
>
> Merci !

## 10. Propositions de solutions

Pour débloquer la recette tout de suite :

1. Un compte de test fixe par rôle (Super admin, [rôle 2], User). C'est la solution la plus simple, et elle correspond à l'usage réel : en production chacun a son compte.
2. Un moyen de purger le cache en recette (action d'administration ou appel réservé à l'équipe).

Pour le produit, à discuter avec les devs :

1. Invalider le cache des droits au moment où un rôle change.
2. Réduire fortement la durée de cache des informations d'habilitation.

Piège à éviter : si on raccourcit le cache seulement en recette, on ne teste plus le comportement de production. Il faut garder au moins un test qui vérifie le délai réel de prise en compte d'un retrait de droits.

## 11. Ce que j'ajoute à ma façon de tester

1. Avant chaque campagne sur un rôle, vérifier que le rôle est effectif (un élément de l'écran propre à ce rôle) et le noter dans le résultat du test.
2. Ajouter un cas de test « retrait de droits » : passer un compte de Super admin à User et mesurer le délai de prise en compte.
3. Demander des comptes dédiés par rôle dans les prérequis de recette.
