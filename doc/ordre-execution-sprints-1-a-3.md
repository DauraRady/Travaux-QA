# Ordre d'exécution des sprints 1 à 3

Rédigé le 27/10/2026. La préprod est accessible ; les comptes par rôle et les données restent à confirmer. Ce document dit quoi exécuter en premier, et pourquoi.

Le principe : d'abord ce dont tout dépend (la création d'une demande), ensuite ce qui peut envoyer des données fausses ou ouvrir des droits en trop, enfin l'affichage. Si le temps manque, on coupe par la fin, jamais par le début.

## Étape 0 : préparer (1 à 2 j)

1. Vérifie ton rôle dans Paramètres, et obtiens un compte par rôle : Admin, SuperAdmin, User. Un compte avec deux rôles fausse tous les résultats de droits.
2. Vérifie ce qui est déployé : numéro d'engagement dans le panneau de création, Catégorie d'entité et marchés de cotation dans la Description du mandat. Une US absente de la préprod ne s'exécute pas, elle se note « non livrée ».
3. Relève les données réelles : entités neuves sans demande (il en faut une par création réussie), engagements libres, et fais la correspondance avec les identifiants fictifs du README du sprint 3.
4. Demande aux développeurs les demandes à injecter : DEM-TEST-01 et DEM-TEST-04 (validées), DEM-RECH-04 (validée), DEM-TEST-08 (titre spécial).
5. Pour les cas « par l'API », demande le Swagger et la façon d'obtenir un jeton derrière le SSO. Sans jeton, ces cas attendent ; ne les remplace pas par des tests à l'écran, ils ne vérifient pas la même chose.

## Étape 1 : test de fumée (une demi-journée)

| Cas | Ce qu'il prouve |
|---|---|
| TC01 de `creer-une-demande.md` | On peut créer une demande |
| Affichage de la liste (`consulter-la-liste-des-demandes.md`) | La liste se charge avec ses colonnes |
| TC02 de `filtrer-les-demandes.md` sur un filtre | Les filtres répondent |
| HEAD-01 | Le formulaire d'une demande s'ouvre |

Si TC01 échoue, arrête-toi et ouvre une anomalie bloquante : presque tous les autres cas en dépendent.

## Étape 2 : sprints 1 et 2 (4,5 à 5 j avec retests)

1. Création, TC01 à TC09 : c'est la base de tout le sprint 3. TC03 (le User ne crée pas) et TC07 (une seule demande en cours par entité) en premier.
2. Liste des demandes : statut Retard (60 jours pile et 61 jours), demandes validées exclues, échec du chargement.
3. Filtres : combinaisons, absence de résultat, Certification des comptes sans Durabilité.
4. Side panel Discovery et groupes de sécurité : retrouver les cas (voir l'écart signalé dans l'estimation) avant de les planifier.

## Étape 3 : sprint 3, première passe avec un seul profil (71 exécutions, 5 à 6 j)

Chaque scénario est joué une fois avec le compte Admin, plus les cas réservés au User (DM-04, DM-05) et au SuperAdmin (HEAD-04).

| Priorité | Cas | Exécutions | Pourquoi d'abord |
|---|---|---|---|
| 1 | ENG-01 à ENG-16, CTRL-01 et CTRL-02 | 21 | Un mauvais engagement part vers la finance : c'est l'erreur la plus coûteuse du sprint |
| 1 | DM-04, DM-05 | 2 | Un User qui écrit est une faille de droits |
| 1 | EIP-10, EIP-11, MC-08, MC-09 | 4 | Une règle contrôlée seulement à l'écran laisse passer des données incohérentes vers les flux sortants |
| 2 | EIP-01 à EIP-09, MC-01 à MC-07, TAX-01 à TAX-05, DA-01, DA-02 | 26 | Les règles de cascade : c'est là que le sprint 3 a le plus de logique, et les retours en arrière cachent les anomalies |
| 3 | HEAD-01 à HEAD-05, TIT-01 à TIT-05, RECH-01 à RECH-05, DM-01 à DM-03 | 18 | Affichage, navigation, recherche : visibles, mais sans effet sur les données |

Recharge la page après chaque saisie qui doit être enregistrée : une valeur visible n'est pas forcément enregistrée.

## Étape 4 : second profil habilité (68 exécutions, 4,5 à 5,5 j)

1. D'abord les 22 exécutions SuperAdmin où le rôle peut changer la réponse du serveur : ENG-01 à ENG-16, EIP-10, EIP-11, MC-08, MC-09.
2. Ensuite les 46 autres, si le planning le permet. Sinon, propose au PO un échantillon : une règle de cascade ne change pas selon le profil, sauf si le code teste le rôle.

C'est un choix à faire valider : tu as rédigé tous les profils, tu peux décider de ne pas tous les exécuter à chaque passe, à condition de le dire.

## En parallèle : une session exploratoire d'une heure

Sur la Description du mandat, avec une demande déjà remplie : changer la catégorie, la catégorie d'entité et le marché 1 dans tous les sens, recharger, revenir en arrière. Note ce que l'écran fait quand la règle n'est pas décrite (MC-06, sortie d'EIP) et transforme chaque surprise en question au PO ou en anomalie.

## Ce qui reste bloqué

Les cas de la section « Non rédigé » de chaque fichier attendent une réponse du PO. Les quatre à relancer en premier, parce que ce sont les principaux cas d'erreur du sprint : Q-21 (champs obligatoires vides), Q-19 (Entité ID inconnue), Q-27 (sortie d'EIP), Q-32 (recherche partielle).
