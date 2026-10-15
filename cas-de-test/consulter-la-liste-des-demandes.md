# Consultation de la Liste des demandes : cas de test

Données fictives uniquement. Dans ADO, écrire les paramètres `@role` (et non `<role>`) et saisir leurs valeurs dans la grille Parameter values.

## Données à préparer (avec les développeurs)

| Demande | Statut métier | Créée il y a | Particularité |
|---|---|---|---|
| DEM-TEST-01 | Pending | 5 jours | |
| DEM-TEST-02 | In Progress | 5 jours | |
| DEM-TEST-03 | In Progress | 61 jours | |
| DEM-TEST-04 | Pending | 61 jours | |
| DEM-TEST-05 | In Progress | 60 jours | |
| DEM-TEST-06 | Pending | 60 jours | |
| DEM-TEST-07 | Validated | 10 jours | |
| DEM-TEST-08 | Validated | 90 jours | |
| DEM-TEST-09 | In Progress | 3 jours | Signataire Durabilité non renseigné |
| DEM-TEST-10 | In Progress | 2 jours | Affectée à « Dupont Jean », créée le 15/09/2026 si possible |

Pour les cas de pagination et de liste vide, il faut un environnement où le nombre de demandes visibles est maîtrisé (exactement 10, exactement 11, aucune).

## Cas nominaux

### TC01 Afficher la Liste des demandes avec ses 15 colonnes pour un rôle autorisé
AC-1, Objectif

```gherkin
Plan du scénario: Afficher la Liste des demandes avec ses 15 colonnes pour un rôle autorisé
  Étant donné que l'utilisateur "<utilisateur>" est connecté avec le rôle "<role>"
  Quand il ouvre la Liste des demandes
  Alors le tableau des demandes est affiché
  Et les colonnes suivantes sont visibles dans cet ordre :
    | ID requête | Statut | Affectée à | Date demande | Pays | Millésime | Entité ID | Nom de l'entité | Type entité | Type de mandat | Catégorie de mandat | BU / Région | Signataire certification comptes | Signataire Durabilité | Actions |

  Exemples:
    | utilisateur | role       |
    | US-TEST-01  | User       |
    | AD-TEST-01  | Admin      |
    | SA-TEST-01  | SuperAdmin |
```

### TC02 Afficher le libellé français du statut métier
RG04, AC statuts

```gherkin
Plan du scénario: Afficher le libellé français du statut métier
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que la demande "<demande>" a le statut métier "<statut_metier>" et a été créée il y a 5 jours
  Quand il ouvre la Liste des demandes
  Alors la demande "<demande>" affiche le statut "<statut_affiche>"

  Exemples:
    | demande     | statut_metier | statut_affiche |
    | DEM-TEST-01 | Pending       | Analyse OCR    |
    | DEM-TEST-02 | In Progress   | En cours       |
```

### TC03 Afficher le statut Retard pour une demande créée il y a plus de 60 jours
RG04 calcul du Retard, AC Retard

```gherkin
Plan du scénario: Afficher le statut Retard pour une demande créée il y a plus de 60 jours
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que la demande "<demande>" a le statut métier "<statut_metier>" et a été créée il y a 61 jours
  Quand il ouvre la Liste des demandes
  Alors la demande "<demande>" est affichée
  Et elle affiche le statut "Retard"

  Exemples:
    | demande     | statut_metier |
    | DEM-TEST-03 | In Progress   |
    | DEM-TEST-04 | Pending       |
```

### TC04 Trier les demandes par date de création décroissante
RG06, AC tri

```gherkin
Scénario: Trier les demandes par date de création décroissante
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que les demandes "DEM-TEST-10" (créée il y a 2 jours), "DEM-TEST-09" (3 jours) et "DEM-TEST-02" (5 jours) existent
  Quand il ouvre la Liste des demandes
  Alors "DEM-TEST-10" apparaît avant "DEM-TEST-09"
  Et "DEM-TEST-09" apparaît avant "DEM-TEST-02"
```

### TC05 Afficher 10 demandes par page et naviguer vers la page suivante
RG07, AC pagination

```gherkin
Scénario: Afficher 10 demandes par page et naviguer vers la page suivante
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que 11 demandes non validées sont visibles dans la liste
  Quand il ouvre la Liste des demandes
  Alors 10 demandes sont affichées sur la page 1
  Et la pagination est affichée
  Et le nombre total affiché est "11"
```

Étape complémentaire dans ADO (même cas) : action « Je clique sur la page 2 », résultat attendu « La 11e demande, la plus ancienne, est affichée seule sur la page 2 ; le tri par date décroissante est conservé ».

### TC06 Afficher Affectée à en Nom Prénom et la date au format JJ/MM/AAAA
RG03

```gherkin
Scénario: Afficher Affectée à en Nom Prénom et la date au format JJ/MM/AAAA
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que la demande "DEM-TEST-10" est affectée à "Dupont Jean" et a été créée le "15/09/2026" pour le millésime "2026"
  Quand il ouvre la Liste des demandes
  Alors la colonne Affectée à de "DEM-TEST-10" affiche "Dupont Jean"
  Et la colonne Date demande affiche "15/09/2026"
  Et la colonne Millésime affiche "2026"
```

### TC07 Afficher une cellule vide quand une donnée n'est pas renseignée
RG02, AC valeurs vides

```gherkin
Scénario: Afficher une cellule vide quand une donnée n'est pas renseignée
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que la demande "DEM-TEST-09" n'a pas de signataire Durabilité
  Quand il ouvre la Liste des demandes
  Alors la cellule Signataire Durabilité de "DEM-TEST-09" est vide
```

### TC08 Ouvrir le panneau de création depuis le bouton Nouvelle demande
RG08, AC Nouvelle demande

```gherkin
Scénario: Ouvrir le panneau de création depuis le bouton Nouvelle demande
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et qu'il est sur la Liste des demandes
  Quand il clique sur "Nouvelle demande"
  Alors le panneau de création d'une demande s'ouvre à droite
  Et la Liste des demandes reste visible en arrière-plan
```

## Cas négatifs

### TC09 Une demande Validated n'apparaît pas dans la Liste des demandes
RG05, AC Validated

```gherkin
Scénario: Une demande Validated n'apparaît pas dans la Liste des demandes
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que la demande "DEM-TEST-07" a le statut métier "Validated"
  Quand il ouvre la Liste des demandes
  Alors la demande "DEM-TEST-07" n'est affichée sur aucune page
```

### TC10 Une demande Validated créée il y a plus de 60 jours n'apparaît pas en Retard
RG04 et RG05

```gherkin
Scénario: Une demande Validated créée il y a plus de 60 jours n'apparaît pas en Retard
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que la demande "DEM-TEST-08" a le statut métier "Validated" et a été créée il y a 90 jours
  Quand il ouvre la Liste des demandes
  Alors la demande "DEM-TEST-08" n'est affichée sur aucune page
```

### TC11 La colonne Actions ne propose aucune action
RG09

```gherkin
Scénario: La colonne Actions ne propose aucune action
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que la demande "DEM-TEST-02" est affichée dans la liste
  Quand il consulte la colonne Actions de "DEM-TEST-02"
  Alors aucune action de modification ni de suppression n'est disponible
```

### TC12 Afficher un message d'erreur quand le chargement de la liste échoue
AC erreur technique

```gherkin
Scénario: Afficher un message d'erreur quand le chargement de la liste échoue
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que le service qui fournit les demandes est indisponible
  Quand il ouvre la Liste des demandes
  Alors un message d'erreur est affiché
  Et aucune donnée incohérente n'est présentée
```

## Cas limites

### TC13 Une demande créée il y a exactement 60 jours n'est pas en Retard
RG04 (« Date de création + 60 jours < Date du jour »)

```gherkin
Plan du scénario: Une demande créée il y a exactement 60 jours n'est pas en Retard
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que la demande "<demande>" a le statut métier "<statut_metier>" et a été créée il y a 60 jours
  Quand il ouvre la Liste des demandes
  Alors la demande "<demande>" affiche le statut "<statut_affiche>"

  Exemples:
    | demande     | statut_metier | statut_affiche |
    | DEM-TEST-05 | In Progress   | En cours       |
    | DEM-TEST-06 | Pending       | Analyse OCR    |
```

### TC14 Exactement 10 demandes tiennent sur une seule page
RG07

```gherkin
Scénario: Exactement 10 demandes tiennent sur une seule page
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et que 10 demandes non validées sont visibles dans la liste
  Quand il ouvre la Liste des demandes
  Alors les 10 demandes sont affichées sur la page 1
  Et le nombre total affiché est "10"
```

### TC15 Afficher un tableau vide quand aucune demande n'existe
AC aucune demande

```gherkin
Scénario: Afficher un tableau vide quand aucune demande n'existe
  Étant donné que l'utilisateur "AD-TEST-01" est connecté avec le rôle "Admin"
  Et qu'aucune demande non validée n'existe
  Quand il ouvre la Liste des demandes
  Alors le tableau des demandes est affiché sans aucune ligne
```

## Questions ouvertes

| Q | Question | Cas concerné |
|---|---|---|
| Q1 | Quel statut affiche une demande en « Révision » (visible sur la maquette, absent de RG04) ? | Aucun cas écrit tant que non répondu |
| Q2 | Un User voit-il toutes les demandes, ou seulement celles qui lui sont affectées ? | TC01 |
| Q3 | Quel est le texte exact du message d'erreur, et que signifie « aucune donnée incohérente » à l'écran ? | TC12 |
| Q4 (développeurs) | Comment créer en recette des demandes datées de 60, 61 et 90 jours, vider la liste, et rendre le service indisponible ? | TC03, TC10, TC12, TC13, TC14, TC15 |
