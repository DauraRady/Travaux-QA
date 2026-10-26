# US 426402 : renseigner les caractéristiques principales du mandat

Sources : US 426402 (captures du 23/10/2026). Données fictives uniquement.

Profils habilités : « collaborateur habilité à compléter une demande », soit Admin et SuperAdmin.

« Une demande vierge » : une demande au statut « En cours », créée pour l'occasion sur une entité neuve, dont aucun champ de la section n'est rempli. Une demande par scénario, pour ne pas hériter des valeurs d'un autre.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Renseigner les caractéristiques principales du mandat

  Plan du scénario: DM-01 Le champ Pays propose les 18 pays du périmètre
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Quand j'ouvre la liste du champ "Pays"
    Alors la liste propose exactement : France, Maroc, Tunisie, Sénégal, Bénin, Burkina, Cameroun, Congo, Côte d'Ivoire, Gabon, Gambie, Guinée équatoriale, Guinée-Bissau, Mali, Niger, RDC, Tchad, Togo

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: DM-02 En France, les trois types de mandat sont proposés
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Quand je sélectionne "France" dans le champ "Pays"
    Et que j'ouvre la liste du champ "Type de mandat"
    Alors la liste propose exactement : Certification des comptes, Durabilité, Certification des comptes & Durabilité

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: DM-03 Hors France, le type est imposé à Certification des comptes
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Quand je sélectionne "<pays>" dans le champ "Pays"
    Alors le champ "Type de mandat" affiche "Certification des comptes"
    Et le champ "Type de mandat" est désactivé

    Exemples:
      | cas                          | compte     | role       | pays    |
      | Admin, Maghreb               | AD-TEST-01 | Admin      | Maroc   |
      | Admin, Afrique francophone   | AD-TEST-01 | Admin      | Sénégal |
      | SuperAdmin, Maghreb          | SA-TEST-01 | SuperAdmin | Maroc   |
      | SuperAdmin, Afrique francophone | SA-TEST-01 | SuperAdmin | Sénégal |

  Plan du scénario: DM-04 Passer de France à Maroc remplace un type Durabilité
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France" et le Type de mandat "Durabilité"
    Quand je sélectionne "Maroc" dans le champ "Pays"
    Alors le champ "Type de mandat" affiche "Certification des comptes"
    Et le champ "Type de mandat" est désactivé

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: DM-06 La catégorie du mandat propose trois valeurs
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Quand j'ouvre la liste du champ "Catégorie du mandat"
    Alors la liste propose exactement : Nouveau, Reprise, Renouvellement

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: DM-08 Le Pays n'accepte qu'une valeur
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et qu'une demande vierge est ouverte sur la section "Description du mandat"
    Et que j'ai sélectionné le Pays "France"
    Quand je sélectionne "Tunisie" dans le champ "Pays"
    Alors le champ "Pays" affiche uniquement "Tunisie"

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |
```

## 2. Couverture

| Règle de l'US | Scénarios | Couvert ? |
|---|---|---|
| Liste des pays (étape 2) | DM-01 | Couvert |
| RG-DM-01 Champs obligatoires | | Non couvert : moment et forme du contrôle inconnus (Q-21) |
| RG-DM-02 Une seule valeur | DM-08 | Partiel : Pays seulement, Type et Catégorie en exploratoire |
| RG-DM-03 Hors France : Certification imposée | DM-03, DM-04 | Couvert |
| RG-DM-04 France : trois types | DM-02 | Couvert |
| Catégorie : trois valeurs (étape 5) | DM-06 | Couvert ; sens de Reprise à confirmer (Q-22) |
| Règles après RG-DM-04 | | Non couvert : capture coupée |

## 3. Non rédigé

1. Retour de Maroc à France : le type garde « Certification des comptes » ou se vide (Q-20).
2. Champs obligatoires vides : quand le contrôle se déclenche et ce qu'il affiche (Q-21).
3. Catégorie choisie ici (Nouveau, Reprise, Renouvellement), alors que la création demande une Nature (Nouveau, Renouvellement) et une Reprise (Oui, Non) : ces champs se recoupent-ils (Q-22) ?
4. Le filtre de la liste propose « Audit contractuel » comme type de mandat, cette US n'en propose que trois (Q-39).
