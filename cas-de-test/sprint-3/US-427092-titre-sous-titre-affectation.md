# US 427092 : lire le titre, le sous-titre et l'affectation du mandat

Sources : US 427092 (captures du 23/10/2026), à l'état « To be tested » (PR #36 fusionnée le 13/10/2026). Données fictives uniquement.

Profils : « utilisateur habilité à consulter ou gérer un mandat ». Admin et SuperAdmin ; le profil Utilisateur n'est pas rédigé, les demandes de test n'étant pas validées (Q5).

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Lire le titre, le sous-titre et l'affectation du mandat

  Plan du scénario: TIT-01 Ouvrir la Description du mandat : le titre du mandat est affiché
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-TEST-07" a pour titre "Titre test Alpha"
    Et que le formulaire de la demande "DEM-TEST-07" est ouvert depuis la "Liste des demandes"
    Quand j'affiche la section "Description du mandat"
    Alors la section affiche le titre "Titre test Alpha"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: TIT-02 Ouvrir la Description du mandat : le sous-titre du mandat est affiché
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-TEST-07" a pour sous-titre "Sous-titre test Alpha"
    Et que le formulaire de la demande "DEM-TEST-07" est ouvert depuis la "Liste des demandes"
    Quand j'affiche la section "Description du mandat"
    Alors la section affiche le sous-titre "Sous-titre test Alpha"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: TIT-03 Ouvrir la Description du mandat : Affecté à affiche la personne saisie à la création
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-TEST-07" a été créée avec "Collaborateur Test 01" dans le champ "Affectée à"
    Et que le formulaire de la demande "DEM-TEST-07" est ouvert depuis la "Liste des demandes"
    Quand j'affiche la section "Description du mandat"
    Alors le champ "Affecté à" affiche "Collaborateur Test 01"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: TIT-04 Réaffecter puis recharger la demande : Affecté à affiche la nouvelle personne
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-TEST-07" a été réaffectée de "Collaborateur Test 01" à "Collaborateur Test 02"
    Et que le formulaire de la demande "DEM-TEST-07" est ouvert sur la section "Description du mandat"
    Quand je recharge la page de la demande
    Alors le champ "Affecté à" affiche "Collaborateur Test 02"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Critère d'acceptation | Scénarios | Couvert ? |
|---|---|---|
| Affichage du titre | TIT-01 | Couvert |
| Affichage du sous-titre | TIT-02 | Couvert |
| Affichage de l'utilisateur affecté | TIT-03 | Couvert |
| Mise à jour de l'affectation | TIT-04 | Couvert ; qui peut réaffecter n'est pas dit |
| Absence de sous-titre | | Non couvert : l'US donne deux résultats possibles (Q-37) |
| Données indisponibles | | Non couvert : texte coupé sur la capture |

## 3. Non rédigé

1. Mandat sans sous-titre : zone masquée ou valeur définie par les règles métier (Q-37). D'où viennent le titre et le sous-titre ?
2. Critère « Données indisponibles » : à relire dans l'US.
3. Profil Utilisateur (Q5).
