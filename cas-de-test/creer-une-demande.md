# Créer une nouvelle demande : cas de test

Données fictives (comptes AD-TEST-01, entités ENT-TEST-xx) à remplacer par les données de test réelles. Les valeurs commençant par @ sont des paramètres : leurs valeurs sont dans le tableau sous chaque cas.

## TC01 : Créer une demande Nouveau de bout en bout

Tags : US-creation; AC-1; AC-3; positif; parcours-2; parcours

| # | Action | Expected result |
|---|---|---|
| 1 | Étant donné que je suis connecté avec le compte @compte ayant le rôle @role |  |
| 2 | Et que l'entité @entite n'a aucune demande |  |
| 3 | Quand je clique sur le bouton "Nouvelle demande" dans la "Liste des demandes" | Alors un panneau latéral s'ouvre à droite de l'écran<br>Et le formulaire de création est affiché<br>Et la "Liste des demandes" reste visible en arrière-plan |
| 4 | Quand je sélectionne la Nature du mandat "Nouveau" | Alors les champs Entité ID, Reprise, N° Requête BSC, Affectée à et Millésime sont affichés<br>Et "Affectée à" contient le nom du compte @compte<br>Et "Millésime" contient l'année fiscale en cours (règle de l'US sur les dates) |
| 5 | Et je renseigne Entité ID = @entite, Reprise = "Non", N° Requête BSC = @requete, sans modifier Affectée à ni Millésime |  |
| 6 | Quand je clique sur "Valider la création" | Alors le message de confirmation de la maquette Figma est affiché<br>Et je suis redirigée vers la page du formulaire de la demande créée<br>Et la demande de l'entité @entite est au statut "En cours" |

Paramètres :

| compte | role | entite | requete |
|---|---|---|---|
| AD-TEST-01 | Admin | ENT-TEST-01 | BSC-TEST-0001 |
| SA-TEST-01 | SuperAdmin | ENT-TEST-02 | BSC-TEST-0002 |

## TC02 : Créer un Renouvellement pour une entité qui a un mandat précédent

Tags : US-creation; AC-3; positif; parcours-1; parcours

| # | Action | Expected result |
|---|---|---|
| 1 | Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin" |  |
| 2 | Et que l'entité @entite existe dans l'application et a un mandat précédent (demande au statut "Validé") |  |
| 3 | Quand je clique sur le bouton "Nouvelle demande" dans la "Liste des demandes" | Alors un panneau latéral s'ouvre à droite de l'écran<br>Et le formulaire de création est affiché<br>Et la "Liste des demandes" reste visible en arrière-plan |
| 4 | Quand je sélectionne la Nature du mandat "Renouvellement" | Alors les champs Entité ID, N° Requête BSC, Affectée à et Millésime sont affichés<br>Et le champ "Reprise" n'est pas affiché<br>Et "Affectée à" contient le nom du compte "AD-TEST-01"<br>Et "Millésime" contient l'année fiscale en cours (règle de l'US sur les dates) |
| 5 | Quand j'ouvre la liste déroulante "Millésime" | Alors la première valeur proposée est N-20 et la dernière N+10, N étant l'année fiscale en cours |
| 6 | Et je renseigne Entité ID = @entite, N° Requête BSC = @requete, sans modifier Affectée à ni Millésime |  |
| 7 | Quand je clique sur "Valider la création" | Alors le message de confirmation de la maquette Figma est affiché<br>Et je suis redirigée vers la page du formulaire de la demande créée<br>Et la demande de l'entité @entite est au statut "En cours" |

Paramètres :

| entite | requete |
|---|---|
| ENT-TEST-03 | BSC-TEST-0003 |
| ENT-TEST-04 | BSC-TEST-0004 |

## TC03 : Un utilisateur User ne peut pas créer de demande

Tags : US-creation; AC-2; negatif; droits; a-confirmer

| # | Action | Expected result |
|---|---|---|
| 1 | Étant donné que je suis connecté avec le compte "US-TEST-01" ayant le rôle "User" |  |
| 2 | Quand j'accède à l'écran "Liste des demandes" | Alors le bouton "Nouvelle demande" n'est pas visible |
| 3 | Quand j'ouvre l'adresse directe de l'écran de création (relevée avec un compte Admin) | Alors la page "Accès refusé" s'affiche avec "Erreur 403" et le texte "Vous ne disposez pas des autorisations nécessaires pour accéder à cette ressource."<br>(Étape à confirmer : question Q7) |

## TC04 : Fermer le panneau de création ne crée aucune demande

Tags : US-creation; AC-4; positif

| # | Action | Expected result |
|---|---|---|
| 1 | Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin" |  |
| 2 | Et que le formulaire de création est ouvert depuis la "Liste des demandes" |  |
| 3 | Et que j'ai sélectionné la Nature du mandat "Nouveau" et l'Entité ID "ENT-TEST-05" |  |
| 4 | Quand je clique sur l'action de fermeture du panneau | Alors le panneau est fermé<br>Et je suis toujours sur la "Liste des demandes"<br>Et aucune demande n'apparaît pour l'entité "ENT-TEST-05" |

## TC05 : Un champ obligatoire vide bloque la création

Tags : US-creation; negatif; partitions

| # | Action | Expected result |
|---|---|---|
| 1 | Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin" |  |
| 2 | Et que le formulaire de création est ouvert depuis la "Liste des demandes" |  |
| 3 | Et que j'ai renseigné tous les champs pour la Nature du mandat @nature et l'Entité ID "ENT-TEST-06", sauf le champ @champ laissé vide |  |
| 4 | Quand je clique sur "Valider la création" | Alors la demande n'est pas initiée<br>Et le ou les champs vides (@champ) sont signalés en erreur<br>Et un message explicite est affiché (texte de la maquette Figma)<br>Et aucune demande n'apparaît pour l'entité "ENT-TEST-06" |

Paramètres :

| nature | champ |
|---|---|
| Nouveau | Entité ID |
| Nouveau | Reprise |
| Nouveau | N° Requête BSC |
| Nouveau | Affectée à |
| Renouvellement | Entité ID |
| Renouvellement | N° Requête BSC |
| Renouvellement | Affectée à |
| Nouveau | tous les champs |

## TC06 : Une Entité ID inconnue bloque la création

Tags : US-creation; negatif; parcours-2

| # | Action | Expected result |
|---|---|---|
| 1 | Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin" |  |
| 2 | Et que le formulaire de création est ouvert depuis la "Liste des demandes" |  |
| 3 | Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau", avec l'Entité ID "ENT-BSC-99" (entité connue de BSC et d'Engage, mais absente du référentiel) |  |
| 4 | Quand je clique sur "Valider la création" | Alors le champ "Entité ID" est surligné en rouge et son titre est affiché en rouge<br>Et le message "entité ID inconnue" est affiché sous le champ<br>Et aucune demande n'apparaît pour l'entité "ENT-BSC-99" |

## TC07 : La création est refusée si l'entité a déjà une demande en cours, en retard ou en révision

Tags : US-creation; negatif; transition-etat

| # | Action | Expected result |
|---|---|---|
| 1 | Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin" |  |
| 2 | Et que l'entité @entite a une demande au statut @statut |  |
| 3 | Et que le formulaire de création est ouvert depuis la "Liste des demandes" |  |
| 4 | Et que j'ai renseigné tous les champs pour la Nature du mandat "Renouvellement", avec l'Entité ID @entite |  |
| 5 | Quand je clique sur "Valider la création" | Alors le message d'erreur de la maquette Figma est affiché<br>Et aucune nouvelle demande n'est créée pour l'entité @entite<br>Et la demande existante de l'entité @entite est toujours au statut @statut |

Paramètres :

| entite | statut |
|---|---|
| ENT-TEST-07 | En cours |
| ENT-TEST-08 | Retard |
| ENT-TEST-09 | Révision |

## TC08 : Une erreur technique à l'enregistrement ne crée pas de demande et conserve la saisie

Tags : US-creation; negatif; robustesse; env-requis

| # | Action | Expected result |
|---|---|---|
| 1 | Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin" |  |
| 2 | Et que le formulaire de création est ouvert depuis la "Liste des demandes" |  |
| 3 | Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau", avec l'Entité ID "ENT-TEST-10" |  |
| 4 | Et qu'une erreur technique est provoquée à l'enregistrement (avec l'équipe de développement : service arrêté ou réponse en erreur simulée) |  |
| 5 | Quand je clique sur "Valider la création" | Alors un message d'erreur est affiché (texte de la maquette Figma)<br>Et les champs saisis sont toujours remplis<br>Et aucune demande n'apparaît pour l'entité "ENT-TEST-10" |

## TC09 : Un double clic sur Valider la création ne crée qu'une seule demande

Tags : US-creation; edge_case; robustesse

| # | Action | Expected result |
|---|---|---|
| 1 | Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin" |  |
| 2 | Et que l'entité "ENT-TEST-11" n'a aucune demande |  |
| 3 | Et que le formulaire de création est ouvert depuis la "Liste des demandes" |  |
| 4 | Et que j'ai renseigné tous les champs pour la Nature du mandat "Nouveau", avec l'Entité ID "ENT-TEST-11" |  |
| 5 | Quand je clique deux fois de suite, rapidement, sur "Valider la création" | Alors le bouton "Valider la création" est désactivé pendant le traitement<br>Et une seule demande existe pour l'entité "ENT-TEST-11" |
