---
name: analyse-us
description: Analyse une User Story Azure DevOps avant d'écrire les tests. Lit l'US, ses critères d'acceptation, tous ses commentaires et le parent, puis donne les règles, un statut par critère, les contradictions et les questions pour le PO, sans rien inventer. À utiliser pour « analyse l'US », « qu'est-ce qui manque », « est-ce testable », « questions pour le PO ».
---

# Analyse d'une User Story

Une question posée avant le sprint coûte cinq minutes. Une règle inventée coûte un cycle de recette. Ce skill trouve les questions qui comptent, pas toutes les questions possibles.

## 1. Lire toutes les sources

1. Le work item avec `$expand=all` : `System.Title`, `System.Description`, `Microsoft.VSTS.Common.AcceptanceCriteria`, `System.TeamProject`, `System.AreaPath`, `System.IterationPath`, et tout champ personnalisé dont le nom contient `Acceptance` ou `Criteres`. Si aucun critère n'est trouvé, le dire.
2. Tous les commentaires, dans l'ordre. Ils contiennent souvent les réponses du PO, qui changent les résultats attendus :
   ```bash
   curl -sS -w '\n%{http_code}' -u ":$ADO_PAT" \
     "https://<organisation>.visualstudio.com/{project}/_apis/wit/workItems/{id}/comments?order=asc&api-version=7.1-preview.4"
   ```
   Si la réponse contient un `continuationToken`, lire la page suivante avec `&continuationToken=<token>`.
3. Le parent (`System.LinkTypes.Hierarchy-Reverse`) : titre et description. Les work items liés : titres seulement.
4. Les pièces jointes : lister leurs noms. Une image ou une maquette n'est pas lue : la marquer « non consultée » et ne jamais décrire son contenu.

## 2. Classer les sources

| Rang | Source |
|---|---|
| 1 | Texte actuel de l'US et de ses critères d'acceptation |
| 2 | Commentaire qui énonce une règle ou répond à une question (citer auteur et date) |
| 3 | Texte du parent |

Rien d'autre n'est une règle : ni une habitude, ni ce que font les autres applications. Si un commentaire contredit le texte actuel de l'US, ne pas choisir : écrire la contradiction et poser la question.

## 3. Analyser

1. Reformuler la règle métier en une phrase. Si c'est impossible, c'est le premier problème de l'US.
2. Numéroter les critères `AC-1`, `AC-2`… dans l'ordre du texte, et les règles `R1`, `R2`… avec leur source.
3. Chercher les trous qui visent une phrase précise de l'US :
   1. Mots flous sans définition : approprié, valide, rapidement, correctement, si nécessaire.
   2. Liste annoncée mais non fournie.
   3. Condition sans son « sinon ».
   4. Statut de départ, d'arrivée ou transition non définis.
   5. Action réservée à un rôle ou un statut, sans ce qui arrive aux autres.
   6. Refus ou erreur sans comportement attendu, ou sans texte exact du message.
   7. Champ obligatoire sans moment d'exigibilité.
   8. Calcul sans formule, unité ou arrondi.
   9. Limite sans comportement au-delà.
   10. Maquette ou document cité mais non fourni.
   11. Contradiction entre US, critère, commentaire ou parent.
4. Ne pas poser une question dont la réponse est évidente pour tout testeur (exemple : deux pays cochés dans un même filtre affichent les demandes des deux pays). Ce cas devient un test, pas une question.
5. Donner un statut à chaque critère. C'est ce statut, et non l'envie d'avancer, qui décide quels cas seront écrits :

| Statut | Quand | Effet sur les cas de test |
|---|---|---|
| Rédigeable | Comportement et résultat attendu présents dans les sources | Cas écrits, `Exécutable` |
| Valeur à trancher | Comportement clair, une valeur de sortie manque (texte, libellé, code) | Cas écrit avec la valeur proposée `[À VALIDER PO]`, état `Bloqué : Q-n` |
| Ambigu | Le comportement lui-même est indéterminé | Aucun cas, seulement la question |
| Non testable | Personne ne peut répondre oui ou non | Aucun cas, reformulation proposée |

Si la réponse du PO ne ferait que remplacer une valeur dans un cas, c'est « Valeur à trancher ». Si elle ferait réécrire le cas, c'est « Ambigu ». Dans le doute, « Ambigu ».

6. Donner un verdict : Prête (tous les critères sont rédigeables), Partiellement prête, ou Non prête (les résultats attendus essentiels ne peuvent pas être écrits).

## 4. Rédiger les questions

Chaque question cite le critère, dit ce qui manque, ne suggère pas la réponse et appelle une réponse vérifiable (une valeur, un texte, un statut, un rôle). Six questions bloquantes au plus, les plus graves d'abord.

| Trou | Modèle de question |
|---|---|
| Refus non décrit pour un autre rôle ou statut | « Que se passe-t-il si <autre rôle ou statut> tente <action> ? » |
| Message sans texte | « Quel est le texte exact du message affiché quand <condition> ? » |
| Limite sans comportement au-delà | « Au-delà de <limite>, la saisie est-elle bloquée, l'enregistrement refusé, ou la valeur tronquée ? » |
| Contradiction | « AC-n dit <x>, le commentaire de <auteur> du <date> dit <y> : lequel s'applique ? » |

Les questions qui concernent la préparation des données ou de l'environnement (dates passées, panne simulée, liste vide) vont aux développeurs, pas au PO : les séparer.

## 5. Livrable

Écrire le rapport dans `qc-reports/US-<id>.md` (ne pas écraser un fichier existant : écrire `US-<id>.nouveau.md` et le dire), avec exactement ces titres :

```
# QC agent : US <id> <titre>

## 1- Sources
| Source | Lue | Remarque |

## 2- Analyse de la fonctionnalité
Règle en une phrase, acteurs, périmètre, hors périmètre.

## 3- Règles, statut des AC et risques
Verdict : <Prête / Partiellement prête / Non prête>
| ID | Règle | Source |
| AC | Statut | Question | Raison |
Contradictions. Risques (cinq lignes au plus).

## 7- Questions ouvertes
| Q | AC | Question | Ce qui est bloqué | Source du doute |
Puis, à part : questions pour les développeurs (données, environnement).
```

Les sections 4, 5, 6, 8 et 9 sont ajoutées par le skill `redaction-gherkin`. Afficher le rapport dans le chat et proposer la suite : `/redaction-gherkin <id>`.

## Contrôle avant de livrer

1. Chaque règle cite sa source, chaque commentaire utilisé cite son auteur et sa date.
2. Aucun comportement ajouté par habitude.
3. Les contradictions sont visibles.
4. Aucun critère flou n'est déclaré rédigeable.
5. Aucune question dont la réponse est évidente.
