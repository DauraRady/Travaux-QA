---
name: redaction-gherkin
description: Rédige les cas de test manuels d'une US en Gherkin français (nominaux, négatifs, limites) à partir de l'analyse, avec données fictives concrètes, un seul Quand, des résultats vérifiables, puis les contrôle avec un script sans IA. À utiliser pour « écris les cas de test », « génère le Gherkin », « cas nominaux, négatifs et limites ».
---

# Rédaction des cas de test en Gherkin

Un cas n'est bon que s'il vérifie une règle précise, avec des données précises, et qu'il peut échouer. La présence de Étant donné, Quand et Alors ne prouve rien.

## 0. Point de départ obligatoire

1. Lire `qc-reports/US-<id>.md`. S'il n'existe pas, appliquer d'abord le skill `analyse-us`.
2. Écrire des cas seulement pour les critères « Rédigeable » et « Valeur à trancher ». Jamais pour « Ambigu » ou « Non testable ».
3. Lire `references/guide-ecriture-gherkin.md` à la première utilisation de la session.

## 1. Choisir la technique

| Forme de la règle | Technique | Ce qu'on écrit | Limite |
|---|---|---|---|
| Catégories de valeurs | Partitions d'équivalence | Une valeur par classe décrite | Pas de classe invalide si la source ne dit pas qu'elle est refusée |
| Seuil, minimum, maximum, délai | Valeurs limites | La borne, et la valeur juste au-delà si le comportement au-delà est décrit | Sans comportement au-delà : la borne seule, et une question |
| Conditions combinées | Table de décision | Un cas ou une ligne par combinaison décrite | Pas de combinaison sans résultat écrit |
| Statuts et transitions | Transitions d'état | Un cas par transition autorisée, un par transition interdite décrite | Les statuts non cités deviennent des questions |
| Droits selon le rôle | Matrice rôle × action | Une ligne par rôle cité | Les rôles non cités deviennent des questions |

## 2. Couvrir

1. Nominal : chaque critère rédigeable a son cas nominal.
2. Négatif : seulement si la source décrit un refus, une interdiction, une erreur ou une exclusion. Ne jamais supposer qu'une valeur non mentionnée est invalide.
3. Limite : dès qu'un critère contient un nombre, une date, une durée, un plafond. Exemple : « plus de 60 jours » donne un cas à 60 jours (pas de changement) et un cas à 61 jours (changement).
4. Bord (double clic, liste vide, panne) : seulement si la source décrit le comportement attendu. Ne jamais inventer longueurs, caractères spéciaux ou coupures réseau.
5. Rôles : tester ce que dit le critère (« le bouton n'est pas affiché »). Pas de test par URL directe ou API si la source ne décrit pas la réponse.

## 3. Pas de doublon

1. Un cas par résultat attendu distinct. Deux valeurs qui donnent le même résultat sont le même cas.
2. Une valeur de champ qui ne change pas le comportement décrit ne justifie pas un cas (exemple : Reprise Oui et Reprise Non menant à la même création).
3. Un `Plan du scénario` seulement si les étapes sont identiques, le résultat a la même forme, et chaque ligne est une classe nommée par les sources (exemple : les trois rôles autorisés).
4. Quand le rôle ne change pas le résultat, un seul compte suffit (Admin). Un cas dédié prouve que chaque rôle autorisé a accès.

## 4. Écrire

| Mot-clé | Règle |
|---|---|
| Étant donné / Et que | Un état, pas des clics. Rôle et compte nommés. Chaque donnée avec un identifiant fictif entre guillemets (`la demande "DEM-TEST-03" au statut "En cours"`). Seules les valeurs qui influencent le résultat. Chaque cas a ses propres données |
| Quand | Une seule action, jamais suivie de Et ou Mais |
| Alors / Et | Observable sans interprétation : statut exact, message exact copié de la source, valeur, élément présent ou absent. Interdits hors guillemets : correctement, bien, normalement, avec succès, comme prévu, etc., ou |
| Refus | Deux vérifications : le refus (message, élément absent) ET la donnée inchangée (`aucune nouvelle demande n'est créée`, `est toujours au statut "En cours"`) |
| Valeur en attente | `[À VALIDER PO]` dans le texte, état `Bloqué : Q-n` |
| Taille | Huit étapes au plus |
| Dates | Une date relative (« créée il y a 61 jours ») plutôt qu'une date fixe qui changera le statut avec le temps |

Le même fait s'écrit toujours avec la même phrase dans tous les cas (connexion, statut d'une demande, vérification d'un message).

Si l'environnement de recette contient d'autres données, écrire les résultats ainsi : les données attendues sont présentes, les données exclues sont absentes, chaque ligne affichée respecte la règle.

## 5. Format de chaque cas (le script le lit)

````
### TC-01 - <titre : le comportement et son résultat>
| AC | Règle | Famille | Priorité | État |
|---|---|---|---|---|
| AC-1, AC-3 | R1 | Nominal | 1 | Exécutable |

Technique : <technique du tableau>
Détecte : <l'anomalie du produit qui ferait échouer ce cas>

```gherkin
Scénario: <titre>
  Étant donné que ...
  Et que ...
  Quand ...
  Alors ...
  Et ...
```
````

Famille : Nominal, Négatif, Limite ou Bord. Priorité : 1 (flux principal, refus qui protège droits ou données), 2 (autres refus décrits, variantes principales), 3 (limites, cas secondaires), 4 (affichage). Au plus 25 % en priorité 1, 60 % en priorités 1 et 2. Pour un `Plan du scénario`, la première colonne des Exemples peut s'appeler `cas` (pourquoi la ligne existe) ; les autres colonnes portent le nom des paramètres, en minuscules sans accent ni espace.

Si tu ne sais pas écrire la ligne `Détecte :`, le cas ne teste rien : le supprimer.

## 6. Compléter le rapport

Ajouter à `qc-reports/US-<id>.md` :

```
## 4- Cas de test
| ID | Titre | AC | Famille | Priorité | État |
puis un bloc par cas (format ci-dessus)

## 5- Cas limites
| Situation | Décision |   → TC-xx, → Q-n, ou Non retenu : raison

## 6- Autres niveaux de test
| Vérification | Niveau (API, UI automatisée) | Pourquoi |

## 8- Couverture
| AC | Cas | Couverture | Raison |   COMPLÈTE, PARTIELLE ou AUCUNE, les manques en premier
Puis le décompte : Nominal, Négatif, Limite, Bord, Exécutable, Bloqué.

## 9- Publication
Résultat du contrôle, avertissements gardés avec leur raison, valeurs de test choisies.
Dernière ligne : « Après relecture du fichier, publier avec : /publication-ado <id> »
```

## 7. Contrôler sans IA

```bash
python3 .github/skills/redaction-gherkin/scripts/build_tc.py check qc-reports/US-<id>.md
```

Corriger chaque `ERREUR` et relancer jusqu'à 0 erreur. Chaque `AVERTISSEMENT` est corrigé ou justifié en une ligne en section 9. Sans Python, appliquer à la main la liste ci-dessous et l'écrire en section 9.

## Contrôle avant de livrer

1. Un seul Quand et au moins un Alors par cas.
2. Aucun Étant donné vague, chacun avec une valeur entre guillemets.
3. Chaque message copié de la source, ou sa question posée.
4. Chaque refus vérifie la donnée inchangée.
5. Aucun doublon de résultat.
6. Aucune valeur en attente sans `[À VALIDER PO]` et `Bloqué : Q-n`.
7. Chaque situation de la section 5 a une décision.
8. Aucun cas pour un critère Ambigu ou Non testable.
