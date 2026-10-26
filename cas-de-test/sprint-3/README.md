# Cas de test du sprint 3 InfoCAC

Rédigés le 26/10/2026, recentrés le même jour sur la France et la Certification des comptes, avec le skill `skills/gherkin-test-generation`, contrôlés par son script (`build_tc.py check` : 0 erreur, 0 avertissement sur chaque fichier). Données fictives uniquement. La note qui explique le projet, l'exécution et les pièges est dans `doc/note-recapitulative-infocac.md`.

| Fichier | US | Scénarios | Exécutions (une par profil et par ligne) |
|---|---|---|---|
| `US-424890-numero-engagement.md` | 424890 Numéro d'engagement à la création | 16 | 36 |
| `US-controles-creation.md` | Contrôles à la création (identifiant non visible) | 2 | 6 |
| `US-426402-caracteristiques-mandat.md` | 426402 Pays, Type et Catégorie du mandat | 3 | 6 |
| `US-426235-indicateurs-DA.md` | 426235 Indicateurs DA | 2 | 4 |
| `US-426973-taxonomie-certification-france.md` | 426973 Taxonomie Certification France | 4 | 12 |
| `US-426406-AGP-categorie-entite-type-EIP.md` | 426406 AGP, catégorie d'entité, Type d'EIP | 7 | 16 |
| `US-426407-marches-cotation.md` | 426407 Marchés de cotation | 5 | 10 |
| `US-425530-recherche-entite-id.md` | 425530 Recherche par Entité ID | 3 | 6 |
| `US-422727-entete-formulaire.md` | 422727 En-tête et bouton Retour | 5 | 9 |
| `US-427092-titre-sous-titre-affectation.md` | 427092 Titre, sous-titre, affectation | 4 | 8 |
| Total | 10 US | 51 | 113 |

Périmètre testé : France uniquement, mandats de Certification des comptes uniquement. Les règles des US qui portent sur la Durabilité, le type mixte ou les autres pays sont marquées « Hors périmètre » dans la couverture et n'ont pas de scénario.

Les titres suivent la forme « action ou situation : résultat attendu », pour qu'on sache ce que vérifie un cas sans l'ouvrir. Le CSV ajoute le profil entre parenthèses.

Chaque fichier a trois sections : les scénarios, la couverture de chaque règle de l'US, et ce qui n'est pas rédigé faute de réponse du PO.

## Choix de rédaction

1. Chaque scénario dit qui est connecté, sur quel écran, avec quelles données. Les préconditions décrivent un état, pas des clics.
2. Chaque scénario est joué pour chaque profil habilité par l'US (colonne `cas` des Exemples). Le profil Utilisateur n'est rédigé nulle part au sprint 3 : le PRD le limite aux données validées, et aucune demande de test ne l'est (Q5).
3. Une règle que le PO n'a pas tranchée n'a pas de scénario : elle est listée en section 3 avec sa question.
4. Quand une US annonce un message sans en donner le texte final, le résultat est « un message d'erreur s'affiche » et le texte reste une question.

## Passage vers Azure Test Plans

```bash
python3 skills/gherkin-test-generation/scripts/build_tc.py csv cas-de-test/sprint-3/US-424890-numero-engagement.md --us 424890 --out US-424890.csv
```

Le CSV produit un cas par ligne d'Exemples (état Design, Area Path à remplir avant l'import). Les préconditions répétées deviennent des étapes partagées :

| Précondition dans le Gherkin | Étape partagée Azure Test Plans |
|---|---|
| je suis connecté avec le compte X ayant le rôle R | Se connecter : ouvrir InfoCAC, s'authentifier par SSO avec le compte, vérifier le rôle dans Paramètres |
| le formulaire de création est ouvert depuis la "Liste des demandes" | Ouvrir la Liste des demandes, cliquer sur « Nouvelle demande » |
| une demande vierge est ouverte sur la section "Description du mandat" | Créer une demande sur une entité neuve, ouvrir son formulaire, déplier la section |
| je suis sur la "Liste des demandes" | Ouvrir la Liste des demandes depuis la side panel |

Mets la liste des profils dans un paramètre partagé « Profils habilités » : un rôle qui change se modifie à un seul endroit.

## Données de test à préparer

| Donnée | Contenu | Utilisée par |
|---|---|---|
| AD-TEST-01, SA-TEST-01 | Comptes Admin (périmètre France) et SuperAdmin | Tous |
| ENT-ENG-01 à ENT-ENG-08 | Entités France neuves, sans aucune demande, une par création réussie | ENG-01, 06, 07, 13 |
| ENT-ENG-10 | Entité neuve qui ne doit jamais recevoir de demande (toutes les créations dessus doivent échouer) | ENG-02, 08, 09, 10, 14, 16 |
| ENT-ENG-11 | Entité à laquelle est rattaché l'engagement 1021003 | ENG-10, 14 |
| ENT-ENG-12 et DEM-TEST-01 | Entité avec une demande au statut « Validé » portant l'engagement 1021002 (à injecter par un développeur) | ENG-11, 12 |
| 1021001 et 1021011, 0001234 et 0001235, 1021004 et 1021014 | Engagements libres, un par profil, rattachés aux entités de leur ligne ; consommés par l'exécution | ENG-06, 07, 13 |
| 1021006 | Engagement libre rattaché à ENT-ENG-10 | ENG-08, 16 |
| 1021001 avec description, 1021002 sans description | Engagements du Référentiel Finance commençant par 1021 | ENG-03 |
| 9999999 | Numéro absent du Référentiel Finance | ENG-02, 08, 09, 10 |
| ENT-CTRL-01 à ENT-CTRL-05, BSC-TEST-01 | Entités neuves et requête déjà utilisée par DEM-TEST-01 | CTRL |
| ENT-RECH-01, ENT-RECH-02, DEM-RECH-01 à 03 | Entités et demandes réservées à la recherche ; DEM-RECH-01 au millésime 2027, DEM-RECH-02 au millésime 2026 | RECH |
| ENT-HEAD-01 « Société Test Alpha », DEM-TEST-02 | Demande en cours | HEAD |
| ENT-HEAD-99, DEM-TEST-06 | Demande sur une entité absente du référentiel | HEAD-02 |
| DEM-TEST-04 | Demande au statut « Validé » (à injecter par un développeur) | HEAD-04 |
| DEM-TEST-07 | Demande avec titre, sous-titre et « Affectée à » renseignés | TIT |

Toutes les entités sont françaises et tous les mandats de Certification des comptes. Les identifiants sont fictifs : remplace-les par les données réelles de préprod avant l'exécution, en gardant les mêmes caractéristiques.

## Questions ouvertes

Elles complètent Q1 à Q10 des sprints 1 et 2. À poser en premier : Q-19, Q-13, Q-14, Q-22 et Q5.

| # | Question | Bloque | À qui |
|---|---|---|---|
| Q5 | Le profil Utilisateur voit-il les demandes non validées ? 425530 dit oui, le PRD dit non | Lignes Utilisateur de RECH, HEAD, TIT | Risk Management |
| Q6 | L'Admin peut-il ouvrir un formulaire validé en modification ? | Ligne Admin de HEAD-04 | Risk Management |
| Q-11 | Une lettre saisie dans « Numéro d'engagement » est-elle ignorée, ou refusée avec un message ? | Message de ENG-05 | PO |
| Q-12 | Codes HTTP et contenu ProblemDetails des refus serveur | ENG-10, 12, 16 (précision) | Développeur |
| Q-13 | Engagement déjà associé : quel texte fait foi, celui de 424890 ou celui de l'US Contrôles ? | ENG-11 | PO |
| Q-14 | Quelle propriété du Référentiel Finance relie un engagement à une Entité ID ? | ENG-10, 14 | Architecte |
| Q-15 | Texte définitif du message « référentiel indisponible » ; comment simuler la panne en préprod ? | ENG-15, 16 | PO, développeur |
| Q-16 | Entité ID modifiée après le choix d'un engagement : vidage, erreur, ou contrôle à la validation ? | Non rédigé | PO |
| Q-17 | Engagement saisi avec une Entité ID inconnue : que devient le contrôle de compatibilité ? | Non rédigé | PO |
| Q-18 | L'engagement d'une demande annulée ou supprimée redevient-il disponible ? | Non rédigé | PO |
| Q-19 | Entité ID inconnue acceptée et plusieurs demandes par entité (US Contrôles), contre blocage (TC06, TC07) ; requête BSC facultative contre obligatoire (TC05) | Non rédigé | PO |
| Q-21 | Quand les champs obligatoires du formulaire sont-ils contrôlés, et avec quel message ? | Non rédigé | PO |
| Q-22 | Que veut dire Reprise ? Comment s'articulent la Nature (création), la Reprise Oui/Non et la Catégorie (formulaire) ? | DM-02, TAX-01 | PO |
| Q-23 | Valeur des indicateurs DA tant qu'aucun type n'est choisi | Non rédigé | PO |
| Q-26 | 426235 : « le système enregistre » contre « pas de sauvegarde » ; quelle US portera l'envoi vers DA ? | Non rédigé | PO |
| Q-27 | En quittant EIP, l'AGP garde-t-il Non ? | Non rédigé | PO |
| Q-28 | RG-EIP-03 et étapes 5 et 6 manquantes dans 426406 | Non rédigé | PO |
| Q-29 | Que signifie AGP ? | Compréhension | PO |
| Q-30 | « Non coté » deux fois dans la liste des marchés ; « Autre » répétable ? | Non rédigé | PO |
| Q-31 | Contrôles de cohérence entre marchés et qualification EIP | Non rédigé | PO, Risk Management |
| Q-32 | Recherche exacte, partielle ou par début ; casse ; message sans résultat | Non rédigé | PO |
| Q-35 | Nom affiché dans l'en-tête pour une entité inconnue du référentiel | Non rédigé | PO |
| Q-36 | Le bouton Retour suit-il la page précédente ou le statut de la demande ? | Non rédigé | PO |
| Q-37 | Origine du titre et du sous-titre ; mandat sans sous-titre | Non rédigé | PO |
| Q-38 | L'unicité des marchés de cotation est-elle contrôlée aussi côté serveur ? | Non rédigé | Développeur |
| Q-40 | Le périmètre est France et Certification des comptes : que doivent proposer les listes Pays et Type de mandat, alors que 426402 décrit 18 pays et 3 types ? L'US sera-t-elle mise à jour ? | DM-01 | PO |
