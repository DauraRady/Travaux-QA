# US 422727 : visualiser la base d'affichage du formulaire

Sources : US 422727 (captures du 23/10/2026 ; ses 4 commentaires ne sont pas visibles). Données fictives uniquement.

Profils : « utilisateur habilité à consulter ou compléter un formulaire ». Admin et SuperAdmin pour les demandes non validées ; le profil Utilisateur n'est pas rédigé (Q5). Ouvrir un formulaire validé en modification : SuperAdmin selon le PRD, Admin selon S1-03 (Q6), seul le SuperAdmin est rédigé.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Visualiser la base d'affichage du formulaire

  Plan du scénario: HEAD-01 Ouvrir une demande : l'en-tête affiche le nom de l'entité, l'Entité ID et le statut
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-TEST-02" de l'entité "ENT-HEAD-01", nommée "Société Test Alpha", est au statut "En cours"
    Et que je suis sur la "Liste des demandes"
    Quand j'ouvre le formulaire de la demande "DEM-TEST-02"
    Alors l'en-tête affiche le nom "Société Test Alpha"
    Et l'en-tête affiche l'Entité ID "ENT-HEAD-01"
    Et l'en-tête affiche le statut "En cours"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: HEAD-02 Ouvrir une demande d'entité inconnue du référentiel : l'en-tête affiche l'Entité ID
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-TEST-06" de l'entité "ENT-HEAD-99", absente du référentiel, existe
    Et que je suis sur la "Liste des demandes"
    Quand j'ouvre le formulaire de la demande "DEM-TEST-06"
    Alors l'en-tête affiche l'Entité ID "ENT-HEAD-99"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: HEAD-03 Cliquer sur Retour depuis une demande non validée : retour à la Liste des demandes
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le formulaire de la demande "DEM-TEST-02", au statut "En cours", est ouvert depuis la "Liste des demandes"
    Quand je clique sur "Retour"
    Alors la "Liste des demandes" s'affiche

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Scénario: HEAD-04 Cliquer sur Retour depuis un formulaire validé : retour à la Gestion d'entité
    Étant donné que je suis connecté avec le compte "SA-TEST-01" ayant le rôle "SuperAdmin"
    Et que le formulaire de la demande "DEM-TEST-04", au statut "Validé", est ouvert en modification depuis la page "Gestion d'entité"
    Quand je clique sur "Retour"
    Alors la page "Gestion d'entité" s'affiche

  Plan du scénario: HEAD-05 Cliquer sur Retour après un lien direct : retour à la Liste des demandes
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le formulaire de la demande "DEM-TEST-02" est ouvert par son lien direct dans un nouvel onglet
    Quand je clique sur "Retour"
    Alors la "Liste des demandes" s'affiche

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Étape du flow | Scénarios | Couvert ? |
|---|---|---|
| 3. Nom de l'entité, Entité ID, statut | HEAD-01, HEAD-02 | Partiel : nom affiché pour une entité inconnue (Q-35) |
| 5. Demande non validée : retour à la liste | HEAD-03 | Couvert |
| 5. Formulaire validé : retour à la Gestion d'entité | HEAD-04 | Partiel : profil Admin à trancher (Q6) ; demande validée à injecter par un développeur |
| 5. Sans page précédente : retour à la liste | HEAD-05 | Couvert |

## 3. Non rédigé

1. Demande non validée ouverte depuis la Gestion d'entité : le retour suit-il la page précédente ou le statut (Q-36) ?
2. Nom affiché quand l'entité est inconnue du référentiel (Q-35).
3. Profil Utilisateur (Q5) et profil Admin sur un formulaire validé (Q6).
