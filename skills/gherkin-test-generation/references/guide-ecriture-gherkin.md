# Guide d'écriture d'un scénario Gherkin

Ce guide accompagne le skill `gherkin-test-generation`. Toutes les données de l'exemple sont fictives.

## 1. À quoi sert chaque mot-clé

| Mot-clé | Rôle | Question à laquelle il répond | Exemple |
|---|---|---|---|
| `Fonctionnalité:` | Le sujet du fichier : une capacité métier | De quoi parle ce fichier ? | `Fonctionnalité: Validation d'une demande` |
| `Règle:` | Une règle métier, qui regroupe ses scénarios | Quelle règle ces exemples illustrent-ils ? | `Règle: Seule une demande soumise peut être validée` |
| `Contexte:` | Les préconditions communes à tous les scénarios | Qu'est-ce qui est vrai avant chaque scénario, sans exception ? | `Étant donné que je suis connecté avec le rôle "Valideur"` |
| `Scénario:` | Un exemple concret de la règle | Quel comportement précis vérifie-t-on ? | `Scénario: Valider une demande soumise la fait passer au statut Validée` |
| `Étant donné` | L'état de départ : les préconditions | Dans quelle situation est-on avant d'agir ? | `Étant donné que la demande "DEM-001" est au statut "Soumise"` |
| `Quand` | L'action testée, une seule | Que fait l'utilisateur ou le système ? | `Quand je valide la demande "DEM-001"` |
| `Alors` | Le résultat observable | Qu'est-ce qu'on doit constater ? | `Alors la demande "DEM-001" est au statut "Validée"` |
| `Et`, `Mais` | Prolongent le mot-clé précédent | | `Et la date de validation est renseignée` |
| `Plan du scénario:` et `Exemples:` | Le même scénario rejoué avec plusieurs jeux de données | Quelles valeurs testent la même règle ? | Voir section 5 |

## 2. La question des préconditions

Oui, les préconditions vont dans le Gherkin. Elles s'écrivent avec `Étant donné`, et il y a trois endroits possibles :

| Où | Quand l'utiliser | Exemple |
|---|---|---|
| Dans le scénario, en `Étant donné` | La précondition est propre à ce scénario | `Étant donné que la demande "DEM-002" est au statut "Brouillon"` |
| Dans le `Contexte` de la fonctionnalité | Elle est vraie pour tous les scénarios du fichier | Le rôle connecté, si tous les scénarios utilisent le même |
| Dans un `Contexte` placé sous une `Règle` | Elle est vraie pour tous les scénarios de cette règle seulement | Un paramétrage propre à la règle |

Trois erreurs fréquentes :

1. Écrire un parcours au lieu d'un état. `Étant donné que j'ouvre la page Demandes et que je clique sur DEM-001` décrit des clics. `Étant donné que la demande "DEM-001" est au statut "Soumise"` décrit l'état. La façon d'y arriver (API, base de test, interface) est le travail de l'automatisation ou du testeur, pas du scénario.
2. Mettre dans le `Contexte` une étape dont un scénario n'a pas besoin. Si un scénario teste un autre rôle, le rôle sort du `Contexte` et passe dans chaque scénario.
3. Faire dépendre un scénario d'un autre (« la demande validée au scénario précédent »). Chaque scénario pose lui-même son état de départ.

Dans Azure Test Plans, un cas de test a aussi un champ de préconditions ou un premier pas de préparation. C'est le même contenu que les `Étant donné` : voir la section 7.

## 3. Mauvais et bon scénario

Mauvais :

```gherkin
Scénario: Test validation
  Étant donné que j'ouvre l'application
  Et je saisis "valideur01" dans le champ "Identifiant"
  Et je clique sur "Se connecter"
  Et je clique sur le menu "Demandes"
  Quand je clique sur la ligne "DEM-001"
  Et je clique sur "Valider"
  Alors la demande est correctement validée
```

| Défaut | Pourquoi c'est un problème |
|---|---|
| Titre « Test validation » | On ne sait pas quel comportement est vérifié sans lire les étapes |
| `Étant donné` en clics | Le scénario casse à chaque changement d'écran, alors que la règle n'a pas changé |
| Deux actions (`Quand` puis `Et je clique`) | Si le test échoue, on ne sait pas laquelle a échoué |
| Statut de départ absent | On ne sait pas si DEM-001 était Soumise ou Brouillon : le test peut passer pour une mauvaise raison |
| « correctement validée » | Rien de vérifiable : quel statut, quelle valeur ? |

Bon :

```gherkin
@AC_1 @REGLE_R1 @positif
Scénario: Valider une demande soumise la fait passer au statut Validée
  Étant donné que je suis connecté avec le rôle "Valideur"
  Et que la demande "DEM-001" est au statut "Soumise"
  Quand je valide la demande "DEM-001"
  Alors la demande "DEM-001" est au statut "Validée"
```

## 4. Exemple complet, pas à pas

US fictive :

> En tant que valideur, je veux valider une demande soumise afin de lancer la saisie.
>
> AC-1 : Un valideur peut valider une demande au statut « Soumise » ; elle passe au statut « Validée ».
>
> AC-2 : Une demande au statut « Brouillon » ne peut pas être validée. Le message « Seules les demandes soumises peuvent être validées » s'affiche.
>
> AC-3 : Le commentaire de validation est facultatif et limité à 500 caractères. Au-delà, la validation est refusée avec le message « 500 caractères maximum ».

Étape 1 : extraire les règles.

| ID | Règle | Source | Technique |
|---|---|---|---|
| R1 | Une demande Soumise validée par un Valideur passe au statut Validée | AC-1 | Transitions d'état |
| R2 | Une demande Brouillon ne peut pas être validée, message exact fourni | AC-2 | Transitions d'état (transition interdite décrite) |
| R3 | Commentaire facultatif, 500 caractères maximum, refus au-delà avec message exact | AC-3 | Valeurs limites, partitions |

Étape 2 : repérer ce que la source ne dit pas.

1. Ce qui arrive si un autre rôle que Valideur tente de valider : non décrit.
2. Ce qui arrive pour les autres statuts (Validée, Rejetée…) : non décrit.

Ces deux points ne donnent aucun scénario. Ils vont en questions.

Étape 3 : choisir le Contexte. Tous les scénarios utilisent le rôle Valideur : il va dans le `Contexte`. Le statut de la demande change d'un scénario à l'autre : il reste dans chaque scénario.

Étape 4 : écrire.

```gherkin
# language: fr
@US_1234
Fonctionnalité: Validation d'une demande
  En tant que valideur
  Je veux valider une demande soumise
  Afin de lancer la saisie

  Contexte:
    Étant donné que je suis connecté avec le rôle "Valideur"

  Règle: Seule une demande soumise peut être validée

    # Technique : transitions d'état (transition autorisée)
    @AC_1 @REGLE_R1 @positif
    Scénario: Valider une demande soumise la fait passer au statut Validée
      Étant donné que la demande "DEM-001" est au statut "Soumise"
      Quand je valide la demande "DEM-001"
      Alors la demande "DEM-001" est au statut "Validée"

    # Technique : transitions d'état (transition interdite décrite)
    @AC_2 @REGLE_R2 @negatif
    Scénario: Une demande en brouillon ne peut pas être validée
      Étant donné que la demande "DEM-002" est au statut "Brouillon"
      Quand je tente de valider la demande "DEM-002"
      Alors le message "Seules les demandes soumises peuvent être validées" est affiché
      Et la demande "DEM-002" est toujours au statut "Brouillon"

  Règle: Le commentaire de validation est facultatif et limité à 500 caractères

    # Technique : partitions (commentaire absent) et valeurs limites (borne haute)
    @AC_3 @REGLE_R3 @edge_case
    Plan du scénario: Une validation avec un commentaire autorisé est acceptée : <cas>
      Étant donné que la demande "<demande>" est au statut "Soumise"
      Quand je valide la demande "<demande>" avec un commentaire de <longueur> caractères
      Alors la demande "<demande>" est au statut "Validée"

      Exemples:
        | cas              | demande | longueur |
        | commentaire vide | DEM-003 | 0        |
        | borne haute      | DEM-004 | 500      |

    # Technique : valeurs limites (juste au-delà de la borne)
    @AC_3 @REGLE_R3 @negatif
    Scénario: Une validation avec un commentaire de 501 caractères est refusée
      Étant donné que la demande "DEM-005" est au statut "Soumise"
      Quand je tente de valider la demande "DEM-005" avec un commentaire de 501 caractères
      Alors le message "500 caractères maximum" est affiché
      Et la demande "DEM-005" est toujours au statut "Soumise"
```

Ce qu'il faut remarquer :

1. Le `Contexte` ne contient que le rôle, commun aux quatre cas.
2. Chaque scénario a sa propre demande (DEM-001 à DEM-005) : ils peuvent tourner dans n'importe quel ordre.
3. Les deux refus vérifient que le statut n'a pas bougé. Sans cette ligne, une validation enregistrée puis suivie d'un message d'erreur passerait le test.
4. 500 et 501 sont séparés : le résultat n'a pas la même forme (accepté d'un côté, message de l'autre), donc pas le même plan.
5. Les messages sont copiés mot pour mot de l'AC.

Étape 5 : les éléments non couverts.

| Réf. | Élément | Raison | Question |
|---|---|---|---|
| AC-1 | Validation par un autre rôle que Valideur | Refus non décrit par la source | « Que se passe-t-il si un utilisateur sans le rôle Valideur tente de valider une demande ? » |
| AC-1, AC-2 | Validation d'une demande au statut Validée ou Rejetée | États non décrits | « Que se passe-t-il si on tente de valider une demande déjà Validée ou Rejetée ? » |

## 5. Plan du scénario : quand oui, quand non

| Situation | Choix |
|---|---|
| Même règle, mêmes étapes, seules les valeurs changent, même forme de résultat | `Plan du scénario` |
| Les résultats n'ont pas la même forme (accepté contre message d'erreur) | Scénarios séparés |
| Une seule ligne d'Exemples | `Scénario` simple |
| Les lignes testent toutes la même classe de valeurs | Garder une seule ligne |

## 6. Les mots à bannir dans un `Alors`

« correctement », « normalement », « comme prévu », « bien », « avec succès » sans dire ce qui est constaté, « une erreur s'affiche » quand la source donne le texte exact. Si la source ne donne pas le texte, l'étape générique est acceptable, et la question du texte exact part au PO.

## 7. Passage vers Azure Test Plans

Azure Test Plans ne lit pas le Gherkin. Si les scénarios doivent devenir des cas de test manuels :

| Gherkin | Cas de test Azure Test Plans |
|---|---|
| Titre du `Scénario` | Titre du cas de test |
| `Contexte` et `Étant donné` | Préconditions (premier pas de préparation, sans résultat attendu, ou champ dédié selon le modèle du projet) |
| `Quand` | Action d'un pas |
| `Alors` et ses `Et` | Résultat attendu du même pas |
| Tags `@AC_n`, `@REGLE_Rn` | Lien vers l'US (Tests / Tested By) et étiquettes |
| `Plan du scénario` et `Exemples` | Paramètres du cas de test |

La convention exacte (champ de préconditions ou premier pas) dépend du modèle de processus du projet : à aligner avec l'équipe.

## 8. Liste de contrôle avant de livrer

1. Le titre dit le comportement et son résultat.
2. Les `Étant donné` décrivent un état, pas des clics.
3. Le `Contexte` est vrai pour tous les scénarios du fichier ou de la règle.
4. Un seul `Quand`.
5. Chaque `Alors` est vérifiable : statut, valeur, message exact.
6. Chaque refus vérifie que la donnée est inchangée.
7. Chaque valeur vient de la source ou est annoncée comme valeur de test.
8. Ce que la source ne dit pas est en question, pas en scénario.
