# US 426407 : renseigner les marchés de cotation de l'entité

Sources : US 426407 (captures du 23/10/2026). Données fictives uniquement.

Profils habilités : « collaborateur habilité à compléter une demande », soit Admin et SuperAdmin.

L'US ne numérote pas ses règles : les identifiants RG-MC de la couverture sont attribués ici.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Renseigner les marchés de cotation de l'entité

  Plan du scénario: MC-01 Choisir Non coté en marché 1 : marchés 2 et 3 forcés à Non coté
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur le bloc "Marchés de cotation de l'entité"
    Quand je sélectionne "Non coté" dans le champ "Marché de cotation 1 Entité"
    Alors les champs "Marché de cotation 2 Entité" et "Marché de cotation 3 Entité" affichent "Non coté"
    Et ces deux champs ne sont pas modifiables

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: MC-02 Remplacer Non coté par Euronext en marché 1 : marchés 2 et 3 redeviennent modifiables
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur le bloc "Marchés de cotation de l'entité"
    Et que j'ai sélectionné "Non coté" dans le champ "Marché de cotation 1 Entité"
    Quand je sélectionne "Euronext" dans le champ "Marché de cotation 1 Entité"
    Alors les champs "Marché de cotation 2 Entité" et "Marché de cotation 3 Entité" sont modifiables
    Et ces deux champs n'affichent plus "Non coté"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: MC-03 Choisir Euronext en marché 1 : Euronext n'est plus proposé en marché 2
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur le bloc "Marchés de cotation de l'entité"
    Et que j'ai sélectionné "Euronext" dans le champ "Marché de cotation 1 Entité"
    Quand j'ouvre la liste du champ "Marché de cotation 2 Entité"
    Alors la liste ne propose pas "Euronext"
    Et la liste propose "NYSE"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: MC-04 Choisir Non coté en marchés 2 et 3 : la valeur peut se répéter
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur le bloc "Marchés de cotation de l'entité"
    Et que j'ai sélectionné "Euronext" dans le champ "Marché de cotation 1 Entité"
    Quand je sélectionne "Non coté" dans le champ "Marché de cotation 2 Entité"
    Et que je sélectionne "Non coté" dans le champ "Marché de cotation 3 Entité"
    Alors les champs "Marché de cotation 2 Entité" et "Marché de cotation 3 Entité" affichent "Non coté"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: MC-05 Recharger la demande : les trois marchés choisis sont conservés
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur le bloc "Marchés de cotation de l'entité"
    Et que j'ai sélectionné "Euronext", "London Stock Exchange" et "Non coté" dans les marchés 1, 2 et 3
    Quand je recharge la page de la demande
    Alors les marchés 1, 2 et 3 affichent "Euronext", "London Stock Exchange" et "Non coté"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: MC-06 Choisir en marché 1 le marché déjà choisi en marché 2 : le même marché n'est pas retenu deux fois
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur le bloc "Marchés de cotation de l'entité"
    Et que j'ai sélectionné "Euronext" dans le champ "Marché de cotation 1 Entité" et "NYSE" dans le champ "Marché de cotation 2 Entité"
    Quand je sélectionne "NYSE" dans le champ "Marché de cotation 1 Entité"
    Alors les champs "Marché de cotation 1 Entité" et "Marché de cotation 2 Entité" n'affichent pas tous les deux "NYSE"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: MC-07 Choisir Non coté en marché 1 alors que les marchés 2 et 3 sont remplis : ils passent à Non coté
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur le bloc "Marchés de cotation de l'entité"
    Et que j'ai sélectionné "Euronext", "NYSE" et "London Stock Exchange" dans les marchés 1, 2 et 3
    Quand je sélectionne "Non coté" dans le champ "Marché de cotation 1 Entité"
    Alors les champs "Marché de cotation 2 Entité" et "Marché de cotation 3 Entité" affichent "Non coté"
    Et ces deux champs ne sont pas modifiables

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: MC-08 Enregistrer par l'API un marché 1 Non coté avec un marché 2 réel : la combinaison n'est pas enregistrée
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge existe
    Quand j'envoie directement à l'API l'enregistrement de cette demande avec les marchés 1, 2 et 3 "Non coté", "NYSE" et "Non coté"
    Alors la demande relue par l'API n'a pas le marché 1 "Non coté" avec le marché 2 "NYSE"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: MC-09 Enregistrer par l'API le même marché réel en marchés 1 et 2 : le doublon n'est pas enregistré
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge existe
    Quand j'envoie directement à l'API l'enregistrement de cette demande avec les marchés 1, 2 et 3 "Euronext", "Euronext" et "Non coté"
    Alors la demande relue par l'API n'a pas "Euronext" à la fois en marché 1 et en marché 2

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Règle | Scénarios | Couvert ? |
|---|---|---|
| RG-MC-01 Non coté en marché 1 : marchés 2 et 3 à Non coté, non modifiables | MC-01, MC-07, MC-08 | Couvert, sur demande vierge, sur demande remplie et par l'API |
| RG-MC-02 Marché 1 réel : marchés 2 et 3 modifiables, Non coté hérité supprimé | MC-02 | Couvert |
| RG-MC-03 Un marché réel une seule fois | MC-03, MC-06, MC-09 | Couvert ; forme du rejet serveur inconnue (Q-38, Q-41) |
| RG-MC-04 Non coté répétable | MC-04 | Couvert |
| RG-MC-05 Enregistrement des trois valeurs | MC-05 | Couvert |
| RG-MC-05 Trois champs obligatoires | | Non couvert : moment et forme du contrôle inconnus (Q-21) |
| RG-MC-07 Référentiel des marchés | | Non couvert : « Non coté » figure deux fois dans la liste de l'US (Q-30) |
| Contrôles de cohérence annoncés dans la phrase de l'US | | Non couvert : décrits nulle part (Q-31) |

MC-06 ne dit pas comment l'écran résout le conflit (refus du choix, vidage du marché 2, ou NYSE absent de la liste du marché 1) : il vérifie seulement que la règle tient. Note ce que l'écran fait réellement et fais-le confirmer au PO. MC-08 et MC-09 portent sur la donnée enregistrée, que le serveur refuse ou corrige (Q-41).

## 3. Non rédigé

1. Forme du rejet serveur quand l'unicité ou la règle Non coté est contournée : code, message (Q-38, Q-41).
2. Champs obligatoires vides : quand et comment le contrôle se manifeste (Q-21).
3. Contenu exact de la liste : doublon « Non coté », « Autre » répétable (Q-30).
4. Cohérence entre marchés et qualification EIP, par exemple une EIP « titres admis sur un marché réglementé de l'UE » avec le marché 1 à « Non coté » (Q-31).
