# US 426402 : renseigner les caractéristiques principales du mandat

Sources : US 426402 (captures du 23/10/2026). Données fictives uniquement.

Périmètre testé : Pays « France » et Type de mandat « Certification des comptes » uniquement. L'US décrit encore 18 pays et trois types de mandat ; les autres pays, la Durabilité et le type mixte sont hors périmètre et ne sont pas testés (Q-40).

Profils habilités : « collaborateur habilité à compléter une demande », soit Admin et SuperAdmin. Le profil User, non habilité, est testé en refus (DM-04, DM-05).

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

  Scénario: DM-04 Ouvrir une demande validée avec le rôle User : la section Description du mandat est en lecture seule
    Étant donné que je suis connecté avec le compte "US-TEST-01" ayant le rôle "User"
    Et que la demande "DEM-TEST-04" est au statut "Validé" avec le Pays "France", le Type de mandat "Certification des comptes" et la Catégorie du mandat "Nouveau"
    Quand j'ouvre le formulaire de la demande "DEM-TEST-04" par son lien direct
    Alors les champs "Pays", "Type de mandat" et "Catégorie du mandat" affichent "France", "Certification des comptes" et "Nouveau"
    Et aucun champ de la section "Description du mandat" n'est modifiable

  Scénario: DM-05 Modifier une demande par l'API avec le rôle User : refus et demande inchangée
    Étant donné que je suis connecté avec le compte "US-TEST-01" ayant le rôle "User"
    Et que la demande "DEM-DROIT-01" est au statut "En cours" avec la Catégorie du mandat "Nouveau"
    Quand j'envoie directement à l'API l'enregistrement de la demande "DEM-DROIT-01" avec la Catégorie du mandat "Renouvellement"
    Alors l'API refuse l'enregistrement pour droits insuffisants
    Et la demande "DEM-DROIT-01" relue avec le compte "AD-TEST-01" a toujours la Catégorie du mandat "Nouveau"
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
| Profils : seul un collaborateur habilité complète la demande | DM-04, DM-05 | Couvert pour le User, à l'écran et par l'API |

DM-04 et DM-05 reposent sur le PRD : le User consulte les données validées, sans écriture. DM-04 utilise une demande validée parce que c'est la seule que le User est sûr de pouvoir ouvrir (Q5). DM-05 utilise une demande en cours, pour que le refus vienne du rôle et pas du statut : sur une demande validée, un refus ne prouverait rien sur les droits du User. Le code attendu est en principe 403, à confirmer (Q-12).

## 3. Non rédigé

1. Valeurs réellement proposées par les listes Pays et Type de mandat : l'US en décrit 18 et 3, le périmètre n'en retient qu'une chacune (Q-40).
2. Champs obligatoires vides : quand le contrôle se déclenche et ce qu'il affiche (Q-21).
3. Catégorie choisie ici (Nouveau, Reprise, Renouvellement), alors que la création demande une Nature (Nouveau, Renouvellement) et une Reprise (Oui, Non) : ces champs se recoupent-ils (Q-22) ?
