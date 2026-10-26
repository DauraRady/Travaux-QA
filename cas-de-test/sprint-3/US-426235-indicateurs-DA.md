# US 426235 : déterminer automatiquement les indicateurs DA du mandat

Sources : US 426235 (captures du 23/10/2026). Données fictives uniquement.

Périmètre testé : Pays « France » et Type de mandat « Certification des comptes » uniquement. Les règles de l'US pour Durabilité (RG-DA-03) et pour le type mixte (RG-DA-04) sont hors périmètre ; le recalcul au changement de type (RG-DA-05) aussi, puisqu'un seul type est disponible.

L'acteur de l'US est le système. L'utilisateur qui choisit le type est un profil habilité à compléter une demande, soit Admin et SuperAdmin.

L'US se contredit : l'étape 3 dit « Le système enregistre les valeurs calculées », le hors scope dit « Pas de sauvegarde pour le moment donc pas d'appel API ». Les scénarios ne vérifient que l'écran (Q-26).

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Déterminer automatiquement les indicateurs DA du mandat

  Plan du scénario: DA-01 Choisir Certification des comptes : indicateur Certification à Oui, Durabilité à Non
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France"
    Quand je sélectionne "Certification des comptes" dans le champ "Type de mandat"
    Alors l'indicateur "Client Certification des comptes avec DA" affiche "Oui"
    Et l'indicateur "Client Durabilité avec DA" affiche "Non"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: DA-02 Tenter de modifier un indicateur DA : la valeur calculée ne change pas
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France" et le Type de mandat "Certification des comptes"
    Quand j'essaie de changer la valeur de l'indicateur "Client Certification des comptes avec DA"
    Alors l'indicateur "Client Certification des comptes avec DA" n'est pas modifiable
    Et l'indicateur "Client Certification des comptes avec DA" affiche toujours "Oui"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Règle de l'US | Scénarios | Couvert ? |
|---|---|---|
| RG-DA-01 Calculés, jamais modifiables | DA-02 | Couvert |
| RG-DA-02 Certification des comptes : Oui et Non | DA-01 | Couvert |
| RG-DA-03 Durabilité | | Hors périmètre |
| RG-DA-04 Certification et Durabilité | | Hors périmètre |
| RG-DA-05 Recalcul au changement de type | | Hors périmètre : un seul type disponible |
| Étape 3 Enregistrement | | Non couvert : contredit par le hors scope (Q-26) |

## 3. Non rédigé

1. Valeur des indicateurs tant qu'aucun type n'est choisi : vides, à Non, ou masqués (Q-23).
2. Enregistrement des indicateurs et envoi vers la Déclaration d'Activités (Q-26).
