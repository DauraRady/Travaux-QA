# US-417829 : Créer une nouvelle demande

Analyse du 27/10/2026. Projet : InfoCAC.

## 1. Sources

| Source | État |
|---|---|
| US 417829 (export `docs/projets/infocac/sources/US-417829.md`) | Lue. Les critères d'acceptation ne sont pas numérotés : la description est découpée par section (§1 à §5). |
| Commentaires de l'US | 4 commentaires, non exportés, non lus. Ils peuvent contenir des décisions du PO (rang 2). |
| Contexte projet InfoCAC (mis à jour le 27/10/2026, v0.1) | Lu en entier. Presque vide : seuls la section 0 (Azure DevOps) et les noms des rôles User, Admin, SuperAdmin (section 3, droits « à compléter ») sont renseignés. Sections 4, 5, 7, 8, 9, 10 et 11 sans contenu utile. |
| Maquettes Figma | Citées par l'US, non exportées, non lues. |
| US 424139 (comportement des dates du millésime) | Citée par l'US, non fournie. |

Aucune donnée client réelle. Aucune consigne adressée à une IA dans l'US.

## 2. Règles

| ID | Règle (reformulation fidèle) | Source | Statut |
|---|---|---|---|
| R1 | Le bouton « Nouvelle demande » de l'écran « Liste des demandes » est visible uniquement pour les rôles Admin et SuperAdmin. | US §1 | Rédigeable |
| R2 | Un clic sur « Nouvelle demande » ouvre un panneau latéral à droite de l'écran, avec le formulaire de création. Le reste de l'écran reste visible en arrière-plan. | US Flow, §2 | Rédigeable |
| R3 | Le champ « Nature du mandat » propose deux valeurs, Renouvellement et Nouveau. Le formulaire s'adapte à la valeur choisie. | US Flow, §3 | Rédigeable |
| R4 | Nature Renouvellement : le formulaire affiche Entité ID, N° Requête BSC, Affectée à, Millésime. Tous les champs sont obligatoires. | US §3 Parcours 1 | Rédigeable |
| R5 | Nature Nouveau : le formulaire affiche Entité ID, Reprise (Oui, Non), N° Requête BSC, Affectée à, Millésime. Tous les champs sont obligatoires. | US §3 Parcours 2 | Rédigeable |
| R6 | Entité ID : valeur issue des données d'InfoCAC (Renouvellement) ou d'InfoCAC ou du référentiel (Nouveau). L'utilisateur ne peut pas saisir librement un code. | US §3 | Rédigeable (absence de saisie libre) |
| R7 | Parcours Nouveau : « si l'utilisateur valide la création avec une entité ID alors » le champ est surligné en rouge, son titre est en rouge et le message « entité ID inconnue » s'affiche sous le champ. | US §3 Parcours 2 | À arbitrer |
| R8 | N° Requête BSC : saisie libre. | US §3 | Rédigeable |
| R9 | Affectée à : la valeur par défaut est le nom du compte connecté. | US §3 | Rédigeable |
| R10 | Affectée à : on peut saisir un nom prénom connu des collaborateurs KPMG. | US §3 | Rédigeable (nom connu) |
| R11 | Affectée à : comportement avec un nom prénom non connu des collaborateurs KPMG. | Non écrit | À arbitrer |
| R12 | Renouvellement, Millésime : ouverture par défaut sur l'année fiscale en cours, liste déroulante de -20 ans à +10 ans. | US §3 Parcours 1 | Rédigeable |
| R13 | Nouveau, Millésime : ouverture par défaut sur l'année fiscale en cours. | US §3 Parcours 2 | Rédigeable |
| R14 | Nouveau, Millésime : valeurs proposées, bornes et comportement sur les dates, renvoyés à l'US 424139. | US §3 Parcours 2 | À arbitrer |
| R15 | Un clic sur « Valider la création » fait vérifier les champs obligatoires. Un champ obligatoire vide bloque la validation. | US §4 | Rédigeable |
| R16 | La validation vérifie « les règles métier liées à la nature du mandat qui va influer sur le type de formulaire ». | US §4 | À arbitrer |
| R17 | La validation vérifie « la présence des documents obligatoires ». | US §4 | À arbitrer |
| R18 | La création est possible avec une entité ID sans statut ou avec une demande au statut validé. | US §4 | Rédigeable |
| R19 | Erreur si l'entité ID a déjà une demande au statut en cours, retard ou révision : la création est refusée, rien n'est créé, un message d'erreur s'affiche. | US §4 | Rédigeable |
| R20 | Entité ID dont la demande a un statut autre que validé, en cours, retard ou révision. | Non écrit | À arbitrer |
| R21 | Après la validation, un message de confirmation ou d'erreur apparaît (cf maquettes). | US §4 | Rédigeable |
| R22 | Si les contrôles sont conformes, la demande est créée. | US §5 | Rédigeable |
| R23 | Après la création, redirection vers la page du formulaire. | US §5 | Rédigeable |

## 3. Préconditions et combinaisons

Préconditions

| Précondition | Valeur | Source |
|---|---|---|
| Rôle et compte connectés | Admin, puis SuperAdmin. Compte fictif de type `ADM-TEST-01` ; aucun compte Admin ni SuperAdmin n'est défini au contexte §4 | US « En tant que », contexte §3 et §4 |
| Rôle non autorisé | User (rôle cité au contexte §3, droits non décrits) | Contexte §3, US §1 (« uniquement ») |
| Écran de départ | « Liste des demandes » | US §1 |
| Données existantes | Une entité sans statut ; une entité dont la demande est validée ; une entité avec une demande en cours ; une en retard ; une en révision. Identifiants fictifs de type `ENT-TEST-01`, à créer ou à désigner (contexte §8 vide) | US §4 |
| Nom du compte connecté | Un compte dont le nom est connu, pour vérifier la valeur par défaut de « Affectée à » | US §3 |

Combinaisons

| Conditions | Résultat attendu | Source | Statut |
|---|---|---|---|
| Admin, écran « Liste des demandes » | Bouton « Nouvelle demande » visible | US §1 | Rédigeable |
| SuperAdmin, écran « Liste des demandes » | Bouton « Nouvelle demande » visible | US §1 | Rédigeable |
| User, écran « Liste des demandes » (filtrage mixte avec les deux lignes précédentes) | Bouton « Nouvelle demande » non visible | US §1 (« uniquement ») | Rédigeable |
| Nature Renouvellement | Champs Entité ID, N° Requête BSC, Affectée à, Millésime ; pas de champ Reprise | US §3 | Rédigeable |
| Nature Nouveau | Champs Entité ID, Reprise, N° Requête BSC, Affectée à, Millésime | US §3 | Rédigeable |
| Renouvellement ou Nouveau, entité sans statut, champs remplis | Demande créée, redirection vers la page du formulaire | US §4, §5 | Rédigeable, sous réserve de Q3 |
| Renouvellement ou Nouveau, entité avec demande validée | Demande créée | US §4 | Rédigeable, sous réserve de Q3 |
| Renouvellement ou Nouveau, entité avec demande en cours, en retard ou en révision | Création refusée, rien créé, message d'erreur (même résultat pour les trois statuts) | US §4 | Rédigeable |
| Renouvellement ou Nouveau, un champ obligatoire vide | Validation bloquée | US §3, §4 | Rédigeable |
| Nouveau, Reprise = Oui, puis Reprise = Non | Les deux valeurs sont proposées ; effet de chacune sur la création non écrit | US §3 | Rédigeable pour l'affichage seulement |
| Nouveau, entité inconnue | Surlignage rouge, titre rouge, message « entité ID inconnue » | US §3 | À arbitrer (Q1) |
| Renouvellement, entité inconnue | Non écrit | Aucune | À arbitrer (Q1) |
| Entité dont la demande a un autre statut | Non écrit | Aucune | À arbitrer (Q6) |

Limites

| Règle | Borne | Juste au-delà |
|---|---|---|
| R12 | Année fiscale en cours -20 ans ; année fiscale en cours +10 ans | Non écrit (liste déroulante : on ne sait pas si des valeurs hors plage sont refusées ou absentes) |
| R14 | Non écrites | Non écrit |

Variations et flux du contexte (sections 10 et 11) : Aucun. Les sections sont vides.

Risques

1. R7 et R6 : la règle de l'entité inconnue contredit l'absence de saisie libre.
2. R18, R19 et R20 : le blocage dépend du statut de la dernière demande de l'entité ; les statuts ne sont pas définis au contexte.
3. R17 : les documents obligatoires peuvent empêcher la création nominale.

## 4. Questions au PO

| # | Règle | Ce qui manque | Question | Bloquante ? |
|---|---|---|---|---|
| Q1 | R7, R6 | La condition de l'erreur est tronquée (« avec une entité ID alors »), et l'entité ne peut pas être saisie librement. Rien n'est écrit pour le parcours Renouvellement. | Dans quel cas précis l'erreur « entité ID inconnue » s'affiche-t-elle : entité vide, entité non sélectionnée dans la liste, autre ? Comment l'utilisateur peut-il choisir une entité inconnue alors que la saisie libre est impossible ? Le même contrôle s'applique-t-il au parcours Renouvellement ? Le champ en erreur bloque-t-il la création ? | Bloquante |
| Q2 | R17 | La liste des documents obligatoires est absente ; le formulaire décrit ne contient aucun champ de document. | Quels sont les documents obligatoires, pour quelle nature de mandat, et où l'utilisateur les ajoute-t-il ? Que se passe-t-il s'il en manque ? | Bloquante |
| Q3 | R17, R22 | Conséquence de Q2 sur la création nominale. | La création réussie (entité sans statut, tous les champs remplis) demande-t-elle un document ? | Bloquante |
| Q4 | R14 | Le comportement du millésime pour Nouveau est renvoyé à l'US 424139, non fournie. | Quelles valeurs, bornes et règles de dates s'appliquent au millésime du parcours Nouveau ? Peut-on fournir l'US 424139 ? | Bloquante pour R14 seulement |
| Q5 | R16 | « Les règles métier liées à la nature du mandat » ne sont pas listées. | Quelles règles métier, en plus des champs affichés par nature, sont vérifiées à la validation ? | Non bloquante |
| Q6 | R20 | Seuls les statuts validé, en cours, retard et révision sont cités. Le contexte §5 ne définit aucun statut. | Quels statuts une demande peut-elle avoir ? Que se passe-t-il à la validation pour un statut non cité ? Quels sont les libellés exacts affichés ? | Non bloquante |
| Q7 | R11 | La branche « nom non connu » est absente. | Que se passe-t-il quand on saisit un nom prénom inconnu des collaborateurs KPMG ? Comment la saisie se fait-elle (liste de suggestions, champ libre) ? | Non bloquante |
| Q8 | R3 | La liste des champs obligatoires ne cite pas « Nature du mandat ». | Nature du mandat est-elle obligatoire ? A-t-elle une valeur par défaut ou est-elle vide à l'ouverture du panneau ? | Non bloquante |
| Q9 | R6 | Le mode de choix de l'entité (liste, recherche) et la définition du « référentiel » ne sont pas écrits. | Comment l'utilisateur choisit-il l'entité ID ? Qu'est-ce que le « référentiel » par rapport à InfoCAC ? | Non bloquante |
| Q10 | R15, R19, R21 | Textes et emplacements non exportés (maquettes). | Quels sont le texte et l'emplacement des messages de confirmation, d'erreur de champ obligatoire et d'erreur de demande existante ? | Non bloquante |
| Q11 | R22, R23 | Statut initial de la demande créée et nom de « la page du formulaire » non écrits. | Quel est le statut de la demande à sa création ? Quel est le nom de l'écran affiché après la redirection ? | Non bloquante |
| Q12 | R12, R13 | « Année fiscale en cours » n'est pas définie. | Comment l'année fiscale en cours est-elle déterminée (dates de début et de fin) ? Les bornes -20 et +10 sont-elles incluses ? | Non bloquante |
| Q13 | R8, R9 | Pas de limite de longueur ni de format pour N° Requête BSC. Pas de compte de test Admin ni SuperAdmin dans le contexte. | Existe-t-il une limite pour N° Requête BSC ? Quels comptes de test Admin et SuperAdmin utiliser ? | Non bloquante |
| Q14 | Commentaires | 4 commentaires non lus. | Peut-on fournir les commentaires de l'US ? Une décision du PO peut répondre à certaines questions ci-dessus. | Non bloquante |

Écarts avec le contexte projet : Aucun écart. Le contexte est trop peu renseigné pour contredire l'US.

Idées exploratoires (hors de ce que l'US promet)

1. Changer la nature du mandat après avoir rempli des champs : les valeurs saisies sont-elles conservées ou perdues ?
2. Fermer le panneau sans valider : aucun comportement décrit.
3. Entité ayant plusieurs demandes (par exemple une validée et une en cours) : le blocage s'applique-t-il ?

## 5. Verdict

Partiellement prête : l'accès au bouton, le panneau, les champs par nature, le contrôle des champs obligatoires et le blocage selon le statut de l'entité sont décrits et rédigeables ; l'entité inconnue (R7), les documents obligatoires (R17) et le millésime du parcours Nouveau (R14) attendent des réponses.

Les scénarios de création réussie restent rédigeables à partir de l'US mais dépendent de la réponse à Q3.

## 6. Propositions pour le contexte

| # | Proposition (une ligne) | Section du contexte | Type | Source |
|---|---|---|---|---|
| 1 | Admin et SuperAdmin voient le bouton « Nouvelle demande » dans la liste des demandes ; les autres rôles ne le voient pas | 3 | ajout | US 417829 §1 (R1) |
| 2 | Écran « Liste des demandes » : bouton « Nouvelle demande » qui ouvre un panneau latéral de création | 7 | ajout | US 417829 §1, §2 (R1, R2) |
| 3 | Objet Demande, variantes de la nature du mandat : Renouvellement et Nouveau | 5 | ajout | US 417829 §3 (R3) |
| 4 | Règle : une demande ne peut pas être créée pour une entité ayant une demande en cours, retard ou révision ; elle l'est si l'entité n'a pas de statut ou un statut validé | 6 | ajout | US 417829 §4 (R18, R19) |
| 5 | Variation par nature du mandat : le champ Reprise (Oui, Non) n'existe que pour Nouveau ; le millésime Renouvellement va de -20 à +10 ans | 10 | ajout | US 417829 §3 (R4, R5, R12) |
| 6 | Statuts cités (validé, en cours, retard, révision) : liste complète, définitions et libellés à confirmer | 9 | point à confirmer | US 417829 §4 (Q6) |
| 7 | Entité ID inconnue : condition de l'erreur et contradiction avec l'absence de saisie libre | 9 | point à confirmer, bloquant | US 417829 §3 (Q1) |
| 8 | Documents obligatoires à la création d'une demande | 9 | point à confirmer, bloquant | US 417829 §4 (Q2, Q3) |
| 9 | Comportement des dates du millésime pour Nouveau (US 424139) | 9 | point à confirmer | US 417829 §3 (Q4) |
| 10 | Comptes de test Admin et SuperAdmin | 4 | point à confirmer | Contexte §4 vide, US 417829 (Q13) |

Rien n'est écrit dans le contexte : /maj-contexte le fera après validation.

---

Rédaction des scénarios du 27/10/2026. Les numéros de règle (R1 à R23) et de question (Q1 à Q14) renvoient à l'analyse ci-dessus.

## 7. Scénarios

### Accès au bouton de création (R1)

```gherkin
Fonctionnalité: Accès à la création d'une demande

  Plan du scénario: Le bouton "Nouvelle demande" n'est affiché que pour les rôles Admin et SuperAdmin
    Étant donné que l'utilisateur "<compte>" est connecté avec le rôle "<role>"
    Quand il ouvre la page "Liste des demandes"
    Alors la "Liste des demandes" s'affiche
    Et le bouton "Nouvelle demande" <affichage>

    Exemples:
      | cas               | compte      | role       | affichage         |
      | rôle autorisé     | ADM-TEST-01 | Admin      | est affiché       |
      | rôle autorisé     | SAD-TEST-01 | SuperAdmin | est affiché       |
      | rôle non autorisé | USR-TEST-01 | User       | n'est pas affiché |
```

### Formulaire de création (R2 à R5, R8 à R10, R12, R13, R15, R18, R19, R21 à R23)

```gherkin
Fonctionnalité: Créer une nouvelle demande depuis la liste des demandes

  Contexte:
    Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
    Et qu'il est sur la page "Liste des demandes"

  Scénario: Le panneau de création s'ouvre à droite de la liste
    # Type : UI
    Quand il clique sur "Nouvelle demande"
    Alors un panneau latéral s'affiche à droite de l'écran
    Et le formulaire de création d'une demande est affiché dans le panneau
    Et la "Liste des demandes" reste visible en arrière-plan

  Scénario: Le champ "Nature du mandat" propose deux valeurs
    Étant donné que le panneau de création est ouvert
    Quand il consulte les valeurs du champ "Nature du mandat"
    Alors le champ "Nature du mandat" propose la valeur "Renouvellement"
    Et le champ "Nature du mandat" propose la valeur "Nouveau"

  Scénario: La nature Renouvellement affiche quatre champs et pas le champ Reprise
    Étant donné que le panneau de création est ouvert
    Quand il sélectionne la nature "Renouvellement"
    Alors le formulaire affiche les champs "Entité ID", "N° Requête BSC", "Affectée à" et "Millésime"
    Mais le champ "Reprise" n'est pas affiché

  Scénario: La nature Nouveau affiche en plus le champ Reprise
    Étant donné que le panneau de création est ouvert
    Quand il sélectionne la nature "Nouveau"
    Alors le formulaire affiche les champs "Entité ID", "Reprise", "N° Requête BSC", "Affectée à" et "Millésime"
    Et le champ "Reprise" propose la valeur "Oui"
    Et le champ "Reprise" propose la valeur "Non"

  Scénario: Le champ "Entité ID" n'accepte pas de code saisi librement
    Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"
    Quand il saisit le code "ENT-LIBRE-99" dans le champ "Entité ID"
    Alors le code "ENT-LIBRE-99" n'est pas retenu comme valeur du champ "Entité ID"

  Scénario: Le champ "N° Requête BSC" accepte une saisie libre
    Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"
    Quand il saisit "BSC-TEST-01" dans le champ "N° Requête BSC"
    Alors le champ "N° Requête BSC" affiche "BSC-TEST-01"

  Plan du scénario: Le champ "Affectée à" propose par défaut le nom du compte connecté
    Étant donné que le nom du compte "ADM-TEST-01" est "Admin Test"
    Quand il clique sur "Nouvelle demande"
    Et qu'il sélectionne la nature "<nature>"
    Alors le champ "Affectée à" affiche "Admin Test"

    Exemples:
      | cas                     | nature         |
      | parcours Renouvellement | Renouvellement |
      | parcours Nouveau        | Nouveau        |

  Scénario: Le champ "Affectée à" accepte le nom d'un collaborateur connu
    Étant donné que le collaborateur "Collaborateur Test" est connu des collaborateurs KPMG
    Et que le panneau de création est ouvert avec la nature "Renouvellement"
    Quand il renseigne "Collaborateur Test" dans le champ "Affectée à"
    Alors le champ "Affectée à" affiche "Collaborateur Test"

  Plan du scénario: Le champ "Millésime" s'ouvre sur l'année fiscale en cours
    Quand il clique sur "Nouvelle demande"
    Et qu'il sélectionne la nature "<nature>"
    Alors le champ "Millésime" affiche l'année fiscale en cours

    Exemples:
      | cas                     | nature         |
      | parcours Renouvellement | Renouvellement |
      | parcours Nouveau        | Nouveau        |

  Plan du scénario: Les bornes de la liste "Millésime" pour un Renouvellement
    Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"
    Quand il ouvre la liste du champ "Millésime"
    Alors le millésime "<millesime>" est proposé dans la liste

    Exemples:
      | cas         | millesime                            |
      | borne basse | année fiscale en cours moins 20 ans  |
      | borne haute | année fiscale en cours plus 10 ans   |

  Scénario: Un champ obligatoire vide bloque la création
    Étant donné que l'entité "ENT-TEST-01" n'a pas encore de statut
    Et que le panneau de création est ouvert avec la nature "Renouvellement"
    Quand il sélectionne l'entité "ENT-TEST-01"
    Et qu'il laisse le champ "N° Requête BSC" vide
    Et qu'il clique sur "Valider la création"
    Alors la création est refusée
    Et un message d'erreur s'affiche
    Et aucune demande n'est créée pour l'entité "ENT-TEST-01"

  Plan du scénario: Une entité sans statut ou au statut validé permet de créer la demande
    Étant donné que l'entité "<entite>" <etat>
    Et que le panneau de création est ouvert avec la nature "<nature>"
    Quand il renseigne tous les champs obligatoires avec l'entité "<entite>"
    Et qu'il clique sur "Valider la création"
    Alors une demande est créée pour l'entité "<entite>"
    Et un message de confirmation s'affiche
    Et il est redirigé vers la page du formulaire

    Exemples:
      | cas                                | nature         | entite      | etat                             |
      | Renouvellement, entité sans statut | Renouvellement | ENT-TEST-01 | n'a pas encore de statut         |
      | Renouvellement, statut validé      | Renouvellement | ENT-TEST-02 | a une demande au statut "validé" |
      | Nouveau, entité sans statut        | Nouveau        | ENT-TEST-06 | n'a pas encore de statut         |
      | Nouveau, statut validé             | Nouveau        | ENT-TEST-08 | a une demande au statut "validé" |

  Plan du scénario: Une entité avec une demande en cours, en retard ou en révision bloque la création
    Étant donné que l'entité "<entite>" a une demande au statut "<statut>"
    Et que le panneau de création est ouvert avec la nature "<nature>"
    Quand il renseigne tous les champs obligatoires avec l'entité "<entite>"
    Et qu'il clique sur "Valider la création"
    Alors la création est refusée
    Et un message d'erreur s'affiche
    Et aucune nouvelle demande n'est créée pour l'entité "<entite>"
    Et la demande existante de l'entité "<entite>" est toujours au statut "<statut>"

    Exemples:
      | cas                         | nature         | entite      | statut   |
      | Renouvellement, en cours    | Renouvellement | ENT-TEST-03 | en cours |
      | Renouvellement, en retard   | Renouvellement | ENT-TEST-04 | retard   |
      | Renouvellement, en révision | Renouvellement | ENT-TEST-05 | révision |
      | Nouveau, en cours           | Nouveau        | ENT-TEST-07 | en cours |
```

## 8. Couverture

| Critère | Scénarios | Couvert ? |
|---|---|---|
| R1 bouton visible pour Admin et SuperAdmin seulement | Plan « Le bouton … n'est affiché que pour les rôles Admin et SuperAdmin » (3 cas) | Couvert. Comptes SuperAdmin et User non définis au contexte (Q13) |
| R2 panneau latéral à droite | « Le panneau de création s'ouvre à droite de la liste » | Couvert |
| R3 Nature du mandat, deux valeurs | « Le champ "Nature du mandat" propose deux valeurs » | Partiel : valeur initiale et caractère obligatoire inconnus (Q8) |
| R4 champs du Renouvellement | « La nature Renouvellement affiche quatre champs … » | Partiel : l'effet « tous obligatoires » n'est testé que sur "N° Requête BSC" (voir R15) |
| R5 champs de Nouveau | « La nature Nouveau affiche en plus le champ Reprise » | Partiel : l'effet de Reprise Oui ou Non sur la création n'est pas écrit |
| R6 pas de saisie libre de l'entité | « Le champ "Entité ID" n'accepte pas de code saisi librement » | Partiel : mode de choix de l'entité et « référentiel » non définis (Q9) |
| R8 N° Requête BSC libre | « Le champ "N° Requête BSC" accepte une saisie libre » | Couvert. Limite de longueur et format inconnus (Q13) |
| R9 Affectée à par défaut | Plan « … propose par défaut le nom du compte connecté » (2 cas) | Couvert |
| R10 Affectée à, nom connu | « … accepte le nom d'un collaborateur connu » | Couvert pour le nom connu. Nom inconnu : voir R11 |
| R12 Millésime Renouvellement | Plan « s'ouvre sur l'année fiscale en cours » ; Plan « Les bornes de la liste » | Partiel : inclusion des bornes et définition de l'année fiscale à confirmer (Q12) ; aucun cas hors plage, le comportement n'est pas écrit |
| R13 Millésime Nouveau, valeur par défaut | Plan « s'ouvre sur l'année fiscale en cours » | Couvert pour la valeur par défaut seulement (R14 non rédigé) |
| R15 champ obligatoire vide | « Un champ obligatoire vide bloque la création » | Partiel : seul "N° Requête BSC" est laissé vide. Les autres champs ont une valeur par défaut ou un mode de choix inconnu (Q8, Q9). Texte et emplacement du message inconnus (Q10) |
| R18 création avec entité sans statut ou validée | Plan « Une entité sans statut ou au statut validé permet de créer la demande » (4 cas) | Couvert, sous réserve de Q3 (documents obligatoires) |
| R19 refus pour demande en cours, retard ou révision | Plan « … bloque la création » (4 cas) | Couvert. Texte du message inconnu (Q10) |
| R21 message de confirmation ou d'erreur | Intégré aux scénarios R15, R18, R19 | Partiel : textes non fournis (Q10) |
| R22 création de la demande | Plan de création (R18) | Couvert, sous réserve de Q3. Statut initial inconnu (Q11) |
| R23 redirection vers la page du formulaire | Plan de création (R18) | Partiel : nom de l'écran inconnu (Q11) |

## 9. Non rédigé

| Règle | Raison | Renvoi |
|---|---|---|
| R7 entité ID inconnue (surlignage rouge, message « entité ID inconnue ») | À arbitrer : condition tronquée, contradiction avec l'absence de saisie libre | Q1 |
| R11 Affectée à avec un nom inconnu | À arbitrer : comportement non écrit | Q7 |
| R14 Millésime de Nouveau, bornes et dates | À arbitrer : renvoi à l'US 424139 non fournie | Q4 |
| R16 règles métier liées à la nature du mandat | À arbitrer : règles non listées | Q5 |
| R17 documents obligatoires | À arbitrer : liste et écran absents | Q2, Q3 |
| R20 entité dont la demande a un autre statut | À arbitrer : comportement non écrit | Q6 |
| Exploratoire : changer la nature après saisie, fermer le panneau sans valider, entité avec plusieurs demandes | Hors de ce que l'US promet | Idées exploratoires de l'analyse |

Aucun scénario de récupération : l'US ne dit pas que l'utilisateur peut corriger et recommencer après un refus.

## 10. Propositions pour le contexte (rédaction)

| # | Proposition (une ligne) | Section du contexte | Type | Source |
|---|---|---|---|---|
| 1 | Compte de test ADM-TEST-01, rôle Admin, utilisé pour la création de demandes | 4 | ajout | Scénarios US 417829 (à confirmer, Q13) |
| 2 | Compte de test SAD-TEST-01, rôle SuperAdmin | 4 | ajout | Scénarios US 417829 (à confirmer, Q13) |
| 3 | Compte de test USR-TEST-01, rôle User, sans accès au bouton « Nouvelle demande » | 4 | ajout | Scénarios US 417829 |
| 4 | Nom du compte ADM-TEST-01 : "Admin Test" (pour la valeur par défaut de « Affectée à ») | 8 | ajout | Scénarios US 417829 |
| 5 | Collaborateur fictif "Collaborateur Test", connu des collaborateurs KPMG | 8 | ajout | Scénarios US 417829 |
| 6 | Entités fictives : ENT-TEST-01 et ENT-TEST-06 sans statut ; ENT-TEST-02 et ENT-TEST-08 au statut validé ; ENT-TEST-03 et ENT-TEST-07 en cours ; ENT-TEST-04 en retard ; ENT-TEST-05 en révision | 8 | ajout | Scénarios US 417829 (R18, R19) |
| 7 | Une création réussie change l'état de l'entité utilisée : les entités des scénarios de création sont à remettre sans statut ou validées avant chaque rejeu | 8 | point à confirmer | Scénarios US 417829 (Q11) |
| 8 | Écran « Liste des demandes » et panneau latéral de création : champs par nature du mandat | 7 | ajout | US 417829 §2, §3 |
| 9 | Libellés de statut utilisés tels qu'écrits dans l'US : « validé », « en cours », « retard », « révision » | 5 | point à confirmer | US 417829 §4 (Q6) |
