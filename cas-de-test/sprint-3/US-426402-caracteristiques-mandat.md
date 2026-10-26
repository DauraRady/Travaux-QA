# US 426402 : renseigner les caractéristiques principales du mandat

Sources : US 426402 (captures du 23/10/2026). Données fictives uniquement.

Périmètre testé : Pays « France » et Type de mandat « Certification des comptes » uniquement. L'US décrit encore 18 pays et trois types de mandat ; les autres pays, la Durabilité et le type mixte sont hors périmètre et ne sont pas testés (Q-40).

Profils habilités : « collaborateur habilité à compléter une demande », soit Admin et SuperAdmin.

« Une demande vierge » : une demande au statut « En cours », créée pour l'occasion sur une entité neuve, dont aucun champ de la section n'est rempli. Une demande par scénario, pour ne pas hériter des valeurs d'un autre.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Renseigner les caractéristiques principales du mandat

  Plan du scénario: DM-01 Choisir France et Certification des comptes : les deux valeurs sont retenues
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Quand je sélectionne "France" dans le champ "Pays"
    Et que je sélectionne "Certification des comptes" dans le champ "Type de mandat"
    Alors le champ "Pays" affiche "France"
    Et le champ "Type de mandat" affiche "Certification des comptes"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: DM-02 Ouvrir la Catégorie du mandat : Nouveau, Reprise et Renouvellement sont proposés
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France" et le Type de mandat "Certification des comptes"
    Quand j'ouvre la liste du champ "Catégorie du mandat"
    Alors la liste propose exactement : Nouveau, Reprise, Renouvellement

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: DM-03 Changer de catégorie : seule la dernière catégorie choisie est retenue
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Quand je sélectionne "Renouvellement" dans le champ "Catégorie du mandat"
    Alors le champ "Catégorie du mandat" affiche uniquement "Renouvellement"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Règle de l'US | Scénarios | Couvert ? |
|---|---|---|
| Pays France, Type Certification des comptes | DM-01 | Couvert |
| Catégorie : trois valeurs (étape 5) | DM-02 | Couvert ; sens de Reprise à confirmer (Q-22) |
| RG-DM-02 Une seule valeur | DM-03 | Couvert sur la Catégorie |
| RG-DM-01 Champs obligatoires | | Non couvert : moment et forme du contrôle inconnus (Q-21) |
| RG-DM-03 Hors France : Certification imposée | | Hors périmètre (France uniquement) |
| RG-DM-04 France : trois types | | Hors périmètre (Certification des comptes uniquement) ; contenu de la liste à confirmer (Q-40) |

## 3. Non rédigé

1. Valeurs réellement proposées par les listes Pays et Type de mandat : l'US en décrit 18 et 3, le périmètre n'en retient qu'une chacune (Q-40).
2. Champs obligatoires vides : quand le contrôle se déclenche et ce qu'il affiche (Q-21).
3. Catégorie choisie ici (Nouveau, Reprise, Renouvellement), alors que la création demande une Nature (Nouveau, Renouvellement) et une Reprise (Oui, Non) : ces champs se recoupent-ils (Q-22) ?
