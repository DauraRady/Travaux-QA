# US 426973 : renseigner la taxonomie pour un mandat de Certification des comptes en France

Sources : US 426973 (captures du 23/10/2026). Données fictives uniquement.

Profils habilités : « collaborateur habilité à compléter une demande », soit Admin et SuperAdmin.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Renseigner la taxonomie pour un mandat de Certification des comptes en France

  Plan du scénario: TAX-01 La catégorie du mandat détermine la taxonomie
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France" et le Type de mandat "Certification des comptes"
    Quand je sélectionne "<categorie>" dans le champ "Catégorie du mandat"
    Alors le bloc "Taxonomie" affiche uniquement "<taxonomie>"

    Exemples:
      | cas                         | compte     | role       | categorie      | taxonomie           |
      | Admin, Nouveau              | AD-TEST-01 | Admin      | Nouveau        | AA11 - CAC Nouveau  |
      | Admin, Reprise              | AD-TEST-01 | Admin      | Reprise        | AA11 - CAC Nouveau  |
      | Admin, Renouvellement       | AD-TEST-01 | Admin      | Renouvellement | AA12 - CAC Maintien |
      | SuperAdmin, Nouveau         | SA-TEST-01 | SuperAdmin | Nouveau        | AA11 - CAC Nouveau  |
      | SuperAdmin, Reprise         | SA-TEST-01 | SuperAdmin | Reprise        | AA11 - CAC Nouveau  |
      | SuperAdmin, Renouvellement  | SA-TEST-01 | SuperAdmin | Renouvellement | AA12 - CAC Maintien |

  Plan du scénario: TAX-02 Changer la catégorie remplace la taxonomie
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que le bloc "Taxonomie" affiche "AA11 - CAC Nouveau"
    Quand je sélectionne "Renouvellement" dans le champ "Catégorie du mandat"
    Alors le bloc "Taxonomie" affiche uniquement "AA12 - CAC Maintien"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: TAX-03 Sans catégorie, aucune taxonomie n'est affectée
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Quand je sélectionne le Pays "France" et le Type de mandat "Certification des comptes"
    Alors le bloc "Taxonomie" n'affiche aucune taxonomie
    Et aucune taxonomie n'est sélectionnable dans le bloc "Taxonomie"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: TAX-04 Passer au type Durabilité retire la taxonomie de Certification
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que le bloc "Taxonomie" affiche "AA11 - CAC Nouveau"
    Quand je sélectionne "Durabilité" dans le champ "Type de mandat"
    Alors le bloc "Taxonomie" n'affiche plus "AA11 - CAC Nouveau"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: TAX-05 La taxonomie calculée n'est pas modifiable
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Renouvellement"
    Quand j'essaie d'ajouter, de retirer et de remplacer une taxonomie dans le bloc "Taxonomie"
    Alors aucune de ces actions n'est proposée
    Et le bloc "Taxonomie" affiche toujours uniquement "AA12 - CAC Maintien"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: TAX-06 Passer le pays hors France retire la taxonomie France
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Et que le bloc "Taxonomie" affiche "AA11 - CAC Nouveau"
    Quand je sélectionne "Maroc" dans le champ "Pays"
    Alors le bloc "Taxonomie" n'affiche plus "AA11 - CAC Nouveau"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Règle de l'US | Scénarios | Couvert ? |
|---|---|---|
| RG-TAX-CERT-01 Automatique, non modifiable | TAX-05 | Couvert |
| RG-TAX-CERT-02 Données nécessaires | TAX-03 | Partiel : Pays ou Type manquant en exploratoire |
| RG-TAX-CERT-03 Nouveau ou Reprise : AA11 | TAX-01 | Couvert |
| RG-TAX-CERT-04 Renouvellement : AA12 | TAX-01 | Couvert |
| RG-TAX-CERT-05 Une seule taxonomie | TAX-01, TAX-02, TAX-05 | Couvert |
| RG-TAX-CERT-06 Recalcul automatique | TAX-02, TAX-04, TAX-06 | Partiel : capture coupée après le point 1 ; la suite vient de l'étape 4 du flow |

## 3. Non rédigé

1. Taxonomie attendue hors France (l'ancien PRD citait MAA11 et MAA12) (Q-24).
2. Type « Certification des comptes & Durabilité » : une taxonomie ou deux (Q-25).
3. Reprise donne AA11 comme Nouveau : à confirmer avec le sens de Reprise (Q-22).
