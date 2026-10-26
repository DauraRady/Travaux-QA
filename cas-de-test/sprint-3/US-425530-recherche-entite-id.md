# US 425530 : rechercher mes demandes via le numéro Entité ID

Sources : US 425530 (captures du 23/10/2026 ; ses 5 commentaires ne sont pas visibles). Données fictives uniquement.

Profils de l'US : Super Admin, Admin et Utilisateur. Les lignes Utilisateur ne sont pas rédigées : le PRD limite le User aux données validées, et les demandes de la liste ne le sont pas (Q5).

Données dédiées ENT-RECH et DEM-RECH : les autres fichiers créent des demandes, une recherche sur une entité partagée afficherait des demandes en plus.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Rechercher mes demandes via le numéro Entité ID

  Plan du scénario: RECH-01 La recherche par Entité ID filtre la liste
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que les demandes "DEM-RECH-01" et "DEM-RECH-02" de l'entité "ENT-RECH-01" et la demande "DEM-RECH-03" de l'entité "ENT-RECH-02" existent
    Et que je suis sur la "Liste des demandes"
    Quand je saisis "ENT-RECH-01" dans le champ "Rechercher par Entité ID"
    Alors les demandes "DEM-RECH-01" et "DEM-RECH-02" sont affichées
    Et la demande "DEM-RECH-03" n'est pas affichée

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: RECH-02 La recherche se combine avec un autre filtre
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-RECH-01" au millésime 2027 et la demande "DEM-RECH-02" au millésime 2026 de l'entité "ENT-RECH-01" existent
    Et que je suis sur la "Liste des demandes" avec "ENT-RECH-01" saisi dans le champ "Rechercher par Entité ID"
    Quand je sélectionne "2027" dans le filtre "Millésime"
    Alors la demande "DEM-RECH-01" est affichée
    Et la demande "DEM-RECH-02" n'est pas affichée

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: RECH-03 Vider la recherche rétablit la liste
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que les demandes "DEM-RECH-01" et "DEM-RECH-02" de l'entité "ENT-RECH-01" et la demande "DEM-RECH-03" de l'entité "ENT-RECH-02" existent
    Et que je suis sur la "Liste des demandes" avec "ENT-RECH-01" saisi dans le champ "Rechercher par Entité ID"
    Quand je vide le champ "Rechercher par Entité ID"
    Alors les demandes "DEM-RECH-01", "DEM-RECH-02" et "DEM-RECH-03" sont affichées

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Étape du flow | Scénarios | Couvert ? |
|---|---|---|
| 1. Liste et champ de recherche affichés | RECH-01 | Couvert |
| 2. Recherche par Entité ID | RECH-01 | Partiel : recherche exacte ou partielle, sensibilité à la casse, message sans résultat (Q-32) |
| 3. Combinaison avec d'autres filtres | RECH-02 | Couvert sur un filtre ; les autres en exploratoire |
| 4. Modification ou suppression de la recherche | RECH-03 | Couvert |
| Profil Utilisateur | | Non couvert : conflit avec le PRD (Q5) |

## 3. Non rédigé

1. Saisie partielle (« ENT-RECH »), fin d'identifiant (« RECH-01 »), minuscules (« ent-rech-01 ») et recherche sans résultat (Q-32).
2. Profil Utilisateur face aux demandes non validées, à vérifier aussi par l'API (Q5).
3. Admin Maroc qui recherche une entité France : la liste est-elle filtrée par périmètre pays (Q-33) ?
