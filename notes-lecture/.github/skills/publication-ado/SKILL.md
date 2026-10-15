---
name: publication-ado
description: Publie dans Azure Test Plans les cas de test relus d'une US (fichier qc-reports/US-<id>.md), exactement tels qu'ils sont, après aperçu et validation explicite, ou produit un CSV à importer soi-même (mode csv). Lie chaque cas à l'US, vérifie les liens, ne crée jamais de doublon ni de plan de test. À utiliser pour « publie les cas », « crée-les dans ADO ».
---

# Publication des cas de test dans Azure DevOps

Ce skill publie le fichier relu par un humain, tel quel. Il ne réécrit, ne complète et n'ajoute aucun cas : si quelque chose doit changer, l'humain modifie le fichier ou relance `/redaction-gherkin`.

## 0. Choisir le mode

| Demande | Mode | Écrit dans Azure DevOps |
|---|---|---|
| `/publication-ado <id>` | API : sections 1 à 6 | Oui, après « oui » explicite |
| `/publication-ado <id> csv`, ou PAT sans droit d'écriture | CSV : section 7 seulement | Non |

Si un appel d'écriture répond 401 ou 403 en mode API, proposer le mode CSV au lieu de réessayer.

## 1. Construire les cas sans IA

1. Si `qc-reports/US-<id>.md` n'existe pas : STOP, « Rapport introuvable : lancer d'abord /analyse-us puis /redaction-gherkin, et relire le rapport ».
2. Lire l'US (`$expand=all`) pour `System.TeamProject`, `System.AreaPath`, `System.IterationPath`. Garder l'id comme `<usId>`.
3. Trouver la personne à qui assigner les cas, dans cet ordre : l'adresse donnée dans la demande ; sinon le trailer `Co-authored-by:` des commits de la session (`git log --format='%(trailers:key=Co-authored-by,valueonly)' | grep -oE '[^<]+@[^>]+' | grep -v noreply | head -n1`) ; sinon personne, et le dire. Ne jamais appeler `_apis/connectionData`.
4. Construire les corps de requête :
   ```bash
   python3 .github/skills/redaction-gherkin/scripts/build_tc.py build qc-reports/US-<id>.md --us <usId> \
     --out .qc-agent/US-<id> --assignee "<email>" --area "<AreaPath>" --iteration "<IterationPath>"
   ```
   Ajouter `--inclure-bloques` seulement si la demande dit « avec bloqués ».
5. Si le script signale une erreur : STOP, afficher les erreurs, ne rien publier. Ne jamais construire le XML des étapes à la main.
6. Lire `.qc-agent/US-<id>/manifest.json` : un fichier par cas, ou la raison pour laquelle il est écarté.

Ce que le script produit pour chaque cas :

| Rapport | Cas de test ADO |
|---|---|
| Étant donné et ses Et | Pas 1 : action = les préconditions, résultat attendu vide |
| Quand | Pas 2 : action |
| Alors et ses Et | Pas 2 : résultat attendu, une ligne chacun, jamais un pas sans action |
| `<param>` d'un Plan du scénario | `@param`, valeurs dans la grille Parameter values |
| AC, famille, US | Tags `QC-agent; US-<id>; AC-n; <Famille>` |

## 2. Trouver le plan et la suite

1. Plan : `plan <id>` dans la demande, sinon le plan par défaut de l'agent. `GET .../_apis/testplan/plans/<planId>?api-version=7.1`. En cas d'échec : STOP. Ne jamais créer de plan.
2. Suite : `suite <id>` dans la demande (suite statique), sinon la suite basée sur l'exigence de l'US : lister `GET .../_apis/testplan/Plans/<planId>/suites?api-version=7.1` (suivre l'en-tête `x-ms-continuationtoken`) et chercher `suiteType` = `requirementTestSuite` avec `requirementId` = `<usId>`. Si elle n'existe pas, elle sera créée sous la suite racine du plan.

## 3. Écarter les doublons

Lire l'US avec `$expand=relations`, récupérer les cas déjà liés (`Microsoft.VSTS.Common.TestedBy-Forward`) et leurs titres (`GET .../_apis/wit/workitems?ids=<ids>&fields=System.Title&api-version=7.1`). Un cas du manifeste dont le titre existe déjà n'est pas recréé : « déjà publié : <id> ».

## 4. Aperçu, puis validation

Afficher, sans rien écrire :
1. Le plan et la suite (existante ou à créer).
2. La liste des cas à créer (ID, titre, priorité).
3. Les cas écartés : bloqués avec leur question, déjà publiés avec leur id.
4. La personne assignée.

Puis demander : « Je crée ces <n> cas dans Azure DevOps ? ». Continuer seulement sur un « oui » explicite.

## 5. Créer, lier, vérifier

1. Créer la suite si besoin, corps dans un fichier :
   `{"suiteType":"requirementTestSuite","name":"<usId> : <titre>","requirementId":<usId>,"parentSuite":{"id":<rootSuiteId>}}`
   envoyé en POST sur `.../_apis/testplan/Plans/<planId>/suites?api-version=7.1`.
2. Pour chaque cas :
   ```bash
   curl -sS -w '\n%{http_code}' -u ":$ADO_PAT" -H "Content-Type: application/json-patch+json" \
     --data-binary @.qc-agent/US-<id>/tc-01.json \
     "https://<organisation>.visualstudio.com/{project}/_apis/wit/workitems/\$Test%20Case?api-version=7.1"
   ```
   Erreur 400 sur l'assigné : reconstruire avec `--assignee ""` et réessayer une fois. Erreur 400 sur la zone ou l'itération : reconstruire sans `--area` ni `--iteration` et réessayer une fois. Le signaler.
3. Lier chaque cas à l'US, un appel par cas :
   ```bash
   curl -sS -X PATCH -w '\n%{http_code}' -u ":$ADO_PAT" -H "Content-Type: application/json-patch+json" \
     -d '[{"op":"add","path":"/relations/-","value":{"rel":"Microsoft.VSTS.Common.TestedBy-Reverse","url":"https://<organisation>.visualstudio.com/_apis/wit/workItems/<usId>","attributes":{"comment":"Cree par QC agent"}}}]' \
     "https://<organisation>.visualstudio.com/{project}/_apis/wit/workitems/<testCaseId>?api-version=7.1"
   ```

---
⛔ CONTRÔLE — liens
OBLIGATOIRE : relire l'US avec `$expand=relations` et trouver une relation `Microsoft.VSTS.Common.TestedBy-Forward` vers chaque cas créé.
SINON : relancer le lien une fois pour chaque cas manquant (un 400 « le lien existe déjà » compte comme un succès). S'il manque encore : « Lien TC <id> -> US <usId> non créé : HTTP <code> », et continuer.
---

4. Suite basée sur l'exigence : les cas liés y apparaissent seuls. Vérifier avec `GET .../_apis/testplan/Plans/<planId>/Suites/<suiteId>/TestCase?api-version=7.1`. Suite statique : ajouter les cas avec `POST .../_apis/testplan/Plans/<planId>/Suites/<suiteId>/TestCase?api-version=7.1`, corps `[{"workItem":{"id":<id>}}]` dans un fichier.
5. Si un cas a des paramètres, le relire et vérifier que `Microsoft.VSTS.TCM.Parameters` et `Microsoft.VSTS.TCM.LocalDataSource` sont présents. Demander à l'utilisateur d'ouvrir ce cas une fois pour vérifier la grille.

## 6. Compte rendu

1. Plan et suite (nom, id, créée ou existante).
2. Tableau des cas créés : id, titre, lien, présence dans la suite.
3. Cas non publiés : bloqués, déjà publiés, en échec avec le code HTTP.
4. Personne assignée, ou « non assigné » et pourquoi.
5. Dernière ligne : « Publication terminée dans Azure DevOps. » seulement si tous les cas créés sont liés. Sinon : « Publication partielle : voir les erreurs ci-dessus. »

## 7. Mode CSV (aucune écriture par l'API)

1. Même point de départ que la section 1, étapes 1 et 2 (rapport relu, lecture de l'US pour `System.AreaPath`). Sans accès en lecture, demander l'Area Path à l'utilisateur.
2. Construire le fichier :
   ```bash
   python3 .github/skills/redaction-gherkin/scripts/build_tc.py csv qc-reports/US-<id>.md --us <usId> \
     --out qc-reports/US-<id>-import.csv --area "<AreaPath>" --assignee "<email>"
   ```
   Erreur du script : STOP, afficher les erreurs. Ajouter `--inclure-bloques` seulement si la demande dit « avec bloqués ».
3. Ce que contient le fichier : une ligne par cas (titre, Area Path, état `Design`, priorité, tags), puis une ligne par pas (pas 1 : Étant donné ; pas 2 : Quand, et Alors en résultat attendu). Un `Plan du scénario` devient un cas par ligne d'Exemples, car l'import CSV ne gère pas les paramètres. Titre limité à 128 caractères.
4. Compte rendu à l'utilisateur, puis STOP :
   1. Chemin du fichier et nombre de cas, cas bloqués non exportés.
   2. Import : Test Plans, plan, suite de l'US, « Import test cases from CSV », vérifier la correspondance des colonnes, Import.
   3. Importer dans la suite basée sur l'exigence de l'US relie les cas à l'US ; dans une suite statique, faire le lien à la main. À vérifier sur le premier import.
   4. Réimporter un cas avec son ID remplace tous ses pas : pour corriger après import, modifier dans Azure DevOps, pas en réimportant.

