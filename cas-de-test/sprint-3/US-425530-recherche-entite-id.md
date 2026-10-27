# US 425530 : rechercher mes demandes via le numéro Entité ID

Sources : US 425530 (captures du 23/10/2026 ; ses 5 commentaires ne sont pas visibles). Données fictives uniquement.

Profils de l'US : Super Admin, Admin et Utilisateur. Les lignes Utilisateur ne sont pas rédigées : le PRD limite le User aux données validées, et les demandes de la liste ne le sont pas (Q5).

Données dédiées ENT-RECH et DEM-RECH : les autres fichiers créent des demandes, une recherche sur une entité partagée afficherait des demandes en plus.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Rechercher mes demandes via le numéro Entité ID

  Plan du scénario: RECH-01 Rechercher une Entité ID : seules les demandes de cette entité sont affichées
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

  Plan du scénario: RECH-02 Combiner la recherche et le filtre Millésime : seules les demandes qui répondent aux deux restent
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

  Plan du scénario: RECH-03 Vider la recherche : toutes les demandes réapparaissent
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que les demandes "DEM-RECH-01" et "DEM-RECH-02" de l'entité "ENT-RECH-01" et la demande "DEM-RECH-03" de l'entité "ENT-RECH-02" existent
    Et que je suis sur la "Liste des demandes" avec "ENT-RECH-01" saisi dans le champ "Rechercher par Entité ID"
    Quand je vide le champ "Rechercher par Entité ID"
    Alors les demandes "DEM-RECH-01", "DEM-RECH-02" et "DEM-RECH-03" sont affichées

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: RECH-04 Rechercher une Entité ID qui n'existe nulle part : aucune demande n'est affichée
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que l'Entité ID "ENT-RECH-99" n'existe ni dans le référentiel ni sur une demande
    Et que je suis sur la "Liste des demandes"
    Quand je saisis "ENT-RECH-99" dans le champ "Rechercher par Entité ID"
    Alors aucune demande n'est affichée dans la "Liste des demandes"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: RECH-05 Rechercher une entité dont la seule demande est validée : la demande n'est pas affichée
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la seule demande de l'entité "ENT-RECH-04" est "DEM-RECH-04", au statut "Validé"
    Et que je suis sur la "Liste des demandes"
    Quand je saisis "ENT-RECH-04" dans le champ "Rechercher par Entité ID"
    Alors la demande "DEM-RECH-04" n'est pas affichée
    Et aucune demande n'est affichée dans la "Liste des demandes"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Étape du flow | Scénarios | Couvert ? |
|---|---|---|
| 1. Liste et champ de recherche affichés | RECH-01 | Couvert |
| 2. Recherche par Entité ID | RECH-01, RECH-04 | Partiel : recherche exacte ou partielle, sensibilité à la casse, texte du message sans résultat (Q-32) |
| Règle de la liste (sprint 1) : une demande validée n'apparaît pas | RECH-05 | Couvert ; la recherche ne doit pas faire réapparaître ce que la liste exclut |
| 3. Combinaison avec d'autres filtres | RECH-02 | Couvert sur un filtre ; les autres en exploratoire |
| 4. Modification ou suppression de la recherche | RECH-03 | Couvert |
| Profil Utilisateur | | Non couvert : conflit avec le PRD (Q5) |

## 3. Non rédigé

1. Saisie partielle (« ENT-RECH »), fin d'identifiant (« RECH-01 »), minuscules (« ent-rech-01 ») et recherche sans résultat (Q-32).
2. Profil Utilisateur face aux demandes non validées, à vérifier aussi par l'API (Q5).
