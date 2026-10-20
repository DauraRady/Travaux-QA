# Agent QC actuel et version proposée : ce que chacun produit sur l'US 417829

US 417829 « Créer une nouvelle demande ».

Sources :
1. La sortie de l'agent actuel : cas TC-001 à TC-014, début de TC-015, et sa liste de cas d'interface.
2. Le résultat de la version proposée, obtenu en appliquant ses consignes hors de l'outil de l'équipe : analyse et scénarios.

« §2 » renvoie à la section 2 de la description de l'US, « TC-004 » à un cas de l'agent actuel.

## En bref

Sur l'écran (sections 1 à 3 de l'US), les deux versions couvrent à peu près la même chose. La différence est ailleurs :

1. Les cas de la version proposée sont exécutables tels quels : on sait avec quel rôle se connecter, sur quel écran partir et quelles données préparer.
2. Elle couvre la règle métier de la validation (§4) dans ses cinq situations, quand l'agent actuel en couvre une dans TC-001 à TC-015.
3. Elle pose 9 questions au PO au lieu de supposer, et n'ajoute rien que l'US ne décrit pas.

## 1. Ce que chacun livre

| Élément | Agent actuel | Version proposée |
|---|---|---|
| Structure | 5 parties fixes : analyse, risques, tableau des cas, cas limites, autres cas (API, UI) | Analyse de l'US, scénarios, tableau de couverture, liste de ce qui n'est pas rédigé |
| Règles de l'US | Pas de liste | 15 règles, chacune avec sa section et un statut (rédigeable, à arbitrer) |
| Questions au PO | Aucune : son format ne le prévoit pas | 9, dont 2 bloquantes |
| Cas de test | Au moins 15 lignes Given, When, Then, toutes de type « Fonctionnel » | 11 scénarios en français, soit 23 cas exécutables |
| Données de test | Aucune, sauf « Jean Dupont » (TC-007) | Comptes et entités fictifs nommés (`ADM-TEST-01`, `ENT-TEST-03`…) |
| Couverture | Non mesurée | Tableau section par section, avec ce qui reste ouvert |
| Publication | Automatique ; un plan créé pour chaque US ; seuls les cas « Fonctionnel » sont créés | Après relecture et accord, dans le plan existant ; ou un CSV à importer |

## 2. La même exigence, deux rédactions

### Un rôle non autorisé ne voit pas le bouton (§1)

Agent actuel, TC-003 :

```
Given un utilisateur connecté avec un rôle autre qu'Admin ou SuperAdmin, When il accède à la Liste des demandes, Then le bouton « Nouvelle demande » n'est pas affiché
```

Version proposée :

```gherkin
Scénario: Un User ne voit pas le bouton de création
  Étant donné que l'utilisateur "USR-TEST-01" est connecté avec le rôle "User"
  Quand il ouvre la page "Liste des demandes"
  Alors la liste des demandes s'affiche
  Mais le bouton "Nouvelle demande" n'est pas affiché
```

Ce qu'on apporte : un rôle et un compte précis, que le testeur peut préparer. « Un rôle autre » ne dit pas lequel utiliser. Le rôle User vient du contexte du projet, pas de l'US : c'est à confirmer.

### Le formulaire s'ouvre dans un panneau (§2)

Agent actuel, TC-004 :

```
Given un Admin sur la Liste des demandes, When il clique sur « Nouvelle demande », Then un panneau latéral s'ouvre à droite avec le formulaire de création et la liste reste visible en arrière-plan
```

Version proposée :

```gherkin
Scénario: Le formulaire de création s'ouvre dans un panneau à droite
  Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
  Et qu'il est sur la page "Liste des demandes"
  Quand il clique sur "Nouvelle demande"
  Alors un panneau s'ouvre sur la droite de l'écran
  Et le formulaire de création d'une demande est affiché dans ce panneau
  Et la "Liste des demandes" reste visible en arrière-plan
```

Ce qu'on apporte : la même couverture, mais avec un résultat par ligne. Dans Test Plans, chaque résultat se coche séparément, et on voit lequel échoue.

### Modifier « Affectée à » (§3)

Agent actuel, TC-008 :

```
Given le formulaire affiché, When l'utilisateur saisit un nom ou prénom de collaborateur KPMG connu et le sélectionne, Then le collaborateur est affecté à la demande
```

Version proposée :

```gherkin
Scénario: Un collaborateur est proposé quand on saisit son nom dans Affectée à
  Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"
  Et que le collaborateur "COLLAB-TEST-02" existe dans le référentiel des collaborateurs
  Et que le panneau de création est ouvert avec la nature "Renouvellement"
  Quand il efface le champ "Affectée à"
  Et qu'il saisit le nom et le prénom de "COLLAB-TEST-02"
  Alors "COLLAB-TEST-02" est proposé dans la liste de résultats
```

Ce qu'on apporte : un résultat qui se vérifie à ce moment-là. Dans TC-008, « affecté à la demande » ne peut pas se vérifier : la demande n'est pas encore créée.

### La règle de validation (§4)

Texte de l'US, §4, 4e point : « une création de demande possible avec une entité ID qui n'a pas encore de statut ou bien un statut validé (erreur si une entité ID a déjà une demande en statut : en cours, retard ou révision) ».

Agent actuel : TC-012 couvre la seule situation « entité sans demande ». Aucun des cas TC-001 à TC-015 ne couvre les quatre autres.

```
Given une entité sans demande existante et tous les champs Renouvellement renseignés, When l'utilisateur clique sur « Valider la création », Then la demande est créée et l'utilisateur est redirigé vers la page du formulaire
```

Version proposée : deux plans, cinq situations. Voici les trois refus :

```gherkin
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
```

Ce qu'on apporte : c'est la règle la plus importante de l'US. Si elle casse, une entité reçoit une nouvelle demande alors qu'une autre est déjà en cours, en retard ou en révision. Chaque refus vérifie aussi que la demande existante n'a pas été modifiée.

### Ce que l'US ne dit pas : l'entité inconnue (§3)

L'US dit qu'on ne peut pas saisir librement l'Entité ID. Elle annonce pourtant un message « entité ID inconnue », et la phrase qui l'introduit est incomplète.

Agent actuel : TC-011 teste que seule une sélection est possible. Sa liste de cas d'interface prévoit aussi l'erreur « Entité ID inconnue », sans relever l'écart entre les deux.

Version proposée : aucun cas sur ce point, mais une question bloquante au PO :

« Une Entité ID inconnue peut être refusée, mais la saisie libre est impossible : comment l'utilisateur peut-il choisir une entité inconnue ? »

Ce qu'on apporte : on ne prépare pas un test dont personne ne sait comment le provoquer, et le PO tranche avant le développement.

## 3. Section par section

| Section de l'US | Agent actuel | Version proposée | Ce qu'on apporte |
|---|---|---|---|
| §1 Accès | TC-001, TC-002, TC-003 | Plan Admin et SuperAdmin ; scénario User | Rôles et comptes nommés |
| §2 Panneau | TC-004 | 1 scénario | Un résultat par ligne |
| §3 Champs par nature | TC-005, TC-006 | 2 scénarios | Valeurs de Reprise vérifiées (Oui, Non) |
| §3 Valeurs par défaut | TC-007, TC-009 | Plan sur les deux natures | Vérifié pour Renouvellement et pour Nouveau |
| §3 Millésime | TC-010 (plage de -20 à +10 ans) | Plan en 4 vérifications | Équivalent : même règle, découpée |
| §3 Affectée à | TC-008 | 1 scénario | Résultat vérifiable avant la création |
| §3 Entité ID | TC-011 ; erreur « inconnue » en test d'interface | Questions Q1 (bloquante) et Q6 | Le point ambigu est remonté au PO |
| §4 Champs obligatoires | TC-015, un cas générique | Plan, un cas par champ (4) | On sait quel champ est en cause, et on vérifie qu'aucune demande n'est créée |
| §4 Statut de l'entité | TC-012 : 1 situation sur 5 | Plans : 5 situations | Les 3 refus couverts |
| §4 Documents obligatoires | Aucun cas trouvé | Question Q3 (bloquante) | La liste manque : demandée au PO |
| §4 Règles liées à la nature | Aucun cas trouvé | Question Q7 | Demandée au PO |
| §4 Messages | « cf maquettes » non repris | Question Q2 | Texte exact demandé, à recopier ensuite |
| §5 Création et redirection | TC-012, TC-013, TC-014 | 3 cas dans le plan des créations acceptées | Message de confirmation ajouté, comme l'écrit le §4 |
| Hors US | « Désactivation du bouton pendant l'envoi (anti double clic) » | Rien | Aucun cas inventé |

## 4. Ce que l'agent actuel fait aussi bien, ou mieux

1. Il teste l'interdiction de saisie libre de l'Entité ID (TC-011). La version proposée la laisse en question (Q6) : sur ce point, l'agent actuel va plus loin.
2. Il crée une demande en Renouvellement sur une entité sans demande (TC-012), ce que le §4 permet. La version proposée en a fait une question (Q8) : elle est trop prudente sur ce point.
3. Il donne une donnée concrète pour la valeur par défaut d'« Affectée à » (TC-007, « Jean Dupont »).
4. Il couvre le millésime aussi bien (TC-009, TC-010).
5. Ses titres sont courts et lisibles par le métier.
6. Sa publication est bien outillée : codes HTTP contrôlés, liens vérifiés entre chaque cas et l'US.

## 5. Ce que la version proposée apporte de plus

1. Des cas exécutables sans rien reconstituer : rôle, compte, écran et données dans chaque cas.
2. La règle métier de la validation couverte dans ses cinq situations, refus compris, avec la vérification que rien n'a changé.
3. Un résultat par ligne : dans Test Plans, on voit exactement ce qui échoue.
4. 9 questions au PO au lieu de suppositions ; 2 bloquent l'exécution (entité inconnue, documents obligatoires).
5. Rien d'inventé : aucun cas hors US.
6. Une couverture lisible section par section, avec ce qui reste ouvert et pourquoi.
7. Tous les cas retenus peuvent être publiés, pas seulement les cas « Fonctionnel », et uniquement après relecture.

## 6. Limites de cette comparaison

1. Le résultat de la version proposée a été obtenu hors de l'outil de l'équipe. Le vrai test est de rejouer le nouvel agent sur la même US.
2. La sortie de l'agent actuel continue après TC-015 ; ses parties analyse, risques et cas limites n'ont pas été comparées.
3. Une seule US : la comparaison doit être refaite sur 3 US déjà traitées à la main, avec les mêmes mesures (cas inventés, cas acceptés sans retouche, temps de rédaction).
