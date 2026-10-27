# US 426406 : renseigner l'AGP, la catégorie d'entité et le Type d'EIP

Sources : US 426406 (captures du 23/10/2026). Données fictives uniquement.

Profils habilités : « collaborateur habilité à compléter une demande », soit Admin et SuperAdmin.

Prérequis de l'US (étape 0) : Pays, Type de mandat et Catégorie du mandat déjà renseignés. Les scénarios les fixent à France, Certification des comptes, Nouveau.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Renseigner l'AGP, la catégorie d'entité et le Type d'EIP

  Plan du scénario: EIP-01 Choisir EIP : AGP forcé à Non et Type d'EIP obligatoire
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que le bloc "Qualification réglementaire de l'entité" est affiché
    Quand je sélectionne "EIP" dans le champ "Catégorie d'entité"
    Alors le champ "AGP" affiche "Non"
    Et le champ "AGP" n'est pas modifiable
    Et le champ "Type d'EIP" est actif et obligatoire

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: EIP-02 Passer de Non-EIP à EIP : l'AGP à Oui est remplacé par Non
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que j'ai sélectionné la Catégorie d'entité "Non-EIP" et l'AGP "Oui"
    Quand je sélectionne "EIP" dans le champ "Catégorie d'entité"
    Alors le champ "AGP" affiche "Non"
    Et le champ "AGP" n'est pas modifiable

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: EIP-03 Choisir deux types d'EIP : les deux sont retenus
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que j'ai sélectionné la Catégorie d'entité "EIP"
    Quand je sélectionne "Établissement de crédit" dans le champ "Type d'EIP"
    Et que je sélectionne aussi "OPCVM coté sur un marché réglementé" dans le champ "Type d'EIP"
    Alors le champ "Type d'EIP" affiche "Établissement de crédit" et "OPCVM coté sur un marché réglementé"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: EIP-04 Ouvrir la liste des types d'EIP : les 13 valeurs de l'US sont proposées
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que j'ai sélectionné la Catégorie d'entité "EIP"
    Quand j'ouvre la liste du champ "Type d'EIP"
    Alors la liste propose exactement les 13 valeurs de la section « Champs concernés » de l'US 426406

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: EIP-05 Choisir Non-EIP ou OPC : Type d'EIP à N/A et verrouillé
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Quand je sélectionne "<categorie>" dans le champ "Catégorie d'entité"
    Alors le champ "Type d'EIP" affiche "N/A"
    Et le champ "Type d'EIP" n'est pas modifiable
    Et le champ "AGP" est modifiable

    Exemples:
      | cas                 | compte     | role       | categorie |
      | Admin, Non-EIP      | AD-TEST-01 | Admin      | Non-EIP   |
      | Admin, OPC          | AD-TEST-01 | Admin      | OPC       |
      | SuperAdmin, Non-EIP | SA-TEST-01 | SuperAdmin | Non-EIP   |
      | SuperAdmin, OPC     | SA-TEST-01 | SuperAdmin | OPC       |

  Plan du scénario: EIP-06 Passer d'EIP à Non-EIP : les types d'EIP choisis sont effacés
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que j'ai sélectionné la Catégorie d'entité "EIP" et les Types d'EIP "Établissement de crédit" et "OPCVM coté sur un marché réglementé"
    Quand je sélectionne "Non-EIP" dans le champ "Catégorie d'entité"
    Alors le champ "Type d'EIP" affiche uniquement "N/A"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: EIP-07 Revenir à EIP après OPC : aucun ancien type d'EIP n'est restauré
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que j'ai sélectionné la Catégorie d'entité "EIP" et le Type d'EIP "Établissement de crédit", puis la Catégorie d'entité "OPC"
    Quand je sélectionne "EIP" dans le champ "Catégorie d'entité"
    Alors le champ "Type d'EIP" est vide
    Et le champ "Type d'EIP" n'affiche pas "N/A"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: EIP-08 Recharger après le passage d'EIP à Non-EIP : les types d'EIP effacés ne reviennent pas
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que j'ai sélectionné la Catégorie d'entité "EIP" et les Types d'EIP "Établissement de crédit" et "OPCVM coté sur un marché réglementé", puis la Catégorie d'entité "Non-EIP"
    Quand je recharge la page de la demande
    Alors le champ "Catégorie d'entité" affiche "Non-EIP"
    Et le champ "Type d'EIP" affiche uniquement "N/A"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: EIP-09 Recharger une demande EIP : l'AGP reste à Non et non modifiable
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que j'ai sélectionné la Catégorie d'entité "Non-EIP" et l'AGP "Oui", puis la Catégorie d'entité "EIP" et le Type d'EIP "Établissement de crédit"
    Quand je recharge la page de la demande
    Alors le champ "AGP" affiche "Non"
    Et le champ "AGP" n'est pas modifiable

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: EIP-10 Enregistrer par l'API une entité EIP avec l'AGP à Oui : la combinaison n'est pas enregistrée
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge existe avec le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Quand j'envoie directement à l'API l'enregistrement de cette demande avec la Catégorie d'entité "EIP", le Type d'EIP "Établissement de crédit" et l'AGP "Oui"
    Alors la demande relue par l'API n'a pas à la fois la Catégorie d'entité "EIP" et l'AGP "Oui"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: EIP-11 Enregistrer par l'API une entité Non-EIP avec un Type d'EIP : le type n'est pas enregistré
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge existe avec le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Quand j'envoie directement à l'API l'enregistrement de cette demande avec la Catégorie d'entité "Non-EIP" et le Type d'EIP "Établissement de crédit"
    Alors la demande relue par l'API n'a pas le Type d'EIP "Établissement de crédit"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Règle de l'US | Scénarios | Couvert ? |
|---|---|---|
| RG-EIP-01 AGP obligatoire | | Non couvert : moment et forme du contrôle inconnus (Q-21) |
| RG-EIP-02 Catégorie d'entité obligatoire | | Non couvert : même raison (Q-21) |
| RG-EIP-03 | | Absente de la numérotation (Q-28) |
| RG-EIP-04 EIP : AGP à Non, Type d'EIP obligatoire | EIP-01, EIP-02, EIP-09, EIP-10 | Partiel : sortie d'EIP non décrite (Q-27) |
| RG-EIP-05 Multisélection | EIP-03, EIP-04 | Couvert |
| RG-EIP-06 Non-EIP ou OPC : N/A non modifiable | EIP-05, EIP-11 | Couvert |
| RG-EIP-07 EIP vers Non-EIP ou OPC : types effacés | EIP-06, EIP-08 | Couvert, à l'écran et après rechargement |
| RG-EIP-08 Retour à EIP : rien de restauré | EIP-07 | Couvert |

EIP-10 et EIP-11 vérifient que le serveur applique les règles même quand l'écran est contourné. Le résultat attendu porte sur la donnée enregistrée, pas sur la réponse : le serveur peut refuser l'envoi ou corriger la valeur, les deux respectent la règle (Q-41). EIP-08 et EIP-09 supposent, comme MC-05, que la saisie est enregistrée sans bouton dédié ; sinon, enregistre avant de recharger.

## 3. Non rédigé

1. Quitter EIP : l'AGP garde Non et redevient modifiable, ou se vide (Q-27).
2. AGP, Catégorie d'entité ou Type d'EIP vide : quand le contrôle se déclenche et ce qu'il affiche (Q-21).
3. RG-EIP-03 et étapes 5 et 6 absentes de l'US (Q-28) ; sens du sigle AGP (Q-29).
