# US 426407 : renseigner les marchés de cotation de l'entité

Sources : US 426407 (captures du 23/10/2026). Données fictives uniquement.

Profils habilités : « collaborateur habilité à compléter une demande », soit Admin et SuperAdmin.

L'US ne numérote pas ses règles : les identifiants RG-MC de la couverture sont attribués ici.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Renseigner les marchés de cotation de l'entité

  Plan du scénario: MC-01 Non coté en marché 1 impose Non coté aux marchés 2 et 3
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur le bloc "Marchés de cotation de l'entité"
    Quand je sélectionne "Non coté" dans le champ "Marché de cotation 1 Entité"
    Alors les champs "Marché de cotation 2 Entité" et "Marché de cotation 3 Entité" affichent "Non coté"
    Et ces deux champs ne sont pas modifiables

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: MC-02 Remplacer Non coté par un marché réel libère les marchés 2 et 3
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

  Plan du scénario: MC-03 Un marché choisi disparaît des listes suivantes
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

  Plan du scénario: MC-04 Non coté peut être choisi pour les marchés 2 et 3
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

  Plan du scénario: MC-06 Les trois marchés choisis sont conservés après rechargement
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur le bloc "Marchés de cotation de l'entité"
    Et que j'ai sélectionné "Euronext", "London Stock Exchange" et "Non coté" dans les marchés 1, 2 et 3
    Quand je recharge la page de la demande
    Alors les marchés 1, 2 et 3 affichent "Euronext", "London Stock Exchange" et "Non coté"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Règle | Scénarios | Couvert ? |
|---|---|---|
| RG-MC-01 Non coté en marché 1 : marchés 2 et 3 à Non coté, non modifiables | MC-01 | Couvert |
| RG-MC-02 Marché 1 réel : marchés 2 et 3 modifiables, Non coté hérité supprimé | MC-02 | Couvert |
| RG-MC-03 Un marché réel une seule fois | MC-03 | Partiel : contrôle serveur non décrit (Q-38) |
| RG-MC-04 Non coté répétable | MC-04 | Couvert |
| RG-MC-05 Enregistrement des trois valeurs | MC-06 | Couvert |
| RG-MC-06 Trois champs obligatoires | | Non couvert : moment et forme du contrôle inconnus (Q-21) |
| RG-MC-07 Référentiel des marchés | | Non couvert : « Non coté » figure deux fois dans la liste de l'US (Q-30) |
| Contrôles de cohérence annoncés dans la phrase de l'US | | Non couvert : décrits nulle part (Q-31) |

## 3. Non rédigé

1. Unicité des marchés contrôlée aussi côté serveur (Q-38).
2. Champs obligatoires vides : quand et comment le contrôle se manifeste (Q-21).
3. Contenu exact de la liste : doublon « Non coté », « Autre » répétable (Q-30).
4. Cohérence entre marchés et qualification EIP, par exemple une EIP « titres admis sur un marché réglementé de l'UE » avec le marché 1 à « Non coté » (Q-31).
