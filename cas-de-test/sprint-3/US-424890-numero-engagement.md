# US 424890 : renseigner un numéro d'engagement lors de la création d'une demande

Sources : US 424890 (captures du 23/10/2026), cas de création existants (`../creer-une-demande.md`). Données fictives uniquement.

Profils habilités selon l'US : Administrateur et SuperAdministrateur. Chaque scénario est joué pour les deux.

Piège de données : la création est refusée si l'entité a déjà une demande en cours, en retard ou en révision (TC07 de `creer-une-demande.md`). Chaque création réussie utilise donc sa propre entité (ENT-ENG-xx), et chaque engagement libre est consommé par la création qui l'utilise.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Renseigner un numéro d'engagement lors de la création d'une demande

  Plan du scénario: ENG-01 Créer une demande sans numéro d'engagement : la demande est créée sans engagement
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau" et l'Entité ID "<entite>"
    Et que le champ "Numéro d'engagement" est vide
    Quand je clique sur "Valider la création"
    Alors une demande pour l'entité "<entite>" apparaît dans la "Liste des demandes"
    Et aucun numéro d'engagement n'est associé à cette demande

    Exemples:
      | cas                | compte     | role       | entite     |
      | rôle Admin         | AD-TEST-01 | Admin      | ENT-ENG-01 |
      | rôle SuperAdmin    | SA-TEST-01 | SuperAdmin | ENT-ENG-02 |

  Plan du scénario: ENG-02 Vider un numéro d'engagement en erreur : l'erreur disparaît
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau" et l'Entité ID "ENT-ENG-10"
    Et que le numéro "9999999" est saisi et affiché en erreur avec le message "Numéro inconnu."
    Quand je vide le champ "Numéro d'engagement"
    Alors le message "Numéro inconnu." n'est plus affiché
    Et le champ "Numéro d'engagement" n'est plus affiché en erreur

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: ENG-03 Saisir le début d'un numéro : les suggestions affichent le numéro et la description
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que l'engagement "1021001" de description "Mission test Alpha" existe dans le Référentiel Finance
    Et que l'engagement "1021002" sans description existe dans le Référentiel Finance
    Quand je saisis "1021" dans le champ "Numéro d'engagement"
    Alors la suggestion "1021001" est affichée avec la description "Mission test Alpha"
    Et la suggestion "1021002" est affichée sans description

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: ENG-04 Saisir un numéro sans correspondance : « Aucun résultat » et aucune suggestion sélectionnable
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et qu'aucun engagement du Référentiel Finance ne commence par "8888"
    Quand je saisis "8888" dans le champ "Numéro d'engagement"
    Alors l'indication "Aucun résultat" est affichée dans la liste
    Et aucune suggestion n'est sélectionnable

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: ENG-05 Saisir des lettres ou un espace : le champ ne garde que des chiffres
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Quand je saisis "<saisie>" dans le champ "Numéro d'engagement"
    Alors le champ "Numéro d'engagement" ne contient que des chiffres

    Exemples:
      | cas                         | compte     | role       | saisie |
      | Admin, lettres et tiret     | AD-TEST-01 | Admin      | ENG-12 |
      | Admin, espace               | AD-TEST-01 | Admin      | 10 21  |
      | SuperAdmin, lettres et tiret | SA-TEST-01 | SuperAdmin | ENG-12 |
      | SuperAdmin, espace          | SA-TEST-01 | SuperAdmin | 10 21  |

  Plan du scénario: ENG-06 Créer avec un engagement valide : l'engagement est enregistré sur la demande
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que l'engagement "<engagement>" existe dans le Référentiel Finance, rattaché à l'entité "<entite>" et associé à aucune demande
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau" et l'Entité ID "<entite>"
    Et que j'ai sélectionné l'engagement "<engagement>" dans les suggestions
    Quand je clique sur "Valider la création"
    Alors une demande pour l'entité "<entite>" apparaît dans la "Liste des demandes"
    Et le numéro d'engagement de cette demande est "<engagement>"

    Exemples:
      | cas             | compte     | role       | entite     | engagement |
      | rôle Admin      | AD-TEST-01 | Admin      | ENT-ENG-03 | 1021001    |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin | ENT-ENG-04 | 1021011    |

  Plan du scénario: ENG-07 Créer avec un engagement à zéros en tête : les zéros sont conservés
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que l'engagement "<engagement>" existe dans le Référentiel Finance, rattaché à l'entité "<entite>" et associé à aucune demande
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau" et l'Entité ID "<entite>"
    Et que j'ai sélectionné l'engagement "<engagement>" dans les suggestions
    Quand je clique sur "Valider la création"
    Alors le numéro d'engagement de la demande de l'entité "<entite>" est "<engagement>"

    Exemples:
      | cas             | compte     | role       | entite     | engagement |
      | rôle Admin      | AD-TEST-01 | Admin      | ENT-ENG-05 | 0001234    |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin | ENT-ENG-06 | 0001235    |

  Plan du scénario: ENG-08 Choisir une suggestion après un numéro en erreur : l'erreur disparaît
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que l'engagement "1021006" existe dans le Référentiel Finance, rattaché à l'entité "ENT-ENG-10" et associé à aucune demande
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau" et l'Entité ID "ENT-ENG-10"
    Et que le numéro "9999999" est saisi et affiché en erreur avec le message "Numéro inconnu."
    Quand je sélectionne l'engagement "1021006" dans les suggestions
    Alors le message "Numéro inconnu." n'est plus affiché
    Et le champ "Numéro d'engagement" n'est plus affiché en erreur

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: ENG-09 Créer avec un numéro absent du Référentiel Finance : création bloquée, « Numéro inconnu. »
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le numéro "9999999" n'existe pas dans le Référentiel Finance
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau" et l'Entité ID "ENT-ENG-10"
    Et que j'ai saisi "9999999" dans le champ "Numéro d'engagement"
    Quand je clique sur "Valider la création"
    Alors le champ "Numéro d'engagement" est affiché en erreur avec le message "Numéro inconnu."
    Et le toaster affiche "Nous ne retrouvons pas votre engagement. Il n'est pas possible de créer la demande avec ce numéro. Vous pouvez laisser le champ vide pour poursuivre la création."
    Et aucune demande pour l'entité "ENT-ENG-10" n'apparaît dans la "Liste des demandes"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: ENG-10 Créer par l'API avec un engagement inconnu ou d'une autre entité : refus du serveur
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que l'engagement "<engagement>" est <situation>
    Quand j'envoie directement à l'API la création d'une demande pour l'entité "ENT-ENG-10" avec l'engagement "<engagement>"
    Alors la création est refusée
    Et aucune demande pour l'entité "ENT-ENG-10" n'existe

    Exemples:
      | cas                           | compte     | role       | engagement | situation                                          |
      | Admin, numéro inconnu         | AD-TEST-01 | Admin      | 9999999    | absent du Référentiel Finance                      |
      | Admin, autre entité           | AD-TEST-01 | Admin      | 1021003    | rattaché à l'entité ENT-ENG-11 et associé à aucune demande |
      | SuperAdmin, numéro inconnu    | SA-TEST-01 | SuperAdmin | 9999999    | absent du Référentiel Finance                      |
      | SuperAdmin, autre entité      | SA-TEST-01 | SuperAdmin | 1021003    | rattaché à l'entité ENT-ENG-11 et associé à aucune demande |

  Plan du scénario: ENG-11 Créer avec un engagement déjà associé : création bloquée, « Numéro déjà existant. »
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-TEST-01" de l'entité "ENT-ENG-12" est au statut "Validé" avec l'engagement "1021002"
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Renouvellement" et l'Entité ID "ENT-ENG-12"
    Et que j'ai sélectionné l'engagement "1021002" dans les suggestions
    Quand je clique sur "Valider la création"
    Alors le toaster affiche "Cet engagement est déjà associé à une demande. Il n'est pas possible de créer une nouvelle demande avec ce numéro. Vous pouvez laisser le champ vide pour poursuivre la création."
    Et le champ "Numéro d'engagement" est affiché en erreur avec le message "Numéro déjà existant."
    Et la demande "DEM-TEST-01" est la seule demande de l'entité "ENT-ENG-12"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: ENG-12 Créer par l'API avec un engagement déjà associé : refus du serveur
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-TEST-01" de l'entité "ENT-ENG-12" est au statut "Validé" avec l'engagement "1021002"
    Quand j'envoie directement à l'API la création d'une demande de renouvellement pour l'entité "ENT-ENG-12" avec l'engagement "1021002"
    Alors la création est refusée
    Et la demande "DEM-TEST-01" est la seule demande de l'entité "ENT-ENG-12"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: ENG-13 Envoyer deux créations simultanées avec le même engagement : une seule demande est créée
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que l'engagement "<engagement>" existe dans le Référentiel Finance, rattaché à l'entité "<entite>" et associé à aucune demande
    Quand j'envoie en même temps à l'API deux créations d'une demande pour l'entité "<entite>" avec l'engagement "<engagement>"
    Alors une seule demande est associée à l'engagement "<engagement>"
    Et l'autre création est refusée avec le message "Numéro déjà existant."

    Exemples:
      | cas             | compte     | role       | entite     | engagement |
      | rôle Admin      | AD-TEST-01 | Admin      | ENT-ENG-07 | 1021004    |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin | ENT-ENG-08 | 1021014    |

  Plan du scénario: ENG-14 Créer avec un engagement d'une autre entité : création bloquée, « Numéro incompatible. »
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que l'engagement "1021003" existe dans le Référentiel Finance, rattaché à l'entité "ENT-ENG-11" et associé à aucune demande
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau" et l'Entité ID "ENT-ENG-10"
    Et que j'ai sélectionné l'engagement "1021003" dans les suggestions
    Quand je clique sur "Valider la création"
    Alors le champ "Numéro d'engagement" est affiché en erreur avec le message "Numéro incompatible."
    Et le toaster affiche "L'engagement n'appartient pas à cette entité. Il n'est pas possible de créer la demande avec ce numéro. Vous pouvez laisser le champ vide pour poursuivre la création."
    Et aucune demande pour l'entité "ENT-ENG-10" n'apparaît dans la "Liste des demandes"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: ENG-15 Référentiel Finance indisponible pendant la saisie : message d'erreur et aucune suggestion
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que le Référentiel Finance est rendu indisponible par l'équipe de développement
    Quand je saisis "1021" dans le champ "Numéro d'engagement"
    Alors un message d'erreur s'affiche
    Et aucune suggestion n'est sélectionnable

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: ENG-16 Référentiel Finance indisponible à la validation : création bloquée
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau" et l'Entité ID "ENT-ENG-10"
    Et que j'ai sélectionné l'engagement "1021006" dans les suggestions
    Et que le Référentiel Finance est ensuite rendu indisponible par l'équipe de développement
    Quand je clique sur "Valider la création"
    Alors un message d'erreur s'affiche
    Et aucune demande pour l'entité "ENT-ENG-10" n'apparaît dans la "Liste des demandes"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Critère de l'US | Scénarios | Couvert ? |
|---|---|---|
| Champ facultatif (scénario 1) | ENG-01 | Couvert |
| Saisie numérique, zéros conservés (scénario 2) | ENG-05, ENG-07 | Couvert |
| Suggestions (scénario 3) | ENG-03 | Couvert |
| Aucun résultat (scénario 4) | ENG-04 | Couvert |
| Numéro absent du référentiel (scénario 5) | ENG-09, ENG-10 | Couvert |
| Numéro existant et disponible (scénario 6) | ENG-06 | Couvert |
| Numéro déjà associé (scénario 7) | ENG-11, ENG-12 | Couvert ; texte du message à confirmer (Q-13) |
| Numéro incompatible avec l'entité (scénario 8) | ENG-10, ENG-14 | Partiel : propriété de rattachement inconnue (Q-14) |
| Correction d'un numéro en erreur (scénario 9) | ENG-08 | Couvert |
| Suppression d'un numéro en erreur (scénario 10) | ENG-02, ENG-01 | Couvert |
| Référentiel indisponible, recherche (scénario 11) | ENG-15 | Partiel : texte « proposé » (Q-15) |
| Référentiel indisponible, création (scénario 12) | ENG-16 | Partiel : contenu du ProblemDetails (Q-12) |
| Double soumission (scénario 13) | ENG-13 | Couvert |
| Contrôle front et back | ENG-10, ENG-12 | Couvert |

## 3. Non rédigé

1. Entité ID modifiée après le choix d'un engagement compatible : vidage, erreur, ou contrôle à la validation seulement (Q-16).
2. Engagement saisi avec une Entité ID inconnue du référentiel : la compatibilité ne peut pas être vérifiée (Q-17).
3. Engagement d'une demande annulée ou supprimée : redevient-il disponible (Q-18) ?
4. Code HTTP exact de chaque refus serveur (Q-12).
