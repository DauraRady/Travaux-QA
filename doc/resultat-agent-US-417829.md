# US-417829 : Créer une nouvelle demande

Analyse du 20/10/2026. Projet : InfoCAC. Verdict : Partiellement prête.

## 1. Sources

| Source | État |
|---|---|
| US 417829, export `docs/projets/infocac/sources/US-417829.md` | Lue en entier. Pas de section « critères d'acceptation » : les étapes §1 à §5 du flow servent de référence (citées « US §n »). |
| Commentaires de l'US (4) | Non exportés, non lus. Ils peuvent contenir des décisions du PO (rang 2). |
| Maquettes Figma (lien dans l'US) | Non exportées, non lues. |
| US 424139 (comportement des dates) | Non fournie. |
| `CONTEXTE.md` InfoCAC, version 0.1, mise à jour 20/10/2026 | Lu en entier. Presque vide : section 0 (URL, projet, plan 429041) et section 3 (noms des rôles User, Admin, SuperAdmin) seulement. Sections 1, 2, 4 à 9 non remplies. |

Aucune donnée client ou personnelle réelle dans l'US. Aucune entrée suspecte.

## 2. Règles

| ID | Règle (reformulation fidèle) | Source | Statut | Question si À arbitrer |
|---|---|---|---|---|
| R1 | Sur l'écran « Liste des demandes », le bouton « Nouvelle demande » est visible uniquement pour les rôles Admin et SuperAdmin. | US §1 | Rédigeable | |
| R2 | Le clic sur « Nouvelle demande » ouvre un panneau latéral à droite avec le formulaire de création. Le reste de l'écran reste visible en arrière-plan. | US §2 | Rédigeable | |
| R3 | Le champ « Nature du mandat » propose deux valeurs, Renouvellement et Nouveau. Le formulaire s'adapte à la valeur choisie. | US §3 | Rédigeable | |
| R4 | Nature = Renouvellement : le formulaire affiche Entité ID, N° Requête BSC, Affectée à, Millésime. | US §3 Parcours 1 | Rédigeable | |
| R5 | Nature = Nouveau : le formulaire affiche Entité ID, Reprise (Oui, Non), N° Requête BSC, Affectée à, Millésime. | US §3 Parcours 2 | Rédigeable | |
| R6 | Entité ID : les valeurs viennent des données d'InfoCAC (pour Nouveau : InfoCAC ou référentiel). L'utilisateur ne peut pas saisir librement un code. | US §3 | Rédigeable | |
| R7 | Nature = Nouveau, validation avec une entité ID : le champ est surligné en rouge, son titre est en rouge, le message « entité ID inconnue » s'affiche sous le champ. | US §3 Parcours 2 | À arbitrer | Q1 |
| R8 | N° Requête BSC est un champ libre. | US §3 | Rédigeable | |
| R9 | Affectée à : valeur par défaut = nom du compte utilisateur connecté. | US §3 | Rédigeable | |
| R10 | Affectée à : l'utilisateur peut saisir un nom prénom connu des collaborateurs KPMG. | US §3 | Rédigeable | |
| R11 | Affectée à : cas d'un nom prénom non connu des collaborateurs KPMG. | US §3 | À arbitrer | Q5 |
| R12 | Nature = Renouvellement : Millésime s'ouvre par défaut sur l'année fiscale en cours. La liste va de -20 ans à +10 ans. | US §3 Parcours 1 | Rédigeable | |
| R13 | Nature = Nouveau : Millésime s'ouvre par défaut sur l'année fiscale en cours. | US §3 Parcours 2 | Rédigeable | |
| R14 | Nature = Nouveau : le comportement sur les dates du Millésime est renvoyé à l'US 424139. | US §3 Parcours 2 | À arbitrer | Q4 |
| R15 | Tous les champs du formulaire sont obligatoires (dans les deux parcours). Le système vérifie les champs obligatoires à la validation. | US §3, §4 | Rédigeable | |
| R16 | À la validation, le système vérifie « les règles métier liées à la nature du mandat ». | US §4 | À arbitrer | Q3 |
| R17 | À la validation, le système vérifie « la présence des documents obligatoires ». | US §4 | À arbitrer | Q2 |
| R18 | Une demande peut être créée pour une entité ID sans statut ou au statut validé. Création en erreur si l'entité ID a déjà une demande au statut en cours, retard ou révision. | US §4 | Rédigeable | |
| R19 | Après le clic sur « Valider la création », un message de confirmation ou d'erreur apparaît (cf maquettes). | US §4 | Rédigeable | |
| R20 | Si les contrôles sont conformes, la demande est créée et l'utilisateur est redirigé vers la page du formulaire. | US §5 | Rédigeable | |

Détails non bloquants pour les règles Rédigeables (voir section 4) : texte et emplacement des messages (R15, R18, R19), mécanisme de choix de l'Entité ID (R6), format du N° Requête BSC (R8), définition de l'année fiscale en cours (R12, R13), nom de la « page du formulaire » (R20).

## 3. Préconditions et combinaisons

Préconditions

| Précondition | Valeur | Source |
|---|---|---|
| Rôle et compte connectés | Admin ou SuperAdmin. Compte fictif non défini : contexte §4 vide. | US « En tant que », contexte §3 |
| Rôle sans accès (cas R1) | User | Contexte §3 |
| Environnement | Non défini (contexte §0 contient des champs à compléter) | Contexte §0 |
| Écran de départ | « Liste des demandes » | US §1 |
| Données existantes | Une entité fictive pour chaque cas de la table ci-dessous. Aucune donnée de test dans le contexte §8. | US §4, contexte §8 |
| Compte connecté | Un nom connu, pour vérifier la valeur par défaut de « Affectée à » | US §3 |

Combinaisons

| Conditions | Résultat attendu | Source | Statut |
|---|---|---|---|
| Admin, écran Liste des demandes | Bouton « Nouvelle demande » visible | US §1 | Rédigeable |
| SuperAdmin, écran Liste des demandes | Bouton « Nouvelle demande » visible | US §1 | Rédigeable |
| User, écran Liste des demandes (filtrage mixte avec les deux lignes précédentes) | Bouton « Nouvelle demande » non visible | US §1 « uniquement » | Rédigeable |
| Nature = Renouvellement | Champs : Entité ID, N° Requête BSC, Affectée à, Millésime | US §3 | Rédigeable |
| Nature = Nouveau | Mêmes champs, plus Reprise (Oui, Non) | US §3 | Rédigeable |
| Entité ID sans statut | Création possible | US §4 | Rédigeable |
| Entité ID au statut validé | Création possible | US §4 | Rédigeable |
| Entité ID avec une demande au statut en cours | Création en erreur | US §4 | Rédigeable |
| Entité ID avec une demande au statut retard | Création en erreur | US §4 | Rédigeable |
| Entité ID avec une demande au statut révision | Création en erreur | US §4 | Rédigeable |
| Entité ID avec un autre statut que les quatre cités | Non écrit | US §4 | À arbitrer (Q6) |
| Entité ID avec plusieurs demandes de statuts différents (ex. une validée, une en cours) | Non écrit | US §4 | À arbitrer (Q6) |
| Entité ID inconnue, Nature = Nouveau | Voir R7 | US §3 | À arbitrer (Q1) |
| Entité ID inconnue, Nature = Renouvellement | Non écrit | US §3 | À arbitrer (Q1) |

La règle R18 est écrite à l'étape de validation, sans distinction de nature : elle est appliquée aux deux parcours.

Quand la création est en erreur (R18, R15), la partie Rédigeable est : l'action est refusée, rien n'est créé, un message d'erreur s'affiche.

Limites

| Élément | Borne Rédigeable | Au-delà |
|---|---|---|
| Millésime, Nature = Renouvellement | -20 ans et +10 ans (la référence des écarts n'est pas écrite, voir Q7) | Non écrit : aucun scénario |

## 4. Questions au PO

Bloquantes (la règle concernée n'aura aucun scénario tant qu'elles restent ouvertes)

| # | Règle | Ce qui manque | Question |
|---|---|---|---|
| Q1 | R7, R6 | L'US dit que l'utilisateur ne peut pas saisir librement une entité ID, mais décrit une erreur « entité ID inconnue ». La phrase ne précise pas la condition (« valide la création avec une entité ID » sans qualificatif). Rien n'est écrit pour Renouvellement. | Comment l'utilisateur peut-il valider avec une entité ID inconnue ? Dans quel cas exact l'erreur s'affiche-t-elle ? Cette erreur vaut-elle aussi pour Renouvellement ? Bloque-t-elle la création ? |
| Q2 | R17 | Aucun document n'est cité ailleurs dans l'US et le formulaire ne contient aucun champ de dépôt. | Quels sont les documents obligatoires, où l'utilisateur les ajoute-t-il, et que se passe-t-il quand ils manquent ? |
| Q3 | R16 | Les « règles métier liées à la nature du mandat » ne sont pas listées. | Quelles sont ces règles, et que se passe-t-il quand l'une d'elles n'est pas respectée ? Ou désignent-elles seulement les champs différents entre Renouvellement et Nouveau (R4, R5) ? |
| Q4 | R14 | Renvoi vers l'US 424139, non fournie. | Quel est le comportement du Millésime (liste, bornes, dates) pour Nature = Nouveau ? |
| Q5 | R11 | La branche « nom non connu » n'est pas écrite. | Que se passe-t-il quand l'utilisateur saisit dans « Affectée à » un nom prénom non connu des collaborateurs KPMG ? |
| Q6 | R18 | Seuls quatre statuts sont cités. Le contexte ne définit aucun statut. | Existe-t-il d'autres statuts d'entité ou de demande ? Que donne le cas d'une entité ayant plusieurs demandes de statuts différents ? Le « statut » est-il celui de l'entité ou celui de la demande ? |

Non bloquantes (détails qui n'empêchent pas la rédaction)

| # | Règle | Question |
|---|---|---|
| Q7 | R12, R13 | Que signifie « année fiscale en cours » (dates) ? Les -20 et +10 ans se comptent-ils à partir de cette année, bornes incluses ? |
| Q8 | R15, R18, R19 | Texte exact et emplacement des messages de confirmation et d'erreur (champ vide, entité déjà en demande en cours, retard ou révision). |
| Q9 | R3, R5, R15 | Nature du mandat est-elle obligatoire ? Que contient le formulaire avant son choix ? Quelle est la valeur par défaut de Reprise ? Millésime peut-il être vidé ? |
| Q10 | R6 | Comment l'entité ID est-elle choisie (liste, recherche) ? Que désigne « le référentiel » pour Nouveau ? |
| Q11 | R8 | Quel format, quelle longueur pour le N° Requête BSC ? |
| Q12 | R20 | Quel écran est « la page du formulaire » ? Quel est le statut initial de la demande créée ? |

Écarts avec le contexte projet : Aucun. Le contexte est presque vide : aucune règle n'est contredite.

Idées exploratoires (hors promesse de l'US, aucun scénario)

1. R1 : un utilisateur sans le rôle Admin ou SuperAdmin accède au formulaire par un autre chemin que le bouton (lien direct). L'US ne parle que de la visibilité du bouton.
2. R3 : changer la Nature du mandat après avoir rempli des champs. Les valeurs saisies sont-elles conservées ou effacées ? L'US ne le dit pas.
3. R2 : fermer le panneau sans valider, puis le rouvrir. L'US ne cite aucun moyen de fermeture.

Risques (rattachés aux règles)

1. R1 : bouton visible pour un rôle non autorisé.
2. R18 : demande créée pour une entité déjà en cours, retard ou révision.
3. R7 et R6 : comportement incohérent sur l'entité ID inconnue.

## 5. Verdict

Partiellement prête : l'accès, le panneau, les champs de chaque nature, les champs obligatoires, la règle sur les statuts d'entité et la création avec redirection sont Rédigeables ; l'entité inconnue, les documents obligatoires, les règles liées à la nature, le Millésime de Nouveau et le nom non connu attendent des réponses.

## 6. Propositions pour le contexte

Rien n'est écrit dans le contexte : `/maj-contexte` le fera après validation.

| # | Proposition (une ligne) | Section du contexte | Type | Source |
|---|---|---|---|---|
| 1 | Admin et SuperAdmin voient le bouton « Nouvelle demande » sur la Liste des demandes ; les autres rôles (User) ne le voient pas. | 3 | ajout | US 417829 §1 |
| 2 | Écran « Liste des demandes » : bouton « Nouvelle demande » qui ouvre un panneau latéral de création. | 7 | ajout | US 417829 §1, §2 |
| 3 | Objet « Demande » : natures du mandat Renouvellement et Nouveau. | 5 | ajout | US 417829 §3 |
| 4 | Règle de création : possible si l'entité ID n'a pas de statut ou un statut validé ; erreur si une demande est en cours, retard ou révision. | 6 | ajout | US 417829 §4 |
| 5 | Statuts cités par l'US (validé, en cours, retard, révision) : définition et liste complète à confirmer. | 9 | point à confirmer | Q6 |
| 6 | Entité ID inconnue : contradiction entre « pas de saisie libre » et l'erreur « entité ID inconnue ». | 9 | point à confirmer (bloquant) | Q1 |
| 7 | Documents obligatoires à la création d'une demande : lesquels et où. | 9 | point à confirmer (bloquant) | Q2 |
| 8 | Règles métier liées à la nature du mandat : liste absente. | 9 | point à confirmer (bloquant) | Q3 |
| 9 | Millésime pour Nouveau : comportement renvoyé à l'US 424139, non fournie. | 9 | point à confirmer (bloquant) | Q4 |
| 10 | « Année fiscale en cours » : définition. | 9 | point à confirmer | Q7 |
| 11 | Comptes de test pour Admin, SuperAdmin et User : à définir (section 4 vide). | 4 | point à confirmer | Absence dans le contexte |

# Scénarios

Rédigés le 20/10/2026 à partir de l'analyse ci-dessus. Seules les règles Rédigeables ont un scénario. Comptes fictifs `ADM-TEST-01` (Admin), `SADM-TEST-01` (SuperAdmin), `USR-TEST-01` (User) : le contexte §4 est vide, ces identifiants sont à confirmer (proposition 11).

## 1. Scénarios

```gherkin
Fonctionnalité: Accéder à la création d'une demande

  Plan du scénario: Visibilité du bouton "Nouvelle demande" selon le rôle
    Étant donné que l'utilisateur "<compte>" est connecté avec le rôle "<role>"
    Quand il ouvre la page "Liste des demandes"
    Alors la "Liste des demandes" s'affiche
    Et le bouton "Nouvelle demande" est <presence>

    Exemples:
      | cas               | compte       | role       | presence |
      | rôle autorisé     | ADM-TEST-01  | Admin      | affiché  |
      | rôle autorisé     | SADM-TEST-01 | SuperAdmin | affiché  |
      | rôle non autorisé | USR-TEST-01  | User       | absent   |

  Scénario: Le panneau de création s'ouvre à droite de la liste
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et qu'il est sur la page "Liste des demandes"
    Quand il clique sur "Nouvelle demande"
    Alors un panneau latéral s'ouvre sur la droite de l'écran
    Et le formulaire de création d'une demande est affiché dans le panneau
    Et la "Liste des demandes" reste visible en arrière-plan
```

```gherkin
Fonctionnalité: Renseigner le formulaire de création selon la nature du mandat

  Contexte:
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et qu'il est sur la page "Liste des demandes"
    Et que le panneau de création est ouvert

  Scénario: Le champ "Nature du mandat" propose deux valeurs
    Quand il ouvre la liste du champ "Nature du mandat"
    Alors la liste propose exactement les valeurs "Renouvellement" et "Nouveau"

  Scénario: La nature "Renouvellement" affiche ses quatre champs
    Quand il sélectionne la nature "Renouvellement"
    Alors le formulaire affiche les champs "Entité ID", "N° Requête BSC", "Affectée à" et "Millésime"

  Scénario: La nature "Nouveau" affiche aussi le champ "Reprise"
    Quand il sélectionne la nature "Nouveau"
    Alors le formulaire affiche les champs "Entité ID", "Reprise", "N° Requête BSC", "Affectée à" et "Millésime"
    Et le champ "Reprise" propose les valeurs "Oui" et "Non"

  Scénario: Le code de l'entité ID ne se saisit pas librement
    Étant donné que le code "ENT-LIBRE-99" n'existe pas dans InfoCAC
    Quand il sélectionne la nature "Renouvellement"
    Et qu'il tente de saisir "ENT-LIBRE-99" dans le champ "Entité ID"
    Alors le champ "Entité ID" ne contient pas "ENT-LIBRE-99"

  Scénario: "Affectée à" propose par défaut le nom du compte connecté
    Quand il sélectionne la nature "Renouvellement"
    Alors le champ "Affectée à" affiche le nom du compte "ADM-TEST-01"

  Scénario: "Affectée à" accepte le nom prénom d'un collaborateur KPMG
    Étant donné que le collaborateur "COL-TEST-01" est connu des collaborateurs KPMG
    Quand il sélectionne la nature "Renouvellement"
    Et qu'il saisit le nom prénom de "COL-TEST-01" dans le champ "Affectée à"
    Alors le champ "Affectée à" affiche le nom prénom de "COL-TEST-01"
    Et le champ "Affectée à" n'est pas en erreur

  Plan du scénario: Le millésime s'ouvre sur l'année fiscale en cours
    Quand il sélectionne la nature "<nature>"
    Alors le champ "Millésime" affiche l'année fiscale en cours

    Exemples:
      | cas        | nature         |
      | parcours 1 | Renouvellement |
      | parcours 2 | Nouveau        |

  Plan du scénario: Les bornes du millésime proposées pour un renouvellement
    Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"
    Quand il ouvre la liste du champ "Millésime"
    Alors le millésime "<millesime>" est proposé dans la liste

    Exemples:
      | cas         | millesime                   |
      | borne basse | année en cours moins 20 ans |
      | borne haute | année en cours plus 10 ans  |
```

```gherkin
Fonctionnalité: Valider la création d'une demande

  Contexte:
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et qu'il est sur la page "Liste des demandes"

  Plan du scénario: Création d'une demande de renouvellement pour une entité ID autorisée
    Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"
    Et que l'entité ID "<entite>" <situation>
    Quand il sélectionne l'entité ID "<entite>"
    Et qu'il renseigne le N° Requête BSC "BSC-TEST-01"
    Et qu'il laisse "Affectée à" et "Millésime" à leur valeur par défaut
    Et qu'il clique sur "Valider la création"
    Alors un message de confirmation s'affiche
    Et une demande pour l'entité ID "<entite>" est créée
    Et l'utilisateur est redirigé vers la page du formulaire

    Exemples:
      | cas                     | entite      | situation                        |
      | entité sans statut      | ENT-TEST-01 | n'a pas encore de statut         |
      | entité au statut validé | ENT-TEST-02 | a une demande au statut "validé" |

  Scénario: Création d'une demande pour un nouveau mandat
    Étant donné que le panneau de création est ouvert avec la nature "Nouveau"
    Et que l'entité ID "ENT-TEST-03" n'a pas encore de statut
    Quand il sélectionne l'entité ID "ENT-TEST-03"
    Et qu'il choisit la reprise "Non"
    Et qu'il renseigne le N° Requête BSC "BSC-TEST-02"
    Et qu'il laisse "Affectée à" et "Millésime" à leur valeur par défaut
    Et qu'il clique sur "Valider la création"
    Alors un message de confirmation s'affiche
    Et une demande pour l'entité ID "ENT-TEST-03" est créée
    Et l'utilisateur est redirigé vers la page du formulaire

  Plan du scénario: Une demande déjà en cours, en retard ou en révision bloque la création
    Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"
    Et que l'entité ID "<entite>" a déjà une demande au statut "<statut>"
    Quand il sélectionne l'entité ID "<entite>"
    Et qu'il renseigne le N° Requête BSC "BSC-TEST-03"
    Et qu'il laisse "Affectée à" et "Millésime" à leur valeur par défaut
    Et qu'il clique sur "Valider la création"
    Alors un message d'erreur s'affiche
    Et aucune nouvelle demande pour l'entité ID "<entite>" n'apparaît dans la "Liste des demandes"
    Et la demande existante de l'entité ID "<entite>" est toujours au statut "<statut>"

    Exemples:
      | cas             | entite      | statut   |
      | statut en cours | ENT-TEST-04 | en cours |
      | statut retard   | ENT-TEST-05 | retard   |
      | statut révision | ENT-TEST-06 | révision |

  Plan du scénario: Un champ obligatoire vide bloque la création
    Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"
    Et que l'entité ID "ENT-TEST-01" n'a pas encore de statut
    Quand il renseigne tous les champs obligatoires sauf le champ "<champ>" laissé vide
    Et qu'il clique sur "Valider la création"
    Alors un message d'erreur s'affiche
    Et aucune nouvelle demande n'apparaît dans la "Liste des demandes"

    Exemples:
      | cas                      | champ          |
      | entité ID non renseignée | Entité ID      |
      | N° BSC non renseigné     | N° Requête BSC |
```

## 2. Couverture

| Critère | Scénarios | Couvert ? |
|---|---|---|
| R1 Bouton visible uniquement pour Admin et SuperAdmin | Visibilité du bouton selon le rôle (3 lignes) | Couvert |
| R2 Panneau latéral à droite, écran visible en arrière-plan | Le panneau de création s'ouvre à droite de la liste | Couvert |
| R3 Deux valeurs de nature | Le champ "Nature du mandat" propose deux valeurs | Couvert. Obligatoire ou non, contenu avant choix : Q9 |
| R4 Champs de Renouvellement | La nature "Renouvellement" affiche ses quatre champs | Couvert |
| R5 Champs de Nouveau | La nature "Nouveau" affiche aussi le champ "Reprise" | Couvert. Valeur par défaut de Reprise : Q9 |
| R6 Pas de saisie libre de l'entité ID | Le code de l'entité ID ne se saisit pas librement | Partiel. Testé en Renouvellement seulement, mécanisme de choix (Q10) et lien avec Q1 non tranchés |
| R8 N° Requête BSC libre | Valeur "BSC-TEST-01" utilisée dans les scénarios de création | Partiel. Pas de scénario dédié, format inconnu (Q11) |
| R9 Valeur par défaut de "Affectée à" | "Affectée à" propose par défaut le nom du compte connecté | Couvert |
| R10 Saisie d'un nom prénom connu | "Affectée à" accepte le nom prénom d'un collaborateur KPMG | Couvert |
| R12 Millésime Renouvellement : défaut et bornes | Le millésime s'ouvre sur l'année fiscale en cours (parcours 1), Les bornes du millésime | Partiel. Référence des écarts et année fiscale non définies (Q7). Aucun scénario au-delà des bornes : non écrit |
| R13 Millésime Nouveau : défaut | Le millésime s'ouvre sur l'année fiscale en cours (parcours 2) | Partiel. Comportement sur les dates : Q4 |
| R15 Champs obligatoires | Un champ obligatoire vide bloque la création | Partiel. Seuls "Entité ID" et "N° Requête BSC" sont testés : "Affectée à" et "Millésime" ont une valeur par défaut, "Reprise" n'a pas de défaut connu (Q9). Texte du message : Q8 |
| R18 Statuts autorisés et refusés | Création pour une entité ID autorisée, Création pour un nouveau mandat, Une demande déjà en cours, en retard ou en révision | Couvert pour les quatre statuts cités. Refus testé en Renouvellement seulement. Autres statuts et demandes multiples : Q6. Texte du message : Q8 |
| R19 Message de confirmation ou d'erreur | Scénarios de création et de refus | Partiel. Texte et emplacement : Q8 |
| R20 Création et redirection | Création pour une entité ID autorisée, Création pour un nouveau mandat | Partiel. Nom de « la page du formulaire » et statut initial : Q12 |

## 3. Non rédigé

| Règle | Raison |
|---|---|
| R7 Erreur « entité ID inconnue » (Nouveau) | À arbitrer, Q1 |
| R11 Nom prénom non connu des collaborateurs KPMG | À arbitrer, Q5 |
| R14 Dates du Millésime pour Nouveau | À arbitrer, Q4 |
| R16 Règles métier liées à la nature du mandat | À arbitrer, Q3 |
| R17 Documents obligatoires | À arbitrer, Q2 |
| Entité ID inconnue en Renouvellement ; statut autre que les quatre cités ; entité à plusieurs demandes | À arbitrer, Q1 et Q6 |
| Accès au formulaire par lien direct ; changement de nature après saisie ; fermeture du panneau | Exploratoire, aucun scénario |
