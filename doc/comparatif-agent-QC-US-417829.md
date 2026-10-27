# Agent QC actuel et nouvel agent : ce que chacun produit sur l'US 417829

US 417829 « Créer une nouvelle demande ».

| | Agent actuel | Nouvel agent |
|---|---|---|
| Outil | Agent GitHub du dépôt | Claude Code, `claude --agent qc` |
| Modèle | Claude Sonnet 5.5 | Claude Sonnet 5.5 |
| Ce qu'il a lu | Le work item dans Azure DevOps | Le même texte d'US, exporté dans un fichier (Azure DevOps n'était pas joignable depuis l'environnement de test) ; un contexte projet presque vide (rôles et plan) |
| Commandes | Une demande | `/us-analysis 417829`, `/gherkin-test-generation 417829`, puis `/maj-contexte 417829` |
| Sortie relue | TC-001 à TC-014, début de TC-015, liste de cas d'interface | Lancement du 27/10 : `resultat-agent-US-417829-27-10.md` et son tableau Azure DevOps `resultat-agent-US-417829-27-10-ado.md` |

« §2 » renvoie à la section 2 de la description de l'US, « TC-004 » à un cas de l'agent actuel.

## En bref

1. Le nouvel agent produit 25 cas exécutables (14 scénarios), tous passés au contrôle automatique sans erreur. L'agent actuel en produit au moins 15.
2. Il couvre la règle de validation du §4 dans ses 5 situations, pour les deux natures de mandat. L'agent actuel en couvre une dans TC-001 à TC-015.
3. Il pose 14 questions au PO, dont 4 bloquantes, et n'invente aucun cas.
4. Il propose de lui-même ce qu'il faut ajouter au contexte du projet, après l'analyse puis après la rédaction ; rien n'est écrit sans accord.

## 1. Ce que chacun livre

| Élément | Agent actuel | Nouvel agent |
|---|---|---|
| Structure | 5 parties fixes : analyse, risques, tableau des cas, cas limites, autres cas (API, UI) | Analyse (règles, préconditions, combinaisons, questions, verdict, propositions pour le contexte), scénarios, couverture, non rédigé, propositions pour le contexte |
| Règles de l'US | Pas de liste | 23 règles, chacune avec sa section et son statut : 17 rédigeables, 6 à arbitrer |
| Questions au PO | Aucune : son format ne le prévoit pas | 14, dont 4 bloquantes |
| Cas de test | Au moins 15 lignes Given, When, Then, toutes de type « Fonctionnel » | 14 scénarios en français, 25 cas exécutables, 0 erreur au contrôle |
| Tableau pour Azure DevOps | Écrit par l'IA | Produit par un script à partir des scénarios relus : `ID, Test case, Gherkin BDD scenario, Type of test`, préconditions répétées dans chaque cas, paramètres en `@role` |
| Type de test | « Fonctionnel » partout ; seuls ces cas sont publiés | Fonctionnel ou UI selon le cas ; tous les cas retenus sont publiables |
| Données de test | Aucune, sauf « Jean Dupont » (TC-007) | Comptes, entités et collaborateur fictifs nommés (`ADM-TEST-01`, `ENT-TEST-03`…) |
| Ajouts hors US | « Désactivation du bouton pendant l'envoi (anti double clic) » | Aucun cas ; 3 idées exploratoires, séparées et sans scénario |
| Contexte projet | Aucun | Propositions après l'analyse et après la rédaction (comptes, données, écrans, variations, points à confirmer), écrites seulement après « oui » |
| Publication | Automatique ; un plan créé pour chaque US | Après relecture et accord, dans le plan existant ; ou un CSV |

## 2. La même exigence, deux rédactions

### Le bouton selon le rôle (§1)

Agent actuel, TC-003 :

```
Given un utilisateur connecté avec un rôle autre qu'Admin ou SuperAdmin, When il accède à la Liste des demandes, Then le bouton « Nouvelle demande » n'est pas affiché
```

Nouvel agent :

```gherkin
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

Ce qu'il apporte : un rôle et un compte précis pour chaque ligne. « Un rôle autre » ne dit pas lequel préparer.

### Affectée à (§3)

Agent actuel, TC-008 :

```
Given le formulaire affiché, When l'utilisateur saisit un nom ou prénom de collaborateur KPMG connu et le sélectionne, Then le collaborateur est affecté à la demande
```

Nouvel agent (le Contexte de la fonctionnalité connecte `ADM-TEST-01` sur la « Liste des demandes ») :

```gherkin
Scénario: Le champ "Affectée à" accepte le nom d'un collaborateur connu
  Étant donné que le collaborateur "Collaborateur Test" est connu des collaborateurs KPMG
  Et que le panneau de création est ouvert avec la nature "Renouvellement"
  Quand il renseigne "Collaborateur Test" dans le champ "Affectée à"
  Alors le champ "Affectée à" affiche "Collaborateur Test"
```

Ce qu'il apporte : un résultat vérifiable sur le moment. Dans TC-008, « affecté à la demande » ne peut pas se vérifier, la demande n'existant pas encore. Le cas d'un nom inconnu devient une question (Q7) au lieu d'un résultat supposé.

### La règle de validation (§4)

Texte de l'US, §4, 4e point : « une création de demande possible avec une entité ID qui n'a pas encore de statut ou bien un statut validé (erreur si une entité ID a déjà une demande en statut : en cours, retard ou révision) ».

Agent actuel : seul TC-012, « entité sans demande existante », touche cette règle dans TC-001 à TC-015.

Nouvel agent : 4 créations acceptées (sans statut et validé, pour Renouvellement et pour Nouveau) et 4 refus :

```gherkin
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

Ce qu'il apporte : la règle la plus importante de l'US est testée en entier. Si elle casse, une entité reçoit une nouvelle demande alors qu'une autre est déjà en cours, en retard ou en révision. Chaque refus vérifie aussi que la demande existante n'a pas changé. Il demande en plus ce que donne une entité qui a plusieurs demandes (idée exploratoire) et quels autres statuts existent (Q6).

### L'entité inconnue (§3)

L'US dit qu'on ne peut pas saisir librement l'Entité ID, mais annonce un message « entité ID inconnue », dans une phrase incomplète.

Agent actuel : TC-011 teste que seule une sélection est possible, et sa liste de cas d'interface prévoit aussi l'erreur « Entité ID inconnue », sans relever l'écart.

Nouvel agent : il teste aussi que la saisie libre est impossible, et pose une question bloquante (Q1) : dans quel cas précis l'erreur apparaît-elle, et vaut-elle aussi pour Renouvellement ?

## 3. Section par section

| Section de l'US | Agent actuel | Nouvel agent | Ce qu'il apporte |
|---|---|---|---|
| §1 Accès | TC-001, TC-002, TC-003 | 1 plan, 3 lignes | Comptes nommés, dont le rôle User |
| §2 Panneau | TC-004 | 1 scénario, type UI | Un résultat par ligne |
| §3 Valeurs de Nature du mandat | Aucun cas | 1 scénario | Les deux valeurs vérifiées |
| §3 Champs par nature | TC-005, TC-006 | 2 scénarios | Reprise absent en Renouvellement, valeurs Oui et Non en Nouveau |
| §3 Entité ID sans saisie libre | TC-011 | 1 scénario | Équivalent |
| §3 N° Requête BSC libre | Aucun cas | 1 scénario | Vérifié |
| §3 Affectée à | TC-007, TC-008 | 2 cas par défaut (deux natures) et 1 scénario de saisie | Résultat vérifiable avant la création |
| §3 Millésime | TC-009, TC-010 | Défaut dans les deux natures, bornes -20 et +10 en Renouvellement | Équivalent, plus le défaut en Nouveau |
| §3 Entité ID inconnue | Prévue en test d'interface | Question bloquante Q1 | Le point ambigu remonte au PO |
| §4 Champs obligatoires | TC-015, un cas générique | 1 scénario (N° Requête BSC vide), avec « aucune demande n'est créée » | Les autres champs ont une valeur par défaut ou un mode de choix inconnu (Q8, Q9) |
| §4 Statut de l'entité | TC-012 : 1 situation sur 5 | 5 situations, dans les deux natures : 4 créations, 4 refus | Les 3 refus couverts |
| §4 Documents obligatoires | Aucun cas trouvé | Questions bloquantes Q2 et Q3 | La liste manque : demandée au PO |
| §4 Règles liées à la nature | Aucun cas trouvé | Question Q5 | Demandée au PO |
| §4 Messages | « cf maquettes » non repris | Messages vérifiés, texte demandé (Q10) | Le scénario existe, le texte se complète ensuite |
| §5 Création et redirection | TC-012, TC-013, TC-014 | 4 créations avec confirmation et redirection | Message de confirmation vérifié, comme l'écrit le §4 |
| Hors US | « Anti double clic » | Aucun cas | Rien d'inventé |

## 4. Ce que l'agent actuel fait aussi bien

1. Il couvre l'affichage de l'écran, la saisie libre de l'entité (TC-011) et le millésime (TC-009, TC-010) aussi bien.
2. Ses titres sont courts et lisibles par le métier.
3. Sa publication est bien outillée : codes HTTP contrôlés, liens vérifiés entre chaque cas et l'US.

## 5. Ce que le nouvel agent apporte de plus

1. Des cas exécutables sans rien reconstituer : rôle, compte, écran et données dans chaque cas.
2. La règle de validation couverte dans ses cinq situations, refus compris, avec la vérification que rien n'a changé.
3. Un résultat par ligne : dans Test Plans, on voit exactement ce qui échoue.
4. 14 questions au PO au lieu de suppositions, dont 4 bloquantes.
5. Rien d'inventé : les idées hors US sont séparées et n'ont pas de scénario.
6. Un tableau Azure DevOps produit par un script, sans recopie à la main.
7. Un contexte projet qui s'enrichit à chaque US, avec ce que l'équipe a validé.

## 6. Comment on en est arrivé là

| Lancement | Résultat | Ce qui a été corrigé ensuite |
|---|---|---|
| 1er, 20/10 | 11 cas ; 2 situations de validation sur 5 ; millésime et champs obligatoires non testés | Un refus dont le texte du message manque est maintenant rédigé ; seul le texte devient une question |
| 2e, 20/10 | 22 cas ; 5 situations sur 5 ; absence de Reprise en Renouvellement non vérifiée | Récupération, type de test, tableau Azure DevOps, propositions pour le contexte après la rédaction |
| 3e, 27/10 | 25 cas ; 5 situations sur 5 dans les deux natures ; Reprise vérifiée | |

Les chiffres varient d'un lancement à l'autre, même à consignes égales : c'est normal pour un modèle d'IA. L'agent se juge donc sur plusieurs lancements par US.

## 7. Limites de cette comparaison

1. Le nouvel agent a lu l'US dans un fichier exporté, sans ses 4 commentaires ni les maquettes. Il reste à le lancer sur le dépôt de l'équipe, avec l'accès Azure DevOps.
2. Son contexte projet était presque vide. Avec des comptes de test et des statuts renseignés, ses préconditions seront plus précises.
3. Une seule US. La comparaison doit être refaite sur 3 US déjà traitées à la main, avec les mêmes mesures : cas inventés, cas acceptés sans retouche, temps de relecture.
