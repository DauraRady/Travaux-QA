# InfoCAC : cas de test Gherkin, sprints 1 et 2

Version du 13/10/2026. 33 scénarios pour les 3 US des sprints 1 et 2.

| Code | US Azure DevOps | Nominal | Négatif | Cas limites |
|---|---|---|---|---|
| S1-01 | Ouvrir la side panel Discovery et voir les features | 3 | 3 | 4 |
| S1-02 | Créer une nouvelle demande | 3 | 4 | 6 |
| S1-03 | Création des groupes de sécurité | 3 | 4 | 3 |

Les codes S1-01, S1-02 et S1-03 sont des codes de travail. Pour le lien Tests dans Azure DevOps, utilise le vrai numéro de l'US.

## Comptes et données de test (fictifs, en ITG)

| Compte | Rôle | Périmètre |
|---|---|---|
| AD-TEST-01 | Admin | France |
| AD-TEST-02 | Admin | Maroc |
| SA-TEST-01 | Super Admin | FMA |
| US-TEST-01 | User | Lecture FMA |
| NR-TEST-01 | Aucun rôle InfoCAC, SSO valide | Aucun |
| MX-TEST-01 | Membre des groupes Admin et User | France |

| Donnée | Contenu |
|---|---|
| ENT-TEST-01 | Entité France connue du référentiel, sans demande |
| ENT-TEST-02 | Entité France ayant déjà une demande en cours |
| ENT-MA-01 | Entité marocaine connue du référentiel |
| N | Millésime courant affiché en ITG le jour de la campagne, à relever avant de commencer |

## Tags

| Tag | Sens |
|---|---|
| @nominal, @negatif, @limite | Type de cas (Nominal, Négatif, Cas limites dans le patrimoine) |
| @P0, @P1, @P2 | Priorité 1, 2, 3 dans Azure DevOps |
| @smoke | À jouer en premier à chaque livraison |
| @api | Vérifier aussi par un appel direct au serveur |
| @question-Qx | Résultat attendu à confirmer : voir la liste des questions en fin de fichier. Cas en état Design tant que la réponse manque |

---

## S1-01 Ouvrir la side panel Discovery et voir les features

```gherkin
# language: fr
Fonctionnalité: S1-01 Ouvrir la side panel Discovery et voir les features

  # ---------- NOMINAL ----------

  @nominal @P0 @smoke
  Plan du scénario: REC-DIS-01 Le panel affiche les fonctions d'un profil autorisé à créer
    Étant donné que je suis connecté avec le compte <compte>
    Quand j'ouvre la side panel Discovery
    Alors je vois les entrées "Nouvelle demande", "Paramètres" et "Déconnexion"

    Exemples:
      | compte     |
      | AD-TEST-01 |
      | SA-TEST-01 |

  @nominal @P1
  Scénario: REC-DIS-02 Les paramètres affichent mon identité et mon rôle
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand j'ouvre "Paramètres" depuis la side panel
    Alors je vois le nom du compte AD-TEST-01
    Et je vois le rôle "Admin"

  @nominal @P1
  Scénario: REC-DIS-03 Se déconnecter depuis la side panel
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand je clique sur "Déconnexion" dans la side panel
    Alors la page d'authentification SSO s'affiche

  # ---------- NÉGATIF ----------

  @negatif @P0 @question-Q5
  Scénario: REC-DIS-04 Le User ne voit pas les fonctions d'écriture
    Étant donné que je suis connecté avec le compte US-TEST-01
    Quand j'ouvre la side panel Discovery
    Alors l'entrée "Nouvelle demande" est absente
    Et l'entrée "Liste des demandes" est absente

  @negatif @P0 @api @question-Q1
  Scénario: REC-DIS-05 Un compte sans rôle InfoCAC n'a accès à rien
    Étant donné que je suis authentifié par le SSO avec le compte NR-TEST-01
    Quand j'ouvre InfoCAC depuis le portail Discovery
    Alors un message m'indique que je n'ai pas de droit sur InfoCAC
    Et la side panel ne propose aucune fonction InfoCAC
    Et l'API refuse mes appels de lecture des demandes

  @negatif @P0 @api
  Scénario: REC-DIS-06 Après déconnexion, le bouton Précédent ne rouvre pas la session
    Étant donné que je me suis connecté avec le compte AD-TEST-01 puis déconnecté depuis la side panel
    Quand j'utilise le bouton Précédent du navigateur
    Alors aucune page InfoCAC utilisable ne s'affiche
    Et toute action me renvoie vers l'authentification SSO

  # ---------- CAS LIMITES ----------

  @limite @P1
  Scénario: REC-DIS-07 Session expirée au moment de cliquer dans la side panel
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Et que ma session a expiré pendant une pause
    Quand je clique sur "Nouvelle demande" dans la side panel
    Alors je suis redirigé vers l'authentification SSO
    Et aucune erreur technique brute ne s'affiche
    Et après reconnexion je peux ouvrir "Nouvelle demande"

  @limite @P0 @question-Q8
  Scénario: REC-DIS-08 Un rôle retiré dans SailPoint disparaît du panel
    Étant donné que le rôle Admin du compte MX-TEST-01 a été retiré dans SailPoint
    Et que le délai de prise en compte annoncé est écoulé
    Quand je me reconnecte avec le compte MX-TEST-01 et que j'ouvre la side panel
    Alors l'entrée "Nouvelle demande" est absente

  @limite @P1
  Scénario: REC-DIS-09 Déconnexion dans un onglet alors qu'un autre onglet est ouvert
    Étant donné que InfoCAC est ouvert dans deux onglets avec le compte AD-TEST-01
    Quand je me déconnecte dans le premier onglet
    Et que j'ouvre "Nouvelle demande" dans le second onglet
    Alors je suis redirigé vers l'authentification SSO

  @limite @P2
  Scénario: REC-DIS-10 Panel utilisable sur un écran de portable avec zoom
    Étant donné que mon navigateur est à la résolution 1366 x 768 avec un zoom de 150 %
    Et que je suis connecté avec le compte AD-TEST-01
    Quand j'ouvre la side panel Discovery
    Alors toutes les entrées sont visibles ou accessibles par défilement
    Et aucun libellé n'est coupé au point d'être illisible
```

---

## S1-02 Créer une nouvelle demande

```gherkin
# language: fr
Fonctionnalité: S1-02 Créer une nouvelle demande

  # ---------- NOMINAL ----------

  @nominal @P0 @smoke @api
  Scénario: REC-CRE-01 L'Admin crée une demande au millésime courant
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand je crée une demande pour l'Entité ID ENT-TEST-01 au millésime N
    Alors un message confirme la création
    Et l'API renvoie une seule demande pour ENT-TEST-01, au millésime N, créée par AD-TEST-01 à la date du jour

  @nominal @P1 @api
  Scénario: REC-CRE-02 Le Super Admin crée une demande
    Étant donné que je suis connecté avec le compte SA-TEST-01
    Quand je crée une demande pour l'Entité ID ENT-TEST-01 au millésime N
    Alors un message confirme la création
    Et l'API renvoie la demande, créée par SA-TEST-01

  @nominal @P1 @api
  Scénario: REC-CRE-03 Créer une demande sur le millésime suivant
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand je crée une demande pour l'Entité ID ENT-TEST-01 au millésime N+1
    Alors l'API renvoie la demande au millésime N+1

  # ---------- NÉGATIF ----------

  @negatif @P0 @api
  Plan du scénario: REC-CRE-04 Pas de demande sans Entité ID
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand je tente de créer une demande avec l'Entité ID "<saisie>"
    Alors la création est impossible et un message nomme le champ Entité ID
    Et l'API ne contient aucune demande sans Entité ID

    Exemples:
      | saisie          |
      | (champ vide)    |
      | (trois espaces) |

  @negatif @P0 @api @question-Q3
  Plan du scénario: REC-CRE-05 Millésime hors de la fenêtre autorisée
    Étant donné que je suis connecté avec le compte <compte>
    Quand je tente de créer une demande pour ENT-TEST-01 au millésime <millesime>
    Alors la création est refusée avec un message qui nomme la fenêtre autorisée

    Exemples:
      | compte     | millesime |
      | AD-TEST-01 | N-1       |
      | AD-TEST-01 | N+3       |
      | SA-TEST-01 | N-3       |
      | SA-TEST-01 | N-20      |
    # Le PRD (FR-22) autorise N-2 à N+2, et seulement N à N+2 pour l'Admin. S1-02 parle de -20 à +10.

  @negatif @P1 @question-Q4
  Scénario: REC-CRE-06 Le nom de l'entité collé à la place de son identifiant
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand je tente de créer une demande avec l'Entité ID "SOCIETE EXEMPLE SA"
    Alors la création est refusée avec un message sur le format de l'Entité ID

  @negatif @P0 @securite
  Scénario: REC-CRE-07 Un texte malveillant dans l'Entité ID n'est jamais exécuté
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand je tente de créer une demande avec l'Entité ID "<script>alert(1)</script>"
    Alors aucune fenêtre d'alerte ne s'ouvre
    Et aucune erreur technique brute ne s'affiche

  # ---------- CAS LIMITES ----------

  @limite @P0 @api
  Scénario: REC-CRE-08 Entité ID copiée depuis ServiceNow avec des espaces
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand je crée une demande en collant "  ENT-TEST-01 " suivi d'un retour à la ligne dans le champ Entité ID
    Alors la demande est rattachée à ENT-TEST-01, sans espace ni retour à la ligne enregistré

  @limite @P0 @api
  Scénario: REC-CRE-09 Un double clic sur le bouton de création
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand je saisis ENT-TEST-01 et que je clique deux fois très vite sur le bouton de création
    Alors une seule confirmation s'affiche
    Et l'API renvoie une seule demande pour ENT-TEST-01

  @limite @P0 @question-Q2
  Scénario: REC-CRE-10 Une deuxième demande pour une entité qui en a déjà une en cours
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Quand je crée une demande pour ENT-TEST-02
    Alors un avertissement signale la demande déjà en cours, avec sa référence
    Et je peux confirmer ou abandonner la création
    # Le PRD (FR-60) interdit le blocage automatique d'un doublon. S1-02 parle de contrôle des doublons sans dire s'il bloque.

  @limite @P0 @api @question-Q2
  Scénario: REC-CRE-11 Deux BSC créent une demande pour la même entité en même temps
    Étant donné que AD-TEST-01 et SA-TEST-01 ont chacun saisi ENT-TEST-01 dans le panneau de création
    Quand ils cliquent sur le bouton de création dans la même seconde
    Alors le second reçoit le même avertissement de doublon que dans REC-CRE-10
    Et l'API ne renvoie jamais deux demandes créées sans avertissement

  @limite @P1
  Scénario: REC-CRE-12 Session expirée pendant la saisie
    Étant donné que je suis connecté avec le compte AD-TEST-01
    Et que j'ai saisi ENT-TEST-01 dans le panneau de création
    Et que ma session a expiré
    Quand je clique sur le bouton de création
    Alors un message m'invite à me reconnecter
    Et après reconnexion, l'API renvoie zéro ou une demande pour ENT-TEST-01, jamais deux

  @limite @P1 @question-Q9
  Scénario: REC-CRE-13 Millésime proposé après le changement d'exercice
    Étant donné que la date du jour est postérieure au 1er octobre
    Et que je suis connecté avec le compte AD-TEST-01
    Quand j'ouvre le panneau de création
    Alors le millésime proposé par défaut est celui du nouvel exercice
```

---

## S1-03 Création des groupes de sécurité

```gherkin
# language: fr
Fonctionnalité: S1-03 Création des groupes de sécurité

  # ---------- NOMINAL ----------

  @nominal @P0 @smoke
  Plan du scénario: REC-SEC-01 Chaque compte reçoit le rôle de son groupe
    Étant donné que je suis connecté avec le compte <compte>
    Quand j'ouvre "Paramètres" depuis la side panel
    Alors le rôle affiché est "<role>"

    Exemples:
      | compte     | role        |
      | SA-TEST-01 | Super Admin |
      | AD-TEST-01 | Admin       |
      | US-TEST-01 | User        |

  @nominal @P0 @api
  Scénario: REC-SEC-02 L'Admin crée une demande dans son périmètre
    Étant donné que je suis connecté avec le compte AD-TEST-01 (périmètre France)
    Quand je crée une demande pour l'entité française ENT-TEST-01
    Alors un message confirme la création
    Et la demande existe pour ENT-TEST-01, créée par AD-TEST-01

  @nominal @P0 @api
  Scénario: REC-SEC-03 Le Super Admin crée une demande pour n'importe quel pays
    Étant donné que je suis connecté avec le compte SA-TEST-01
    Quand je crée une demande pour l'entité marocaine ENT-MA-01
    Alors un message confirme la création
    Et la demande existe pour ENT-MA-01, créée par SA-TEST-01

  # ---------- NÉGATIF ----------

  @negatif @P0 @api
  Scénario: REC-SEC-04 Le User ne peut pas créer de demande, même sans passer par l'écran
    Étant donné que je suis connecté avec le compte US-TEST-01
    Quand j'ouvre directement l'adresse de la page de création relevée avec AD-TEST-01
    Et que j'envoie une création pour ENT-TEST-01 par l'API avec mon jeton
    Alors la page de création ne s'affiche pas
    Et l'API refuse la création (code 403)
    Et aucune demande n'est créée pour ENT-TEST-01

  @negatif @P0 @api @question-Q1
  Scénario: REC-SEC-05 Un compte sans groupe ne peut rien faire
    Étant donné que je suis authentifié par le SSO avec le compte NR-TEST-01
    Quand j'envoie une création pour ENT-TEST-01 par l'API avec mon jeton
    Alors l'API refuse la création (code 403)
    Et aucune demande n'est créée pour ENT-TEST-01

  @negatif @P0 @api
  Scénario: REC-SEC-06 L'Admin France ne crée pas de demande pour une entité marocaine
    Étant donné que je suis connecté avec le compte AD-TEST-01 (périmètre France)
    Quand je tente de créer une demande pour ENT-MA-01, à l'écran puis par l'API
    Alors la création est refusée avec un message explicite
    Et aucune demande n'est créée pour ENT-MA-01

  @negatif @P0 @api @question-Q6
  Scénario: REC-SEC-07 L'Admin ne modifie pas une demande validée
    Étant donné qu'une demande validée existe pour ENT-TEST-02 (injectée en base, la validation n'étant pas livrée)
    Et que je suis connecté avec le compte AD-TEST-01
    Quand je tente de modifier cette demande par l'API
    Alors l'API refuse la modification (code 403)
    # Le PRD (FR-20) réserve la correction après validation au Super Admin. L'AC3 de S1-03 l'autorise à l'Admin.

  # ---------- CAS LIMITES ----------

  @limite @P0 @question-Q10
  Scénario: REC-SEC-08 Un compte présent dans deux groupes
    Étant donné que le compte MX-TEST-01 est membre des groupes Admin et User
    Quand je me connecte avec MX-TEST-01
    Alors le rôle affiché et les fonctions disponibles sont ceux décidés pour ce cas
    Et l'écran et l'API donnent les mêmes droits

  @limite @P0 @api @question-Q8
  Scénario: REC-SEC-09 Un rôle retiré pendant que l'utilisateur travaille
    Étant donné que je suis connecté avec le compte MX-TEST-01 et que le panneau de création est ouvert
    Et que son rôle Admin est retiré dans SailPoint
    Et que le délai de prise en compte annoncé est écoulé
    Quand je clique sur le bouton de création pour ENT-TEST-01
    Alors la création est refusée
    Et aucune demande n'est créée pour ENT-TEST-01

  @limite @P0 @api @securite
  Scénario: REC-SEC-10 Un User ne s'attribue pas de droits en modifiant sa requête
    Étant donné que je dispose d'un jeton du compte US-TEST-01
    Quand j'envoie une création par l'API en ajoutant les champs "role" = "Admin" et "statut" = "Validated"
    Alors l'API refuse la création (code 403)
    Et mon rôle reste "User" à la connexion suivante
```

---

## Ordre de jeu (par le risque)

| Vague | Scénarios |
|---|---|
| 1, dès la livraison | CRE-01, CRE-04, CRE-05, CRE-08, CRE-09, CRE-10, CRE-11, SEC-04, SEC-05, SEC-06, SEC-07, SEC-10, DIS-04, DIS-05 |
| 2, couverture complète | SEC-01, SEC-02, SEC-03, SEC-08, SEC-09, CRE-02, CRE-03, CRE-06, CRE-07, CRE-12, CRE-13, DIS-01, DIS-06, DIS-08 |
| 3, s'il reste du temps | DIS-02, DIS-03, DIS-07, DIS-09, DIS-10 |

## Questions à poser

| # | Question | Cas bloqués | À qui |
|---|---|---|---|
| Q1 | Que voit un compte authentifié par le SSO mais sans rôle InfoCAC : message, page, code de refus de l'API ? | DIS-05, SEC-05 | PO |
| Q2 | Une deuxième demande pour une entité qui en a déjà une en cours est-elle bloquée (S1-02) ou seulement signalée (PRD FR-60) ? | CRE-10, CRE-11 | PO |
| Q3 | Quelle fenêtre de millésime à la création : -20 à +10 (S1-02) ou N-2 à N+2, et N à N+2 pour l'Admin (PRD FR-22) ? | CRE-05 | PO, Risk Management |
| Q4 | Le format de l'Entité ID est-il contrôlé dès S1-02 ? | CRE-06 | PO |
| Q5 | Le User voit-il l'entrée « Liste des demandes » (US-17) ou non (PRD FR-1) ? | DIS-04 | Risk Management |
| Q6 | L'Admin peut-il modifier une demande validée (AC3 de S1-03) ou est-ce réservé au Super Admin (PRD FR-20) ? | SEC-07 | Risk Management |
| Q7 | Tant que la liste des demandes n'est pas livrée, comment vérifier qu'une demande existe ? | Tous les cas @api | Développeur |
| Q8 | Quel délai entre le retrait d'un rôle dans SailPoint et sa prise en compte ? | DIS-08, SEC-09 | ITS, sécurité |
| Q9 | À quelle date et heure le millésime courant change-t-il, et quel est son libellé ? | CRE-13 | PO |
| Q10 | Quels droits pour un compte membre de deux groupes ? | SEC-08 | Sécurité |
