# Agent QC actuel et nouvel agent : ce que chacun produit sur l'US 417829

US 417829 « Créer une nouvelle demande ».

| | Agent actuel | Nouvel agent |
|---|---|---|
| Outil | Agent GitHub du dépôt | Claude Code, `claude --agent qc` |
| Modèle | Claude Sonnet 5.5 | Claude Sonnet 5.5 |
| Ce qu'il a lu | Le work item dans Azure DevOps | Le même texte d'US, exporté dans un fichier (Azure DevOps n'était pas joignable depuis l'environnement de test) ; un contexte projet presque vide (rôles et plan) |
| Commandes | Une demande | `/us-analysis 417829`, puis `/gherkin-test-generation 417829` |
| Sortie relue | TC-001 à TC-014, début de TC-015, liste de cas d'interface | Rapport complet : `resultat-agent-US-417829.md` |

« §2 » renvoie à la section 2 de la description de l'US, « TC-004 » à un cas de l'agent actuel.

## En bref

1. Le nouvel agent produit 22 cas exécutables (14 scénarios), tous passés au contrôle sans erreur. L'agent actuel en produit au moins 15.
2. Il couvre la règle de validation du §4 dans ses 5 situations ; l'agent actuel en couvre une dans TC-001 à TC-015.
3. Il pose 12 questions au PO, dont 6 bloquantes, et n'invente aucun cas.
4. Un premier passage du nouvel agent était trop prudent : il laissait en question tout refus dont le texte du message manquait, et ne testait donc que 2 situations sur 5. La consigne a été corrigée (un message dont le texte manque n'empêche pas d'écrire le refus), puis l'agent a été relancé : c'est ce second résultat qui est comparé ici.

## 1. Ce que chacun livre

| Élément | Agent actuel | Nouvel agent |
|---|---|---|
| Structure | 5 parties fixes : analyse, risques, tableau des cas, cas limites, autres cas (API, UI) | Analyse (règles, préconditions, combinaisons, questions, verdict, propositions pour le contexte), scénarios, couverture, non rédigé |
| Règles de l'US | Pas de liste | 20 règles, chacune avec sa section et son statut : 15 rédigeables, 5 à arbitrer |
| Questions au PO | Aucune : son format ne le prévoit pas | 12, dont 6 bloquantes |
| Cas de test | Au moins 15 lignes Given, When, Then, toutes de type « Fonctionnel » | 14 scénarios en français, 22 cas exécutables, 0 erreur au contrôle |
| Données de test | Aucune, sauf « Jean Dupont » (TC-007) | Comptes, entités et collaborateur fictifs nommés (`ADM-TEST-01`, `ENT-TEST-04`, `COL-TEST-01`…) |
| Couverture | Non mesurée | Tableau règle par règle, avec ce qui reste ouvert |
| Ajouts hors US | « Désactivation du bouton pendant l'envoi (anti double clic) » | Aucun cas ; 3 idées exploratoires, séparées et sans scénario |
| Contexte projet | Aucun | 11 propositions d'ajout, à valider avant écriture |
| Publication | Automatique ; un plan créé pour chaque US ; seuls les cas « Fonctionnel » | Après relecture et accord, dans le plan existant ; ou un CSV |

## 2. La même exigence, deux rédactions

### Le bouton selon le rôle (§1)

Agent actuel, TC-001, TC-002 et TC-003 :

```
Given un utilisateur connecté avec un rôle autre qu'Admin ou SuperAdmin, When il accède à la Liste des demandes, Then le bouton « Nouvelle demande » n'est pas affiché
```

Nouvel agent :

```gherkin
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
```

Ce qu'il apporte : un rôle et un compte précis pour chaque ligne. « Un rôle autre » ne dit pas lequel préparer.

### Affectée à (§3)

Agent actuel, TC-008 :

```
Given le formulaire affiché, When l'utilisateur saisit un nom ou prénom de collaborateur KPMG connu et le sélectionne, Then le collaborateur est affecté à la demande
```

Nouvel agent :

```gherkin
Scénario: "Affectée à" accepte le nom prénom d'un collaborateur KPMG
  Étant donné que le collaborateur "COL-TEST-01" est connu des collaborateurs KPMG
  Quand il sélectionne la nature "Renouvellement"
  Et qu'il saisit le nom prénom de "COL-TEST-01" dans le champ "Affectée à"
  Alors le champ "Affectée à" affiche le nom prénom de "COL-TEST-01"
  Et le champ "Affectée à" n'est pas en erreur
```

Ce qu'il apporte : un résultat vérifiable sur le moment. Dans TC-008, « affecté à la demande » ne peut pas se vérifier, la demande n'existant pas encore. Le cas d'un nom inconnu devient une question (Q5) au lieu d'un résultat supposé.

### La règle de validation (§4)

Texte de l'US, §4, 4e point : « une création de demande possible avec une entité ID qui n'a pas encore de statut ou bien un statut validé (erreur si une entité ID a déjà une demande en statut : en cours, retard ou révision) ».

Agent actuel : seul TC-012, « entité sans demande existante », touche cette règle dans TC-001 à TC-015.

Nouvel agent : deux créations acceptées (entité sans statut, statut validé), une création en Nouveau, et les trois refus :

```gherkin
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
```

Ce qu'il apporte : la règle la plus importante de l'US est testée en entier. Si elle casse, une entité reçoit une nouvelle demande alors qu'une autre est déjà en cours, en retard ou en révision. Chaque refus vérifie aussi que la demande existante n'a pas changé. Il pose en plus une question que personne n'avait vue (Q6) : « Le statut est-il celui de l'entité ou celui de la demande ? »

### L'entité inconnue (§3)

L'US dit qu'on ne peut pas saisir librement l'Entité ID, mais annonce un message « entité ID inconnue », dans une phrase incomplète.

Agent actuel : TC-011 teste que seule une sélection est possible, et sa liste de cas d'interface prévoit aussi l'erreur « Entité ID inconnue », sans relever l'écart.

Nouvel agent : il teste aussi que la saisie libre est impossible, et pose une question bloquante (Q1) : « Comment l'utilisateur peut-il valider avec une entité ID inconnue ? Dans quel cas exact l'erreur s'affiche-t-elle ? Cette erreur vaut-elle aussi pour Renouvellement ? »

## 3. Section par section

| Section de l'US | Agent actuel | Nouvel agent | Ce qu'il apporte |
|---|---|---|---|
| §1 Accès | TC-001, TC-002, TC-003 | 1 plan, 3 lignes | Comptes nommés, dont le rôle User |
| §2 Panneau | TC-004 | 1 scénario | Un résultat par ligne |
| §3 Valeurs de Nature du mandat | Aucun cas | 1 scénario | Les deux valeurs vérifiées |
| §3 Champs par nature | TC-005, TC-006 | 2 scénarios | Valeurs de Reprise vérifiées (Oui, Non) |
| §3 Entité ID sans saisie libre | TC-011 | 1 scénario | Équivalent |
| §3 Affectée à | TC-007, TC-008 | 2 scénarios | Résultat vérifiable avant la création |
| §3 Millésime | TC-009, TC-010 | 2 plans : défaut dans les deux natures, bornes -20 et +10 | Équivalent, plus le défaut en Nouveau |
| §3 Entité ID inconnue | Prévue en test d'interface | Question bloquante Q1 | Le point ambigu remonte au PO |
| §4 Champs obligatoires | TC-015, un cas générique | 1 plan, un cas par champ sans valeur par défaut (2) | On sait quel champ est en cause, et on vérifie qu'aucune demande n'est créée |
| §4 Statut de l'entité | TC-012 : 1 situation sur 5 | 5 situations, plus une création en Nouveau | Les 3 refus couverts |
| §4 Documents obligatoires | Aucun cas trouvé | Question bloquante Q2 | La liste manque : demandée au PO |
| §4 Règles liées à la nature | Aucun cas trouvé | Question bloquante Q3 | Demandée au PO |
| §4 Messages | « cf maquettes » non repris | Messages vérifiés, texte demandé (Q8) | Le scénario existe, le texte se complète ensuite |
| §5 Création et redirection | TC-012, TC-013, TC-014 | 3 créations avec confirmation et redirection | Message de confirmation vérifié, comme l'écrit le §4 |
| Hors US | « Anti double clic » | Aucun cas | Rien d'inventé |

## 4. Ce que l'agent actuel fait aussi bien, ou mieux

1. TC-005 vérifie que Reprise n'est pas affiché en Renouvellement. Le nouvel agent liste les quatre champs de Renouvellement sans vérifier l'absence de Reprise : c'est une perte.
2. Il donne une donnée concrète pour la valeur par défaut d'« Affectée à » (TC-007, « Jean Dupont »).
3. Il couvre la saisie libre de l'entité (TC-011) et le millésime (TC-009, TC-010) aussi bien.
4. Ses titres sont courts et lisibles par le métier.
5. Sa publication est bien outillée : codes HTTP contrôlés, liens vérifiés entre chaque cas et l'US.

## 5. Ce que le nouvel agent apporte de plus

1. Des cas exécutables sans rien reconstituer : rôle, compte, écran et données dans chaque cas.
2. La règle de validation couverte dans ses cinq situations, refus compris, avec la vérification que rien n'a changé.
3. Un résultat par ligne : dans Test Plans, on voit exactement ce qui échoue.
4. 12 questions au PO au lieu de suppositions, dont 6 bloquantes.
5. Rien d'inventé : les idées hors US sont séparées et n'ont pas de scénario.
6. Une couverture lisible règle par règle, avec ce qui reste ouvert et pourquoi.
7. Des propositions pour enrichir le contexte du projet, appliquées seulement après validation.

## 6. Limites de cette comparaison

1. Le nouvel agent a lu l'US dans un fichier exporté, sans ses 4 commentaires ni les maquettes. Il reste à le lancer sur le dépôt de l'équipe, avec l'accès Azure DevOps.
2. Son contexte projet était presque vide. Avec des comptes de test et des statuts renseignés, ses préconditions seront plus précises.
3. La consigne sur les messages a été corrigée après un premier passage trop prudent. Il faut vérifier sur d'autres US que la correction ne pousse pas l'agent dans l'excès inverse.
4. Une seule US. La comparaison doit être refaite sur 3 US déjà traitées à la main, avec les mêmes mesures : cas inventés, cas acceptés sans retouche, temps de relecture.
