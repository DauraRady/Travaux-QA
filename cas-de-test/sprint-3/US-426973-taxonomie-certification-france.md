# US 426973 : renseigner la taxonomie pour un mandat de Certification des comptes en France

Sources : US 426973 (captures du 23/10/2026). Données fictives uniquement.

Périmètre testé : Pays « France » et Type de mandat « Certification des comptes », comme l'US elle-même.

Profils habilités : « collaborateur habilité à compléter une demande », soit Admin et SuperAdmin.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Renseigner la taxonomie pour un mandat de Certification des comptes en France

  Plan du scénario: TAX-01 Choisir la catégorie du mandat : la taxonomie correspondante est affectée automatiquement
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

  Plan du scénario: TAX-02 Passer de Nouveau à Renouvellement : AA11 est remplacée par AA12
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

  Plan du scénario: TAX-03 Catégorie du mandat non renseignée : aucune taxonomie n'est affectée
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Quand je sélectionne le Pays "France" et le Type de mandat "Certification des comptes"
    Alors le bloc "Taxonomie" n'affiche aucune taxonomie
    Et aucune taxonomie n'est sélectionnable dans le bloc "Taxonomie"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: TAX-04 Tenter de modifier la taxonomie calculée : aucune action n'est possible
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
```

## 2. Couverture

| Règle de l'US | Scénarios | Couvert ? |
|---|---|---|
| RG-TAX-CERT-01 Automatique, non modifiable | TAX-04 | Couvert |
| RG-TAX-CERT-02 Données nécessaires | TAX-03 | Couvert |
| RG-TAX-CERT-03 Nouveau ou Reprise : AA11 | TAX-01 | Couvert |
| RG-TAX-CERT-04 Renouvellement : AA12 | TAX-01 | Couvert |
| RG-TAX-CERT-05 Une seule taxonomie | TAX-01, TAX-02, TAX-04 | Couvert |
| RG-TAX-CERT-06 Recalcul automatique | TAX-02 | Partiel : seul le changement de catégorie existe dans le périmètre (France, Certification) ; capture coupée après le point 1 |

## 3. Non rédigé

1. Reprise donne AA11 comme Nouveau : à confirmer avec le sens de Reprise (Q-22).
