# Estimation de la recette QA, sprints 1 à 5

Mise à jour le 27/10/2026 (première version le 23/10/2026).

## Où en est la recette

| Sprint | US | Conception des cas | Exécution |
|---|---|---|---|
| Sprints 1 et 2 | 8 | Faite (43 cas annoncés, 38 dans ce dépôt) | À faire |
| Sprint 3 | 10 | Faite (65 scénarios, 139 exécutions) | À faire |
| Sprints 4 et 5 | À confirmer | À faire | À faire |

Au 27/10/2026, la préprod est accessible. Restent à confirmer avant d'exécuter : un compte par rôle (Admin, SuperAdmin, User), les données de test réelles (entités neuves, engagements libres), et les demandes au statut « Validé » à injecter par un développeur. Il n'y a toujours pas d'environnement d'intégration (ITG).

Écart à éclaircir : les sprints 1 et 2 annoncent 43 cas, ce dépôt en contient 38 (création 9, liste 15, filtres 14). La side panel Discovery et les groupes de sécurité n'ont pas de fichier ici. Hypothèse : les 5 cas manquants les couvrent et sont ailleurs, par exemple directement dans Azure Test Plans.

## Hypothèses

1. Ratio constaté sur les sprints 1 et 2 : 43 cas pour 8 US, soit 5 à 6 cas par US.
2. Ratio constaté au sprint 3 : 65 scénarios pour 10 US, soit 139 exécutions parce que chaque scénario est joué pour chaque profil habilité.
3. Sprints 4 et 5 : 10 US par sprint, comme au sprint 3. À remplacer dès que le nombre réel est connu.
4. Conception : environ 10 cas par jour, analyse de l'US et questions au PO comprises.
5. Exécution : 12 à 15 exécutions par jour, preuves dans Azure Test Plans comprises.
6. Retests et suivi des anomalies : environ 25 % du temps d'exécution (application jeune, champs ajoutés à chaque sprint).
7. Pas de non-régression sur un existant (nouvelles fonctionnalités), mais une repasse rapide des cas critiques après chaque nouvelle livraison.

## Phase 1 : exécuter les sprints 1 à 3 (reste à faire)

| Lot | Exécution | Retests et anomalies | Bilan | Total |
|---|---|---|---|---|
| Préparation (comptes, données, demandes injectées) | | | | 1 à 2 j |
| Sprints 1 et 2 (38 cas, plus les 5 à retrouver) | 3 à 3,5 j | 1 j | 0,5 j | 4,5 à 5 j |
| Sprint 3, première passe (71 exécutions) | 5 à 6 j | 1 à 1,5 j | 0,5 j | 6,5 à 8 j |
| Total phase 1 | | | | 12 à 15 j, soit environ 3 semaines |

La première passe du sprint 3 joue chaque scénario avec un seul profil habilité (Admin), plus les cas du User et les cas réservés au SuperAdmin. Le second profil habilité (68 exécutions, 4,5 à 5,5 j) se joue ensuite là où le rôle peut changer le résultat : droits, contrôles serveur, formulaire validé. Le détail est dans `doc/ordre-execution-sprints-1-a-3.md`.

## Phase 2 : sprints 4 et 5

| Lot | Conception | Exécution | Retests et anomalies | Bilan | Total |
|---|---|---|---|---|---|
| Sprint 4 (10 US supposées, environ 55 cas) | 5 à 6 j | 4 à 4,5 j | 1 à 1,5 j | 0,5 j | 10,5 à 12,5 j |
| Sprint 5 (10 US supposées, environ 55 cas) | 5 à 6 j | 4 à 4,5 j | 1 à 1,5 j | 0,5 j | 10,5 à 12,5 j |
| Total phase 2 | | | | | 21 à 25 j, soit environ 5 semaines |

Ces chiffres datent d'avant la conception du sprint 3. Avec le ratio réel du sprint 3 (65 scénarios pour 10 US), la phase 2 est probablement sous-estimée d'environ 20 %.

## Points d'attention

1. Un sprint de 10 US demande plus de 10 j de QA alors qu'il dure 10 j : le retard grandit à chaque sprint sans priorisation ou renfort.
2. Chaque jour sans comptes par rôle ni données de test décale d'autant l'exécution, même avec la préprod accessible.
3. Jouer chaque scénario pour chaque profil double l'exécution. C'est justifié pour les droits, beaucoup moins pour une règle d'affichage identique pour tous les profils.
4. Le POC d'automatisation prévu vers le sprint 6 ou 7 s'ajoute à cette charge.
5. Le gain possible de l'agent QA sur la conception n'est pas compté tant qu'il n'a pas été mesuré sur de vraies US.

## Décisions à demander

1. Les comptes de test par rôle et l'injection des demandes validées, avec une date.
2. La validation de l'ordre d'exécution par le risque : droits, contrôles serveur et règles de cascade d'abord ; libellés et ergonomie en session exploratoire limitée dans le temps.
3. Un arbitrage entre renfort, périmètre réduit ou POC d'automatisation décalé.
