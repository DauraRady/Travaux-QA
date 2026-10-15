---
name: gherkin-test-generation
description: Génère des scénarios Gherkin en français à partir d'une User Story et de ses critères d'acceptation, sans inventer de règle, de valeur ou de message, avec les techniques de conception ISTQB, une traçabilité par tags et la liste des éléments non couverts. À utiliser quand l'utilisateur colle une US ou une analyse d'US et demande des scénarios, des cas de test, du Gherkin, du BDD ou des critères au format Étant donné / Quand / Alors.
---

# Génération de tests Gherkin à partir d'une US

## Objectif

Produire des scénarios Gherkin traçables, lisibles par le métier et exécutables par un humain ou un outil, qui couvrent :

1. Les tests positifs, lorsque la source décrit un comportement attendu.
2. Les tests négatifs, uniquement lorsque la source décrit un refus, une interdiction ou un échec.
3. Les edge cases, uniquement lorsque la limite ou le cas frontière est défini par la source.

Les règles d'écriture détaillées et un exemple complet commenté sont dans `references/guide-ecriture-gherkin.md`. Le lire avant la première génération de la session.

## Règle fondamentale

Ne jamais inventer une règle métier, une valeur, une liste, une permission, un message, un seuil, un format, une transition, une précondition ou un résultat attendu.

Si un AC ou une règle est flou, incomplet, contradictoire ou non testable :

1. Ne générer aucun scénario basé sur la partie indéterminée.
2. L'ajouter à la section « Éléments non couverts ».
3. Expliquer précisément pourquoi aucun test n'a été produit.
4. Formuler une question d'arbitrage.

Il est permis de générer les scénarios de la partie claire d'un AC partiellement testable, à condition que les étapes n'utilisent pas la partie floue.

## Entrées attendues

1. US complète.
2. Critères d'acceptation.
3. Facultatif : règles métier, exemples, tables de décision, maquettes, sources de référence, sortie du skill `us-analysis`.

Si l'entrée contient des données personnelles ou client réelles, le signaler et utiliser des valeurs fictives dans les scénarios.

## Pré-analyse obligatoire

Si la sortie de `us-analysis` est fournie, reprendre ses règles (R1, R2…), ses verdicts par AC et ses pistes de test, sans les refaire.

Sinon, avant d'écrire du Gherkin :

1. Extraire les règles explicites et les numéroter R1, R2…
2. Associer chaque règle à sa source.
3. Qualifier chaque règle : testable, partiellement testable, non testable.
4. Identifier les ambiguïtés et contradictions.
5. Exclure les parties non testables.

Si l'US est jugée Non prête, ne produire que les éléments non couverts et les questions.

## Politique de génération par catégorie

### Tests positifs

Générer un test positif lorsqu'une source définit explicitement une entrée ou action autorisée, les préconditions nécessaires et un résultat observable attendu.

### Tests négatifs

Générer un test négatif seulement si la source définit explicitement au moins l'un de ces éléments : une entrée interdite ou invalide, une action non autorisée, une précondition manquante qui doit entraîner un refus, un contrôle bloquant, le comportement attendu en échec.

Ne pas supposer qu'une donnée non mentionnée est invalide.

Si une action est réservée à un rôle ou à un état, mais que la source ne dit pas ce qui arrive aux autres rôles ou aux autres états :

1. Ne pas générer le test négatif.
2. L'inscrire dans « Éléments non couverts » avec la raison « refus non décrit par la source ».
3. Formuler la question : « Que se passe-t-il si <autre rôle ou autre état> tente <action> ? »

Messages d'erreur : ne jamais inventer le texte. Si la source donne le texte exact, le reprendre mot pour mot entre guillemets. Si elle exige seulement « une erreur » ou « un refus », écrire l'étape avec cette formulation générique (« la validation est refusée ») et ajouter dans « Éléments non couverts » la question du texte exact.

Quand la source décrit un refus d'enregistrement ou de modification, ajouter un « Et » qui vérifie que la donnée concernée est inchangée. C'est la conséquence directe du refus, pas une règle ajoutée : sans cette vérification, un refus affiché après une sauvegarde partielle passerait le test.

### Edge cases

Générer un edge case uniquement si la source fournit une limite ou un cas frontière exploitable : valeur minimale ou maximale, borne temporelle, nombre maximal d'éléments, état précédent ou suivant explicitement défini, champ facultatif explicitement défini, liste vide explicitement supportée, changement de contexte explicitement décrit, cas exceptionnel explicitement autorisé ou bloqué.

Ne pas créer arbitrairement des longueurs de chaîne, tailles de fichier, dates extrêmes, valeurs nulles, doublons, caractères spéciaux ou problèmes réseau si aucune source ne définit leur traitement.

## Techniques de conception

Choisir la technique d'après la forme de la règle, puis l'appliquer seulement aux valeurs que la source définit.

| Forme de la règle | Technique | Ce qu'on génère | Limite à respecter |
|---|---|---|---|
| Catégories ou plages de valeurs | Partitions d'équivalence | Une valeur représentative par classe décrite | Pas de classe invalide si la source ne dit pas qu'elle est refusée |
| Seuil, minimum, maximum, date limite | Valeurs limites | La borne, et la valeur juste au-delà si le comportement au-delà est décrit | Sans comportement au-delà : seulement la borne, et une question |
| Plusieurs conditions qui se combinent | Table de décision | Une ligne d'Exemples par combinaison décrite | Pas de combinaison dont le résultat n'est pas écrit |
| Statuts et transitions | Transitions d'état | Un scénario par transition autorisée, un par transition interdite décrite | Les états non cités vont en questions |
| Droits selon le rôle | Matrice rôle × action | Une ligne par rôle cité avec son résultat | Les rôles non cités vont en questions |
| Anomalie connue fournie | Estimation d'erreurs | Le cas fragile, relié à une règle | Jamais un cas sans règle source |

Indiquer la technique en commentaire au-dessus du scénario : `# Technique : valeurs limites (borne haute de R3)`.

## Écrire un scénario

1. Un comportement par scénario : un seul `Quand`. Deux actions à vérifier font deux scénarios.
2. `Étant donné` décrit l'état du système avant l'action (les préconditions) : qui est connecté, dans quel état sont les données. C'est un état, pas un parcours de clics.
3. `Contexte` regroupe seulement les `Étant donné` communs à tous les scénarios de la fonctionnalité (ou de la `Règle` où il est placé). Si un seul scénario n'en a pas besoin, l'étape sort du `Contexte`. Au plus trois ou quatre lignes.
4. `Quand` décrit l'action métier testée, au présent, à la première personne ou avec l'acteur nommé, de façon constante dans le fichier.
5. `Alors` décrit un résultat observable et vérifiable : un statut, une valeur, un message exact, la présence ou l'absence d'un élément. Jamais « correctement », « normalement », « comme prévu ».
6. `Et` et `Mais` prolongent le mot-clé précédent. Pas de `Et` après `Quand` pour ajouter une seconde action.
7. Style déclaratif : décrire le comportement métier, pas l'interface (« je valide la demande », pas « je clique sur le bouton Valider »), sauf si l'US impose ces détails.
8. Titre du scénario : le comportement et son résultat, compréhensible sans lire les étapes. Jamais « Test 1 » ou « Cas nominal ».
9. `Règle:` regroupe les scénarios d'une même règle métier quand la fonctionnalité en a plusieurs. Une `Règle` par R-n ou par AC.

## Jeux de données

1. Chaque valeur qui influence le résultat est écrite explicitement dans l'étape, entre guillemets : `la demande "DEM-001" est au statut "Soumise"`.
2. Ne mettre dans les étapes que les données qui changent le résultat. Les autres restent implicites.
3. Valeurs fictives, reconnaissables comme telles (DEM-001, Valideur01). Aucune donnée réelle.
4. Une donnée par scénario, pour que les scénarios restent indépendants : DEM-001 pour l'un, DEM-002 pour l'autre.
5. Les valeurs viennent de la source. Si la source ne donne pas de valeur et qu'une valeur quelconque de la classe convient, la choisir et l'annoncer dans le résumé comme valeur de test, pas comme règle.
6. Les états de départ (statuts, rôles) sont posés dans `Étant donné`, jamais obtenus en déroulant un autre scénario.

## Plan du scénario et Exemples

Utiliser `Plan du scénario` uniquement si plusieurs jeux de données partagent exactement la même règle et les mêmes étapes, et si les valeurs proviennent des sources ou de l'utilisateur. Si les résultats diffèrent par leur forme (accepté d'un côté, message d'erreur de l'autre), faire des scénarios séparés.

Écriture des Exemples :

1. Une première colonne `cas` qui dit pourquoi la ligne existe : « borne haute », « champ facultatif vide ».
2. Une ligne par partition ou par limite, pas de lignes redondantes dans la même classe.
3. Les noms de colonnes reprennent les paramètres `<...>` du plan, en minuscules, sans espace.
4. Pas de calcul dans le tableau : le résultat attendu est écrit en clair, repris de la source.

## Traçabilité

Chaque scénario porte des tags :

1. `@US_<identifiant>` sur la fonctionnalité, si l'identifiant existe.
2. `@AC_<n>` pour l'AC couvert.
3. `@REGLE_<Rn>` pour la règle analysée.
4. Un type parmi `@positif`, `@negatif`, `@edge_case`.

Ajouter `@priorite_haute`, `@priorite_moyenne` ou `@priorite_basse` uniquement si une priorité est fournie par l'utilisateur ou la source. Sinon, ne pas inventer de priorité.

## Format de sortie obligatoire

### 1. Résumé de couverture

| Source | Règle/AC | Statut | Scénarios générés | Technique | Motif |
|---|---|---|---|---|---|

### 2. Scénarios Gherkin

Un seul bloc par fonctionnalité, en français :

```gherkin
# language: fr
@US_x
Fonctionnalité: <capacité métier>
  En tant que <rôle>
  Je veux <action>
  Afin de <valeur>

  Contexte:
    Étant donné que <précondition commune à tous les scénarios>

  Règle: <R1 en une phrase>

    # Technique : <technique>
    @AC_1 @REGLE_R1 @positif
    Scénario: <comportement et résultat>
      Étant donné que <état initial>
      Quand <action unique>
      Alors <résultat observable>
```

### 3. Éléments non couverts

Pour chaque élément flou, non testable ou non décrit : référence de l'AC ou de la règle, texte ou reformulation fidèle, raison de non-génération, information manquante, question d'arbitrage.

### 4. Contrôle de couverture

Présenter séparément : nombre de scénarios positifs, négatifs, edge cases ; AC et règles entièrement, partiellement et non couverts. Les nombres sont calculés à partir des scénarios effectivement produits.

## Exemples de traitement

AC flou : « Le système affiche rapidement les résultats pertinents. »

1. Aucun test de performance, car « rapidement » n'a pas de seuil.
2. Aucun test de pertinence, car les critères de classement ne sont pas définis.
3. Signalement dans « Éléments non couverts ».
4. Questions : « Quel est le temps de réponse maximal attendu ? » et « Quelles règles déterminent qu'un résultat est pertinent ? »

Couverture partielle : « Un Admin peut enregistrer un formulaire incomplet et les dates invalides sont refusées. »

Si la source définit l'enregistrement incomplet mais pas ce qu'est une date invalide :

1. Générer le test positif d'enregistrement incomplet.
2. Ne générer aucun test sur les dates invalides.
3. Signaler la définition manquante des formats et plages de dates.
4. Signaler aussi que les autres rôles ne sont pas décrits : « Que se passe-t-il si un utilisateur non Admin tente d'enregistrer un formulaire incomplet ? »

## Contrôles qualité avant réponse

1. Chaque scénario est relié à une règle et à une source testable.
2. Chaque scénario a un seul `Quand`.
3. Aucun `Étant donné` ne décrit un parcours de clics.
4. Le `Contexte` ne contient que des étapes utiles à tous les scénarios.
5. Aucun résultat attendu n'est implicite ni vague.
6. Aucun exemple n'introduit une nouvelle règle métier.
7. Aucun texte de message n'est inventé.
8. Chaque refus d'enregistrement ou de modification vérifie que la donnée est inchangée.
9. Les scénarios négatifs ne testent que des interdictions ou des échecs explicitement définis.
10. Les edge cases correspondent à des bornes ou exceptions explicitement documentées.
11. Chaque AC sans test négatif ni edge case a sa ligne dans « Éléments non couverts », avec la raison.
12. Les éléments exclus et les questions d'arbitrage sont visibles.
