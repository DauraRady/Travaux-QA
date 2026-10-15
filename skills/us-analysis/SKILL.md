---
name: us-analysis
description: Analyse une User Story et ses critères d'acceptation sans inventer de règle métier, puis rend un verdict de préparation (Prête, Partiellement prête, Non prête) avec les règles explicites, les ambiguïtés, les questions d'arbitrage et les pistes de test. À utiliser quand l'utilisateur colle une US, demande de relire, challenger ou préparer une US avant un affinage, un Three Amigos ou une génération de tests ("analyse cette US", "elle est testable ?", "quelles questions pour le PO ?").
---

# Analyse d'une User Story

## Objectif

Produire une revue de l'US et de ses critères d'acceptation (AC) exploitable par le Product Owner, le métier, les développeurs et la QA, sans ajouter de règle métier absente des sources.

La sortie sert d'entrée au skill `gherkin-test-generation` : les règles numérotées, les verdicts par AC et les pistes de test y sont repris tels quels.

## Principe non négociable

Ne jamais inventer, compléter ou déduire une règle métier non explicitement écrite dans l'US, ses AC ou les documents de référence fournis par l'utilisateur.

Une pratique générale, une convention UX, une hypothèse technique, un comportement habituel ou une connaissance du domaine ne devient jamais une règle sans source explicite. Si une connaissance générale aide à poser une question, elle reste une question.

## Entrées attendues

1. Texte de l'US.
2. Critères d'acceptation.
3. Facultatif : règles métier, maquettes, glossaire, documents de référence, décisions d'arbitrage.

Si les AC ne sont pas numérotés, les numéroter AC-1, AC-2… dans l'ordre du texte et le signaler. Cette numérotation sert aux tags du Gherkin.

Si l'entrée contient des données personnelles ou des données client réelles (noms, numéros, montants identifiables), le signaler avant toute analyse et proposer de les remplacer par des valeurs fictives.

## Hiérarchie des preuves

Classer chaque information utilisée :

| Rang | Source |
|---|---|
| 1 | Explicite dans l'US |
| 2 | Explicite dans un AC |
| 3 | Explicite dans une source de référence fournie |
| 4 | Décision d'arbitrage fournie et datée |

Tout élément absent de ces catégories est non spécifié.

En cas de contradiction, ne pas choisir silencieusement une version. Signaler la contradiction et citer les sources concernées.

## Méthode d'analyse

### 1. Reformulation factuelle

Restituer uniquement : acteur ou rôle, action ou capacité attendue, objet métier, résultat ou valeur attendue, déclencheur et préconditions explicitement indiqués.

Si la structure « En tant que / Je veux / Afin de » est incomplète, le signaler sans la compléter.

### 2. Extraction des règles explicites

Pour chaque règle :

| Champ | Contenu |
|---|---|
| ID | R1, R2… (stable : le Gherkin le réutilise en `@REGLE_R1`) |
| Règle | Formulation fidèle et concise, avec les termes métier exacts |
| Source | US, AC-n, document et section |
| Type | autorisation, validation, calcul, statut, affichage, données, workflow, intégration, sécurité, autre |
| Testabilité | testable, partiellement testable, non testable |

Ne pas transformer un exemple en règle générale, sauf si la source le définit explicitement comme tel.

### 3. Analyse des critères d'acceptation

Pour chaque AC :

1. Vérifier qu'il décrit un résultat observable.
2. Identifier les préconditions, données d'entrée et résultats attendus explicitement présents.
3. Signaler les termes vagues.
4. Signaler les valeurs, listes, seuils, formats, rôles ou états manquants.
5. Signaler les dépendances à un autre AC ou à une autre règle.
6. Conclure : testable, partiellement testable ou non testable.

### 4. Détection des ambiguïtés

Considérer comme ambigu ou insuffisant, notamment :

1. « approprié », « valide », « rapidement », « correctement », « si nécessaire », « selon le cas » sans définition.
2. Une liste annoncée mais non fournie.
3. Une règle conditionnelle dont une branche manque (le « sinon » n'est pas décrit).
4. Un statut initial, final ou une transition non définis.
5. Une autorisation sans rôle clairement identifié.
6. Une action réservée à un rôle ou à un état, sans ce qui arrive aux autres rôles ou aux autres états.
7. Une erreur ou un refus sans comportement attendu, ou sans texte exact du message.
8. Une donnée obligatoire sans moment d'exigibilité (à la saisie, à l'enregistrement, à la soumission).
9. Un calcul sans formule, unité, arrondi ou source.
10. Une limite sans comportement au-delà (blocage de la saisie, refus à l'enregistrement, troncature).
11. Une référence à une maquette ou à un document non fourni.
12. Une contradiction entre US, AC, règle ou source.

### 5. Couverture fonctionnelle

Analyser uniquement les dimensions justifiées par le contenu :

1. Parcours nominal.
2. Refus et erreurs explicitement décrits.
3. Limites et cas frontières explicitement définis.
4. Rôles et permissions.
5. Transitions de statut.
6. Persistance et historisation.
7. Intégrations.
8. Données obligatoires et facultatives.
9. Règles de validation.
10. Impacts sur les éléments existants.

Ne pas créer artificiellement une exigence pour remplir une rubrique.

### 6. Pistes de test

Pour chaque règle testable ou partiellement testable, indiquer la technique de conception qui s'applique et ce qu'elle produira. Ce sont des pistes, pas des scénarios.

| Signal dans la règle | Technique | Ce qu'elle produit |
|---|---|---|
| Plages, catégories de valeurs | Partitions d'équivalence | Une valeur représentative par classe valide et invalide décrite |
| Seuil, minimum, maximum, date limite | Valeurs limites | La borne et sa voisine, de chaque côté décrit par la source |
| Plusieurs conditions combinées | Table de décision | Une colonne par combinaison décrite |
| Statuts et transitions | Transitions d'état | Une transition autorisée par cas, les transitions interdites décrites |
| Droits différents selon le rôle | Matrice rôle × action | Une ligne par rôle cité |
| Erreur connue ou historique d'anomalies fourni | Estimation d'erreurs | Le cas fragile, seulement s'il est relié à une règle |

Lister aussi les données de test nécessaires : rôles, comptes, objets dans un état donné. Exemple fictif : « une demande au statut Soumise, un compte avec le rôle Valideur ».

### 7. Questions d'arbitrage

Transformer chaque blocage en question précise et neutre.

Une bonne question :

1. Cite l'élément concerné (AC-n, R-n).
2. Explique ce qui manque ou se contredit.
3. Ne suggère pas qu'une option est déjà décidée.
4. Propose si utile les choix observés dans les sources, sans en inventer.
5. Appelle une réponse vérifiable : une valeur, un texte, un état, un rôle.

Formulations types :

| Manque | Question |
|---|---|
| Refus non décrit pour un autre rôle ou état | « Que se passe-t-il si <autre rôle ou autre état> tente <action> ? » |
| Message d'erreur sans texte | « Quel est le texte exact du message affiché quand <condition> ? » |
| Limite sans comportement au-delà | « Au-delà de <limite>, la saisie est-elle bloquée, l'enregistrement refusé, ou la valeur tronquée ? » |
| Terme vague | « Quel critère mesurable définit "<terme>" dans AC-n ? » |

### 8. Verdict de préparation

| Verdict | Condition |
|---|---|
| Prête pour génération de tests | Toutes les règles nécessaires sont explicites et testables |
| Partiellement prête | Une partie est testable ; les éléments flous sont exclus des tests |
| Non prête | Les ambiguïtés empêchent de déterminer les résultats attendus essentiels |

Le verdict n'est pas une évaluation d'une personne. Il porte uniquement sur la qualité et la testabilité du contenu fourni.

## Format de sortie obligatoire

### A. Synthèse de l'US

Acteur, besoin, valeur attendue, périmètre explicite, hors périmètre explicite.

### B. Règles explicites

| ID | Règle | Source | Type | Testabilité |
|---|---|---|---|---|

### C. Revue des critères d'acceptation

| AC | Résultat observable | Éléments manquants ou flous | Statut |
|---|---|---|---|

### D. Ambiguïtés, contradictions et dépendances

Pour chaque point : identifiant, source, constat, impact sur les tests.

### E. Pistes de test et données nécessaires

| Règle | Technique | Cas à couvrir | Données nécessaires |
|---|---|---|---|

### F. Questions d'arbitrage

Liste numérotée et priorisée : bloquante, importante, amélioration. Une question bloquante empêche d'écrire le résultat attendu d'un AC.

### G. Périmètre testable

1. Testable maintenant.
2. Non testable tant que non clarifié.

### H. Verdict

Prête, Partiellement prête ou Non prête, avec justification factuelle.

## Contrôles qualité avant réponse

1. Chaque règle est rattachée à une source.
2. Aucun comportement n'a été ajouté par habitude ou supposition.
3. Les contradictions sont visibles.
4. Les AC flous ne sont pas déclarés testables.
5. Chaque action réservée à un rôle ou à un état a sa question sur les autres rôles ou états, si la source ne les décrit pas.
6. Chaque refus sans texte de message a sa question.
7. Les pistes de test ne citent que des règles de la section B.
8. Les suppositions éventuelles de l'utilisateur sont distinguées des décisions confirmées.
9. L'analyse conserve les termes métier exacts de la source.
