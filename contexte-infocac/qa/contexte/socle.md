# Contexte projet : InfoCAC : socle

Socle : Azure DevOps, projet, rôles, comptes de test, objets, statuts, termes, écrans, données de test. Lu par tous les agents.

Fichier lu par l'agent QA avant chaque analyse d'US. Il donne la configuration Azure DevOps, le vocabulaire, les rôles, les statuts, les règles déjà validées et les données de test du projet, pour que chaque US ne soit pas analysée isolément.

| En-tête | Valeur |
|---|---|
| Dernière mise à jour | 30/10/2026 |
| Responsable | QA (à reprendre par l'équipe après la mission) |
| Version | 0.2 |

Règles de tenue du fichier :

1. Une ligne n'entre ici que si elle a une source (US, décision du PO datée, PRD, maquette citée). Sans source, elle va en section 9.
2. Seul l'agent `qc-cas-de-test` écrit dans ces fichiers, après aperçu et « oui ». Un humain relit les différences avant chaque commit.
3. Une règle remplacée n'est pas supprimée : son statut passe à `remplacée` et la colonne « Remplacée par » est remplie.
4. Ce fichier ne remplace jamais l'US en cours : il la complète.
5. C'est une synthèse : une ligne par règle, pas de paragraphe recopié des sources.

Abréviations des sources : « US 417829 §4 » renvoie à la section 4 de l'US ; « S3 » signifie que la règle est connue par les cas de test du sprint 3 (`cas-de-test/sprint-3/`), pas par une lecture directe de l'US.

## 0. Azure DevOps du projet

| Clé | Valeur |
|---|---|
| URL de l'organisation | https://kpmgfr.visualstudio.com |
| Projet Azure DevOps | InfoCAC |
| Plan de test par défaut | 429041 |
| Area Path par défaut | [à compléter] |
| Environnements de recette | Préprod (PPR) uniquement ; pas d'ITG ; préprod partagée avec la recette métier (SRC-01) |

## 1. Le projet en cinq lignes

| Question | Réponse |
|---|---|
| Ce que fait l'application | Tient la liste officielle des mandats de commissariat aux comptes et la transmet aux autres applications ; tout mandat commence par une demande, complétée puis validée (SRC-01) |
| Qui l'utilise | Back-office BSC (Admin), Risk Management et certains BSC (SuperAdmin), collaborateurs KPMG en consultation (User) (SRC-01) |
| Ce qu'elle remplace | La partie mandats d'IBS (SRC-01) |
| Systèmes connectés | Voir section 11 |
| Mise en production | Mars 2027 (SRC-01) |

Périmètre de la recette QA au 26/10/2026 : France et mandats de Certification des comptes uniquement (cas-de-test/sprint-3/README.md). Le sprint 4 remet ce périmètre en question (CONF-S4-10).

## 3. Rôles et droits

| Rôle | Peut faire | Ne peut pas faire | Source | Statut |
|---|---|---|---|---|
| SuperAdmin | Voir le bouton « Nouvelle demande » et créer une demande ; compléter une demande ; modifier après validation, annuler, importer en masse, voir le journal | | US 417829 §1 ; SRC-01 | confirmé |
| Admin | Voir le bouton « Nouvelle demande » et créer une demande ; compléter les demandes de son périmètre | Modifier une demande validée (PRD) | US 417829 §1 ; SRC-01 | confirmé, sauf modification après validation (CONF-02) |
| User | Consulter les données validées | Voir le bouton « Nouvelle demande » ; écrire dans une demande | US 417829 §1 ; SRC-01 ; cas DM-04, DM-05 | confirmé ; visibilité des demandes non validées à trancher (CONF-01) |

Les US désignent les profils habilités de plusieurs façons : « collaborateur habilité à compléter une demande » (426402, 426408, 426409), « utilisateur habilité à créer ou modifier un mandat » (429709), « Admin ou SuperAdmin » (417829, 424890, 429428). Les cas de test lisent les deux premières comme Admin et SuperAdmin (S3, 426402).

Droits gérés par SSO et SailPoint (SRC-01). Règle de test : un droit se vérifie aussi côté serveur, pas seulement par un bouton masqué.

## 4. Connexion et comptes de test

Convention reprise des cas du sprint 3. Les identifiants sont fictifs : les remplacer par les comptes réels de préprod avant l'exécution.

| Compte fictif | Rôle | Environnement | Particularité | Usage |
|---|---|---|---|---|
| AD-TEST-01 | Admin | Préprod | Périmètre France | Création, complétude |
| SA-TEST-01 | SuperAdmin | Préprod | | Création, complétude, actions après validation |
| US-TEST-01 | User | Préprod | | Refus d'écriture, consultation |

Écran d'arrivée après connexion : [à confirmer]. Vérifier le rôle effectif avant chaque campagne : un changement de rôle peut tarder à être pris en compte (`doc/anomalie-changement-role-non-pris-en-compte.md`).

## 5. Objets métier, statuts et transitions

### Objets

| Objet | Définition | Variantes | Source | Statut |
|---|---|---|---|---|
| Demande | Dossier qui deviendra un mandat une fois validé | | SRC-01 | confirmé |
| Entité | Entreprise cliente, identifiée par son Entité ID | Héritée d'InfoCAC (Renouvellement) ; d'InfoCAC ou du référentiel (Nouveau) | US 417829 §3 | confirmé |
| Nature du mandat | Choisie dans le panneau Nouvelle demande | Renouvellement, Nouveau | US 417829 §3 | confirmé ; lien avec la Catégorie à trancher (CONF-05) |
| Catégorie du mandat | Champ de Description du mandat | Nouveau, Reprise, Renouvellement | 426402 (S3) | confirmé |
| Type de mandat | Champ de Description du mandat ; commande les sections affichées | Certification des comptes ; Durabilité ; Certification des comptes & Durabilité | 426402 (S3) ; US 426408 étape 1 ; US 429428 RG-PERSIST-DM-02 | confirmé |
| Engagement | Mission dans le Référentiel Finance, identifiée par un numéro | | 424890 (S3) ; US 429709 | confirmé ; nombre par mandat à trancher (CONF-S4-02) |
| Section du formulaire | Bloc de champs affiché ou masqué selon Pays et Type | Voir section 7 | US 426408 | confirmé |

### Termes et synonymes

Le même objet porte plusieurs noms selon les US. L'agent traite ces termes comme un seul, et signale tout écart de sens.

| Terme retenu | Autres formes dans les sources | Sources |
|---|---|---|
| Affectée à | Affecté à | US 417829 §3 ; US 429428 |
| N° engagement | Numéro d'engagement | US 429709, 429428 ; 424890 (S3) |
| Panneau Nouvelle demande | Side panel, fenêtre Nouvelle demande, formulaire de création | US 417829 §2 ; US 429428 |
| Formulaire de la demande | Page du formulaire | US 417829 §5 ; US 429428 |
| Admin, SuperAdmin | Administrateur, SuperAdministrateur ; collaborateur habilité | Voir section 3 |
| Nature du mandat et Catégorie du mandat | Sens proches, valeurs différentes : non synonymes tant que CONF-05 est ouvert | US 417829 ; 426402 (S3) |

### Statuts

| Objet | Statut affiché | Signification | Source | Statut |
|---|---|---|---|---|
| Demande | En cours | Statut à la création | SRC-01 | confirmé |
| Demande | Analyse OCR | Traitement du PV d'AG | SRC-01 | à confirmer |
| Demande | Retard | Plus de 60 jours sans validation | SRC-01 | confirmé ; testabilité à régler (CONF-S4-17) |
| Demande | Validé | Validée, envoyée aux autres applications | SRC-01 ; US 417829 §4 | confirmé |
| Demande | Révision | Correction après validation, avant revalidation | SRC-01 ; US 417829 §4 | confirmé |
| Demande | Annulé | | SRC-01 | à confirmer |

Liste exacte des statuts à trancher entre le PRD et les US (SRC-01).

### Transitions

| Objet | Statut de départ | Action | Statut d'arrivée | Rôle autorisé | Source | Statut |
|---|---|---|---|---|---|---|
| Demande | (aucune) | Valider la création | En cours | Admin, SuperAdmin | US 417829 §4-5 ; SRC-01 | confirmé |
| Demande | En cours | Aucune validation pendant 60 jours | Retard | Système | SRC-01 | confirmé |
| Demande | Validé | Correction | Révision | SuperAdmin | SRC-01 | confirmé ; Admin à trancher (CONF-02) |

## 7. Écrans

| Écran | Comment on y accède | Ce qu'il affiche | Actions possibles | Source |
|---|---|---|---|---|
| Liste des demandes | Side panel de l'application | Les demandes, recherche par Entité ID, filtres | « Nouvelle demande » (Admin, SuperAdmin) | US 417829 §1 ; 425530 (S3) |
| Panneau Nouvelle demande | Bouton « Nouvelle demande » ; s'ouvre à droite, la liste reste visible | Nature du mandat, Entité ID, Reprise (Nouveau), N° Requête BSC, Affectée à, Millésime ; N° engagement depuis le sprint 3 | « Valider la création » | US 417829 §2-3 ; 424890 (S3) ; champs à jour : CONF-S4-05 |
| Formulaire de la demande, en-tête | Redirection après création, ou ouverture depuis la liste | Nom de l'entité, Entité ID, statut, titre, sous-titre, affectation | Bouton Retour | 422727, 427092 (S3) ; US 429428 |
| Section Description du mandat | Formulaire | Pays, Type de mandat, Catégorie, indicateurs DA, taxonomie, catégorie d'entité, AGP, Type d'EIP, marchés de cotation ; N° engagement et Affectée à (sprint 4) | Saisie avec sauvegarde automatique | 426402 à 426407 (S3) ; US 426409 ; US 429709 ; US 429428 |
| Sections Informations mandat Certification, Informations mandat Durabilité, Informations de l'entité, Référentiel et Normes, Audit contractuel | Formulaire, selon Pays et Type de mandat | Contenu non décrit à ce jour | | US 426408 RG-SEC-01, 02 |
| Gestion d'entité | | | Retour depuis un formulaire validé | 422727 (S3) |

Ne pas déduire l'existence d'un export, d'une recherche, d'une API ou d'une pièce jointe qui n'est pas citée par une source.

## 8. Données de test

Toutes les données sont fictives. Elles ne créent aucune règle métier. Le détail des données du sprint 3 est dans `cas-de-test/sprint-3/README.md`.

| ID fictif | Objet | État | Particularité utile aux tests |
|---|---|---|---|
| ENT-ENG-01 à 08, ENT-CTRL-01 à 05 | Entités France | Sans demande | Consommées par chaque création réussie : une par exécution |
| ENT-ENG-12, DEM-TEST-01 | Entité et demande | Validé, engagement 1021002 | À injecter par un développeur |
| DEM-TEST-04 | Demande | Validé, France, Certification des comptes, Nouveau | À injecter par un développeur |
| 9999999 | Numéro d'engagement | Absent du Référentiel Finance | Cas de refus |
| [à créer] | Demande | Retard (plus de 60 jours sans validation) | Pour RT-01 ; voir CONF-S4-17 |
| [à créer] | Demande France avec des données dans les sections Durabilité et Référentiel et Normes | En cours | Pour RT-05 (426408) ; suppose le Type Durabilité accessible (CONF-S4-10) |
