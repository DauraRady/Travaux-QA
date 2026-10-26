# US 426235 : déterminer automatiquement les indicateurs DA du mandat

Sources : US 426235 (captures du 23/10/2026). Données fictives uniquement.

L'acteur de l'US est le système. L'utilisateur qui choisit le type est un profil habilité à compléter une demande, soit Admin et SuperAdmin.

L'US se contredit : l'étape 3 dit « Le système enregistre les valeurs calculées », le hors scope dit « Pas de sauvegarde pour le moment donc pas d'appel API ». Les scénarios ne vérifient que l'écran (Q-26).

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Déterminer automatiquement les indicateurs DA du mandat

  Plan du scénario: DA-01 Indicateurs DA calculés selon le type de mandat
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France"
    Quand je sélectionne "<type>" dans le champ "Type de mandat"
    Alors l'indicateur "Client Certification des comptes avec DA" affiche "<certification>"
    Et l'indicateur "Client Durabilité avec DA" affiche "<durabilite>"

    Exemples:
      | cas                             | compte     | role       | type                                   | certification | durabilite |
      | Admin, Certification            | AD-TEST-01 | Admin      | Certification des comptes              | Oui           | Non        |
      | Admin, Durabilité               | AD-TEST-01 | Admin      | Durabilité                             | Non           | Oui        |
      | Admin, mixte                    | AD-TEST-01 | Admin      | Certification des comptes & Durabilité | Oui           | Oui        |
      | SuperAdmin, Certification       | SA-TEST-01 | SuperAdmin | Certification des comptes              | Oui           | Non        |
      | SuperAdmin, Durabilité          | SA-TEST-01 | SuperAdmin | Durabilité                             | Non           | Oui        |
      | SuperAdmin, mixte               | SA-TEST-01 | SuperAdmin | Certification des comptes & Durabilité | Oui           | Oui        |

  Plan du scénario: DA-02 Changer de type recalcule immédiatement les indicateurs
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France" et le Type de mandat "Certification des comptes"
    Quand je sélectionne "Durabilité" dans le champ "Type de mandat"
    Alors l'indicateur "Client Certification des comptes avec DA" affiche "Non"
    Et l'indicateur "Client Durabilité avec DA" affiche "Oui"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: DA-03 Hors France, les indicateurs suivent le type imposé
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France" et le Type de mandat "Durabilité"
    Quand je sélectionne "Maroc" dans le champ "Pays"
    Alors l'indicateur "Client Certification des comptes avec DA" affiche "Oui"
    Et l'indicateur "Client Durabilité avec DA" affiche "Non"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: DA-04 Les indicateurs DA ne sont pas modifiables
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France" et le Type de mandat "Durabilité"
    Quand j'essaie de changer la valeur de l'indicateur "Client Durabilité avec DA"
    Alors l'indicateur "Client Durabilité avec DA" n'est pas modifiable
    Et l'indicateur "Client Durabilité avec DA" affiche toujours "Oui"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Règle de l'US | Scénarios | Couvert ? |
|---|---|---|
| RG-DA-01 Calculés, jamais modifiables | DA-04 | Couvert |
| RG-DA-02, 03, 04 Valeurs par type | DA-01, DA-03 | Couvert |
| RG-DA-05 Recalcul immédiat | DA-02, DA-03 | Couvert |
| Étape 3 Enregistrement | | Non couvert : contredit par le hors scope (Q-26) |

## 3. Non rédigé

1. Valeur des indicateurs tant qu'aucun type n'est choisi : vides, à Non, ou masqués (Q-23).
2. Enregistrement des indicateurs et envoi vers la Déclaration d'Activités (Q-26).
