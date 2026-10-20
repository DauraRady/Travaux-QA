# CONTEXTE PROJET : [NOM DU PROJET]

Fichier lu par l'agent QC avant chaque analyse d'US. Il donne le vocabulaire, les rôles, les statuts, les règles déjà validées et les données de test du projet, pour que chaque US ne soit pas analysée isolément.

| En-tête | Valeur |
|---|---|
| Dernière mise à jour | [date] |
| Responsable | [nom ou rôle] |
| Version | [version] |

Règles de tenue du fichier :

1. Une ligne n'entre ici que si elle a une source (US, décision du PO, PRD, maquette citée). Sans source, elle va en section 9.
2. Une règle remplacée n'est pas supprimée : son statut passe à `remplacée` et la colonne « Remplacée par » est remplie.
3. Ce fichier ne remplace jamais l'US en cours : il la complète.

## 1. Le projet en cinq lignes

| Question | Réponse |
|---|---|
| Ce que fait l'application | |
| Qui l'utilise | |
| Ce qu'elle remplace | |
| Systèmes connectés | |
| Mise en production | |

## 2. Sources

| ID | Document ou décision | Date ou version | État (à jour, partiel, historique) | Emplacement |
|---|---|---|---|---|
| SRC-01 | | | | |

## 3. Rôles et droits

| Rôle | Peut faire | Ne peut pas faire | Source | Statut |
|---|---|---|---|---|
| [rôle] | [actions] | [interdictions] | [source] | confirmé / à confirmer / remplacé |

## 4. Connexion et comptes de test

C'est ici que l'agent trouve comment écrire la précondition « connecté avec le rôle … ».

| Compte fictif | Rôle | Environnement | Particularité | Usage |
|---|---|---|---|---|
| USR-TEST-01 | [rôle] | [ITG, PREPROD] | [ex. affecté à aucune demande] | [ex. cas nominaux] |

Écran d'arrivée après connexion : [écran]

## 5. Objets métier, statuts et transitions

### Objets

| Objet | Définition | Variantes | Source | Statut |
|---|---|---|---|---|
| [objet] | | [ex. Nouveau, Renouvellement] | | |

### Statuts

| Objet | Statut affiché | Signification | Source | Statut |
|---|---|---|---|---|
| | | | | |

### Transitions

| Objet | Statut de départ | Action | Statut d'arrivée | Rôle autorisé | Source | Statut |
|---|---|---|---|---|---|---|
| | | | | | | |

## 6. Règles transverses et décisions

Une seule table pour les règles qui valent pour plusieurs US et les décisions du PO.

| ID | Règle ou décision | Périmètre | Source et date | Statut | Remplacée par |
|---|---|---|---|---|---|
| RT-01 | | | | confirmée / remplacée | [ID ou vide] |

## 7. Écrans

| Écran | Comment on y accède | Ce qu'il affiche | Actions possibles | Source |
|---|---|---|---|---|
| | | | | |

Ne pas déduire l'existence d'un export, d'une recherche, d'une API ou d'une pièce jointe qui n'est pas citée par une source.

## 8. Données de test

Toutes les données sont fictives. Elles ne créent aucune règle métier.

| ID fictif | Objet | État | Particularité utile aux tests |
|---|---|---|---|
| DEM-TEST-01 | [objet] | [statut] | [ex. créée il y a 61 jours] |

## 9. Points à confirmer et écarts

Une ligne ouverte ne produit aucun résultat attendu.

| ID | Sujet | Ce qui est connu | Question | Bloquante ? | État (ouvert, répondu) |
|---|---|---|---|---|---|
| CONF-01 | | | | oui / non | |

## 10. Journal

| Date | Auteur | Sections modifiées | Motif |
|---|---|---|---|
| | | | |
