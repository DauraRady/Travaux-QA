# Test des skills sur l'US 417829 « Créer une nouvelle demande »

Résultat obtenu en appliquant `us-analysis` puis `gherkin-test-generation` à l'US complète (sections 1 à 5), puis comparé au résultat de l'agent QC actuel sur la même US.

# Partie A : sortie de us-analysis

## 1. Sources

1. US 417829, description complète (sections 1 à 5).
2. Contexte projet : pas encore de fichier. Un fait connu du projet est utilisé et signalé : les rôles sont User, Admin et SuperAdmin. À reporter dans le fichier de contexte.
3. Maquettes Figma citées par l'US pour les messages : non fournies.

## 2. Règles

| ID | Règle | Source | Statut | Question |
|---|---|---|---|---|
| R1 | Le bouton « Nouvelle demande » est visible uniquement pour Admin et SuperAdmin | §1 | Rédigeable | |
| R2 | Le clic ouvre un panneau à droite avec le formulaire ; le reste de l'écran reste visible | §2 | Rédigeable | |
| R3 | Renouvellement affiche : Entité ID, N° Requête BSC, Affectée à, Millésime | §3 | Rédigeable | |
| R4 | Nouveau affiche en plus : Reprise (Oui, Non) | §3 | Rédigeable | |
| R5 | Entité ID : pas de saisie libre d'un code | §3 | À arbitrer | Q6 |
| R6 | Nouveau : une Entité ID inconnue à la validation met le champ et son titre en rouge, avec le message « entité ID inconnue » | §3 | À arbitrer | Q1 |
| R7 | Affectée à : par défaut l'utilisateur connecté ; recherche par nom et prénom d'un collaborateur KPMG | §3 | Rédigeable (nom inconnu : Q5) | |
| R8 | Millésime : par défaut l'année fiscale en cours | §3 | Rédigeable | |
| R9 | Renouvellement : Millésime de l'année en cours moins 20 ans à plus 10 ans | §3 | Rédigeable | |
| R10 | Nouveau : dates du Millésime décrites dans l'US 424139 | §3 | À arbitrer | Q4 |
| R11 | Tous les champs sont obligatoires ; un champ vide est refusé à la validation avec un message d'erreur | §3, §4 | Rédigeable (texte du message : Q2) | |
| R12 | La validation vérifie les règles métier liées à la nature du mandat | §4 | À arbitrer | Q7 |
| R13 | La validation vérifie la présence des documents obligatoires | §4 | À arbitrer (liste) | Q3 |
| R14 | Création possible si l'entité n'a pas de demande ou une demande au statut Validé ; erreur si elle a une demande En cours, Retard ou Révision | §4 | Rédigeable (texte du message : Q2) | |
| R15 | Contrôles conformes : la demande est créée et l'utilisateur est redirigé vers la page du formulaire ; un message de confirmation apparaît | §4, §5 | Rédigeable (texte du message : Q2 ; page exacte : Q9) | |

## 3. Préconditions et combinaisons

| Précondition | Valeur | Source |
|---|---|---|
| Rôle connecté | Admin `ADM-TEST-01`, SuperAdmin `SUP-TEST-01` ; User `USR-TEST-01` pour le refus | US « En tant que » ; rôle User : fait connu du projet |
| Écran de départ | « Liste des demandes » | §1 |
| Entités | Une entité par statut de demande à tester (`ENT-TEST-01` à `ENT-TEST-05`) | §4 |
| Collaborateur | `COLLAB-TEST-02` connu du référentiel | §3 |
| Documents | Les documents obligatoires de la nature choisie (liste : Q3) | §4 |

| Statut de la demande existante sur l'entité | Résultat à la validation | Source |
|---|---|---|
| Aucune demande | Demande créée | R14 |
| Validé | Demande créée | R14 |
| En cours | Erreur, pas de création | R14 |
| Retard | Erreur, pas de création | R14 |
| Révision | Erreur, pas de création | R14 |

| Rôle | Bouton | Source |
|---|---|---|
| Admin, SuperAdmin | Affiché | R1 |
| User | Absent | R1 (« uniquement ») |

Limites : Millésime en Renouvellement, bornes moins 20 ans et plus 10 ans (R9).

## 4. Questions au PO

| ID | Règle | Question | Bloquante |
|---|---|---|---|
| Q1 | R5, R6 | Une Entité ID inconnue peut être refusée, mais la saisie libre est impossible : comment l'utilisateur peut-il choisir une entité inconnue ? | Oui, pour R6 |
| Q2 | R11, R14, R15 | Quels sont les textes exacts des messages de confirmation et d'erreur (maquettes citées, non fournies) ? | Non : les scénarios sont écrits, le texte est à compléter |
| Q3 | R13 | Quels documents sont obligatoires, pour quelle nature ? | Oui, pour exécuter les cas de création |
| Q4 | R10 | Quelle plage de millésimes est proposée en Nouveau (US 424139 non fournie) ? | Non |
| Q5 | R7 | Que se passe-t-il si le nom saisi dans Affectée à ne correspond à aucun collaborateur ? | Non |
| Q6 | R5 | L'Entité ID se choisit-elle dans une liste ou par recherche ? | Non |
| Q7 | R12 | Quelles règles métier liées à la nature sont vérifiées à la validation ? | Non |
| Q8 | R14 | Un Renouvellement est-il possible sur une entité qui n'a encore aucune demande ? | Non |
| Q9 | R15 | Vers quelle page exactement l'utilisateur est-il redirigé après la création ? | Non |

## 5. Verdict

Partiellement prête : l'accès, le formulaire, les champs obligatoires et la règle du statut de l'entité sont rédigeables. Le refus d'une entité inconnue attend Q1, et l'exécution des cas de création attend la liste des documents (Q3).

# Partie B : sortie de gherkin-test-generation

## 1. Scénarios

```gherkin
Fonctionnalité: Créer une nouvelle demande

  Plan du scénario: Un Admin ou un SuperAdmin voit le bouton de création
    Étant donné que l'utilisateur "<compte>" est connecté avec le rôle "<role>"
    Quand il ouvre la page "Liste des demandes"
    Alors le bouton "Nouvelle demande" est affiché

    Exemples:
      | cas             | compte      | role       |
      | rôle Admin      | ADM-TEST-01 | Admin      |
      | rôle SuperAdmin | SUP-TEST-01 | SuperAdmin |

  Scénario: Un User ne voit pas le bouton de création
    Étant donné que l'utilisateur "USR-TEST-01" est connecté avec le rôle "User"
    Quand il ouvre la page "Liste des demandes"
    Alors la liste des demandes s'affiche
    Mais le bouton "Nouvelle demande" n'est pas affiché

  Scénario: Le formulaire de création s'ouvre dans un panneau à droite
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et qu'il est sur la page "Liste des demandes"
    Quand il clique sur "Nouvelle demande"
    Alors un panneau s'ouvre sur la droite de l'écran
    Et le formulaire de création d'une demande est affiché dans ce panneau
    Et la "Liste des demandes" reste visible en arrière-plan

  Scénario: Le parcours Renouvellement affiche quatre champs, sans Reprise
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et que le panneau de création est ouvert depuis la page "Liste des demandes"
    Quand il choisit la valeur "Renouvellement" dans le champ "Nature du mandat"
    Alors les champs "Entité ID", "N° Requête BSC", "Affectée à" et "Millésime" sont affichés
    Mais le champ "Reprise" n'est pas affiché

  Scénario: Le parcours Nouveau affiche aussi le champ Reprise
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et que le panneau de création est ouvert depuis la page "Liste des demandes"
    Quand il choisit la valeur "Nouveau" dans le champ "Nature du mandat"
    Alors les champs "Entité ID", "Reprise", "N° Requête BSC", "Affectée à" et "Millésime" sont affichés
    Et le champ "Reprise" propose les valeurs "Oui" et "Non"

  Plan du scénario: Affectée à et Millésime sont préremplis
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et que le panneau de création est ouvert depuis la page "Liste des demandes"
    Quand il choisit la valeur "<nature>" dans le champ "Nature du mandat"
    Alors le champ "Affectée à" contient l'utilisateur "ADM-TEST-01"
    Et le champ "Millésime" contient l'année fiscale en cours

    Exemples:
      | cas            | nature         |
      | renouvellement | Renouvellement |
      | nouveau        | Nouveau        |

  Plan du scénario: Bornes de la liste Millésime en Renouvellement
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et que le panneau de création est ouvert avec la nature "Renouvellement"
    Quand il ouvre la liste du champ "Millésime"
    Alors le millésime "<millesime>" est <presence> dans la liste

    Exemples:
      | cas                  | millesime                   | presence |
      | borne basse          | année en cours moins 20 ans | proposé  |
      | juste avant la borne | année en cours moins 21 ans | absent   |
      | borne haute          | année en cours plus 10 ans  | proposé  |
      | juste après la borne | année en cours plus 11 ans  | absent   |

  Scénario: Un collaborateur est proposé quand on saisit son nom dans Affectée à
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et que le collaborateur "COLLAB-TEST-02" existe dans le référentiel des collaborateurs
    Et que le panneau de création est ouvert avec la nature "Renouvellement"
    Quand il efface le champ "Affectée à"
    Et qu'il saisit le nom et le prénom de "COLLAB-TEST-02"
    Alors "COLLAB-TEST-02" est proposé dans la liste de résultats

  Plan du scénario: La création est acceptée si l'entité n'a pas de demande en cours
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et que l'entité "<entite>" <etat_entite>
    Et que le panneau de création est ouvert avec la nature "<nature>"
    Et que tous les champs obligatoires sont renseignés avec l'entité "<entite>"
    Et que les documents obligatoires de la nature "<nature>" sont joints
    Quand il clique sur "Valider la création"
    Alors une nouvelle demande pour l'entité "<entite>" est créée
    Et un message de confirmation s'affiche
    Et l'utilisateur est redirigé vers la page du formulaire

    Exemples:
      | cas                            | entite      | etat_entite                                   | nature         |
      | nouveau, aucune demande        | ENT-TEST-01 | n'a aucune demande                            | Nouveau        |
      | nouveau, demande validée       | ENT-TEST-02 | a une demande "DEM-TEST-02" au statut "Validé" | Nouveau        |
      | renouvellement, demande validée | ENT-TEST-02 | a une demande "DEM-TEST-02" au statut "Validé" | Renouvellement |

  Plan du scénario: La création est refusée si l'entité a déjà une demande en cours de traitement
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et que l'entité "<entite>" a une demande "<demande>" au statut "<statut>"
    Et que le panneau de création est ouvert avec la nature "Nouveau"
    Et que tous les champs obligatoires sont renseignés avec l'entité "<entite>"
    Et que les documents obligatoires de la nature "Nouveau" sont joints
    Quand il clique sur "Valider la création"
    Alors un message d'erreur s'affiche
    Et aucune nouvelle demande pour l'entité "<entite>" n'est créée
    Et la demande "<demande>" est toujours au statut "<statut>"

    Exemples:
      | cas       | entite      | demande     | statut   |
      | en cours  | ENT-TEST-03 | DEM-TEST-03 | En cours |
      | en retard | ENT-TEST-04 | DEM-TEST-04 | Retard   |
      | révision  | ENT-TEST-05 | DEM-TEST-05 | Révision |

  Plan du scénario: Un champ obligatoire vide bloque la création
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et que l'entité "ENT-TEST-01" n'a aucune demande
    Et que le panneau de création est ouvert avec la nature "Renouvellement"
    Et que tous les champs sont renseignés sauf "<champ>"
    Quand il clique sur "Valider la création"
    Alors un message d'erreur s'affiche
    Et aucune nouvelle demande n'apparaît dans la "Liste des demandes"

    Exemples:
      | cas                    | champ          |
      | entité absente         | Entité ID      |
      | requête BSC absente    | N° Requête BSC |
      | affectation effacée    | Affectée à     |
      | millésime effacé       | Millésime      |
```

Les messages d'erreur et de confirmation sont écrits sans leur texte : il est dans les maquettes, non fournies (Q2). Dès la réponse, remplacer « un message … s'affiche » par le texte exact.

## 2. Couverture

| Section de l'US | Scénarios | Couvert ? |
|---|---|---|
| §1 Accès | Plan rôles Admin et SuperAdmin ; User sans bouton | Couvert |
| §2 Panneau | Ouverture à droite | Couvert |
| §3 Renouvellement | Quatre champs ; préremplissage ; bornes du millésime ; recherche d'un collaborateur | Couvert, sauf Entité ID (Q6) |
| §3 Nouveau | Champ Reprise ; préremplissage | Partiel : entité inconnue (Q1), plage du millésime (Q4) |
| §4 Validation | Statut de l'entité (5 cas) ; champs obligatoires (4 cas) | Partiel : documents (Q3), règles liées à la nature (Q7), textes des messages (Q2) |
| §5 Création | Création et redirection (3 cas) | Couvert, page exacte à confirmer (Q9) |

## 3. Non rédigé

R5 et R6 (Q1, Q6), R10 (Q4), R12 (Q7), R13 en tant que contrôle des documents (Q3), Affectée à avec un nom inconnu (Q5).

# Partie C : comparaison avec l'agent QC actuel

Base : sa sortie sur la même US (TC-001 à TC-014, début de TC-015 sur un champ obligatoire vide, et sa liste de cas d'interface).

| Point | Agent QC actuel | Notre version |
|---|---|---|
| Langue et forme | Une ligne Given, When, Then en anglais par cas, dans un tableau ; colonne « Type : Fonctionnel » sur chaque ligne | Gherkin en français ; préconditions, actions et résultats sur des lignes séparées |
| Préconditions | « Given le formulaire de création ouvert » (TC-005, 006, 009) : ni rôle, ni écran ; « une entité valide » (TC-013, 014) sans identifiant | Chaque scénario dit le rôle et le compte, l'écran de départ, l'entité et le statut de sa demande, les documents joints |
| Rôles | « un rôle autre qu'Admin ou SuperAdmin » (TC-003) | Rôle User nommé, avec son compte de test |
| Règle clé de la validation (§4) : statut de l'entité | Un seul cas : entité sans demande (TC-012) | Cinq cas : aucune demande et Validé acceptés ; En cours, Retard, Révision refusés, avec vérification que la demande existante n'a pas changé |
| Champs obligatoires | Un cas générique (TC-015, début visible) | Un cas par champ, avec « aucune demande créée » |
| Millésime en Renouvellement | Valeur par défaut (TC-009) et plage de -20 à +10 ans (TC-010) | Même couverture, découpée en quatre vérifications (bornes et valeurs juste au-delà) |
| Reprise | « Oui » (TC-013) et « Non » (TC-014) : même résultat écrit | Affichage de Reprise vérifié ; son effet n'est pas décrit par l'US, donc pas inventé |
| Point ambigu de l'US (§3, entité inconnue) | TC-011 teste « seule une sélection est possible » ; sa liste UI prévoit l'erreur « Entité ID inconnue » sans relever l'écart | Repéré, posé au PO en question bloquante |
| Ce que l'US ne dit pas | Aucune question : son format n'a pas de place pour ça | Neuf questions, dont deux bloquantes : entité inconnue, liste des documents obligatoires |
| Documents obligatoires, règles liées à la nature (§4) | Absents | Questions au PO |
| Résultat de la création | « la demande est créée et redirigée vers le formulaire » | Création, message de confirmation (texte à compléter) et redirection |

Ce que l'agent actuel fait bien, et qui est gardé : l'absence de Reprise en Renouvellement (TC-005), la valeur par défaut concrète « Jean Dupont » (TC-007), l'ouverture du panneau (TC-004), la recherche d'un collaborateur (TC-008). Sur les sections 1 à 3, sa couverture est proche de la nôtre ; il teste même l'interdiction de saisie libre de l'entité (TC-011), que nous laissons en question (Q6).

La différence se joue sur trois points :
1. Exécutabilité : ses cas ne disent ni qui se connecte, ni quelles données préparer.
2. La règle métier de la validation : le statut de l'entité, qui décide si la création est acceptée ou refusée. Il en couvre un cas sur cinq.
3. L'honnêteté face à l'US : il ne signale ni le point ambigu sur l'entité inconnue, ni ce qui manque (documents, messages).

En volume : environ 15 cas pour l'agent actuel, 23 lignes exécutables pour notre version (11 scénarios, dont 6 plans). Il y a plus de lignes, mais aucune en double : chacune a une raison écrite dans la colonne « cas ».
