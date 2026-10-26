# US Contrôles à la création d'une demande (Entité ID, engagement, requête BSC)

Sources : texte de l'US collé dans Copilot (captures du 23/10/2026, identifiant Azure DevOps non visible), cas de création existants (`../creer-une-demande.md`). Données fictives uniquement.

Profils habilités : « utilisateur habilité à créer une demande », soit Admin et SuperAdmin.

Attention : cette US contredit deux cas déjà écrits pour la création. TC06 bloque une Entité ID inconnue avec le message « entité ID inconnue », cette US dit « aucun blocage ». TC07 refuse une deuxième demande pour une entité qui en a déjà une en cours, cette US dit « aucun contrôle d'unicité ». Ces deux règles ne sont pas rédigées tant que le PO n'a pas tranché (Q-19).

Les règles sur le numéro d'engagement sont couvertes par `US-424890-numero-engagement.md`.

## 1. Scénarios

```gherkin
# language: fr
Fonctionnalité: Contrôles des informations saisies à la création d'une demande

  Plan du scénario: CTRL-03 L'Entité ID propose les entités connues en autocomplétion
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que l'entité "ENT-CTRL-01" existe dans le référentiel
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Quand je saisis "ENT-CTRL" dans le champ "Entité ID"
    Alors la suggestion "ENT-CTRL-01" est affichée

    Exemples:
      | cas             | compte     | role       |
      | rôle Admin      | AD-TEST-01 | Admin      |
      | rôle SuperAdmin | SA-TEST-01 | SuperAdmin |

  Plan du scénario: CTRL-04 La requête BSC ne bloque jamais la création
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que la demande "DEM-TEST-01" porte la requête BSC "BSC-TEST-01"
    Et que le formulaire de création est ouvert depuis la "Liste des demandes"
    Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau" et l'Entité ID "<entite>", avec la requête BSC "<requete>"
    Quand je clique sur "Valider la création"
    Alors une demande pour l'entité "<entite>" apparaît dans la "Liste des demandes"
    Et la requête BSC de cette demande est "<requete>"

    Exemples:
      | cas                                   | compte     | role       | entite      | requete     |
      | Admin, requête déjà utilisée          | AD-TEST-01 | Admin      | ENT-CTRL-02 | BSC-TEST-01 |
      | Admin, requête nouvelle               | AD-TEST-01 | Admin      | ENT-CTRL-03 | BSC-TEST-02 |
      | SuperAdmin, requête déjà utilisée     | SA-TEST-01 | SuperAdmin | ENT-CTRL-04 | BSC-TEST-01 |
      | SuperAdmin, requête nouvelle          | SA-TEST-01 | SuperAdmin | ENT-CTRL-05 | BSC-TEST-03 |
```

## 2. Couverture

| Règle de l'US | Scénarios | Couvert ? |
|---|---|---|
| Entité ID obligatoire | TC05 de `creer-une-demande.md` | Couvert ailleurs |
| Entité ID en autocomplétion | CTRL-03 | Couvert |
| Entité ID inconnue non bloquante | | Non couvert : contradiction avec TC06 (Q-19) |
| Entité ID sans contrôle d'unicité | | Non couvert : contradiction avec TC07 (Q-19) |
| Requête BSC libre, sans unicité | CTRL-04 | Couvert |
| Requête BSC facultative | | Non couvert : TC05 traite N° Requête BSC comme obligatoire (Q-19) |
| Numéro d'engagement | Fichier 424890 | Couvert ailleurs ; texte du message en conflit (Q-13) |

## 3. Non rédigé

1. Entité ID inconnue acceptée, et plusieurs demandes pour une même Entité ID : à arbitrer contre TC06 et TC07 (Q-19).
2. Requête BSC facultative : TC05 la traite comme obligatoire (Q-19).
3. Message d'engagement déjà existant : « Un engagement étant déjà existant, il n'est pas possible de créer une demande. » ici, deux messages différents dans 424890 (Q-13).
