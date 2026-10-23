# Estimation de la recette QA, sprints 1 à 5

Mise à jour le 23/10/2026.

## Où en est la recette

| Sprint | US | Conception des cas | Exécution |
|---|---|---|---|
| Sprints 1 et 2 | 8 | Faite (43 cas) | À faire |
| Sprint 3 | 10 | À faire | À faire |
| Sprints 4 et 5 | À confirmer | À faire | À faire |

L'exécution est bloquée : pas d'accès à la préprod, pas de comptes de test, pas d'environnement d'intégration (ITG).

## Hypothèses

1. Ratio constaté sur les sprints 1 et 2 : 43 cas pour 8 US, soit 5 à 6 cas par US.
2. Sprints 4 et 5 : 10 US par sprint, comme au sprint 3. À remplacer dès que le nombre réel est connu.
3. Conception : environ 10 cas par jour, analyse de l'US et questions au PO comprises.
4. Exécution : 12 à 15 cas par jour, preuves dans Azure Test Plans comprises.
5. Retests et suivi des anomalies : environ 25 % du temps d'exécution (application jeune, champs ajoutés à chaque sprint).
6. Pas de non-régression sur un existant (nouvelles fonctionnalités), mais une repasse rapide des cas critiques après chaque nouvelle livraison.

Repère pour recalculer : environ 0,5 j de conception et 0,6 j d'exécution, retests et bilan par US, soit 1,1 j par US.

## Phase 1 : rattraper les sprints 1 à 3

| Lot | Conception | Exécution | Retests et anomalies | Bilan | Total |
|---|---|---|---|---|---|
| Sprints 1 et 2 (43 cas) | Faite, relecture 0,5 j | 3 à 3,5 j | 1 j | 0,5 j | 5 à 5,5 j |
| Sprint 3 (environ 55 cas) | 5,5 à 6 j | 4 à 4,5 j | 1 à 1,5 j | 0,5 j | 11 à 12,5 j |
| Préparation (accès, comptes, données) | | | | | 1 à 2 j |
| Total phase 1 | | | | | 17 à 20 j, soit environ 4 semaines |

La conception du sprint 3 (environ 6 j) peut avancer dès maintenant. Les 11 à 14 j d'exécution, de retests et de bilan ne commencent qu'à l'obtention de l'accès à la préprod et des comptes de test.

## Phase 2 : sprints 4 et 5

| Lot | Conception | Exécution | Retests et anomalies | Bilan | Total |
|---|---|---|---|---|---|
| Sprint 4 (10 US supposées, environ 55 cas) | 5 à 6 j | 4 à 4,5 j | 1 à 1,5 j | 0,5 j | 10,5 à 12,5 j |
| Sprint 5 (10 US supposées, environ 55 cas) | 5 à 6 j | 4 à 4,5 j | 1 à 1,5 j | 0,5 j | 10,5 à 12,5 j |
| Total phase 2 | | | | | 21 à 25 j, soit environ 5 semaines |

## Total sprints 1 à 5

38 à 45 jours, soit 8 à 9 semaines pour une seule personne.

## Points d'attention

1. Un sprint de 10 US demande 10,5 à 12,5 j de QA alors qu'il dure 10 j : le retard grandit à chaque sprint sans priorisation ou renfort.
2. Chaque jour sans accès à la préprod décale d'autant la fin de l'exécution.
3. Le POC d'automatisation prévu vers le sprint 6 ou 7 s'ajoute à cette charge.
4. Le gain possible de l'agent QA sur la conception n'est pas compté tant qu'il n'a pas été mesuré sur de vraies US.

## Décisions à demander

1. Une date d'accès à la préprod et aux comptes de test par rôle.
2. Une priorisation par le risque : droits par rôle, statuts et champs obligatoires exécutés en entier ; libellés et ergonomie couverts par une session exploratoire limitée dans le temps.
3. Un arbitrage entre renfort, périmètre réduit ou POC d'automatisation décalé.
