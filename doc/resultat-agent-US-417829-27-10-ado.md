| ID | Test case | Gherkin BDD scenario | Type of test |
|---|---|---|---|
| TC-001 | Le bouton "Nouvelle demande" n'est affiché que pour les rôles Admin et SuperAdmin | Étant donné que l'utilisateur "@compte" est connecté avec le rôle "@role"<br>Quand il ouvre la page "Liste des demandes"<br>Alors la "Liste des demandes" s'affiche<br>Et le bouton "Nouvelle demande" @affichage | Fonctionnel |
| TC-002 | Le panneau de création s'ouvre à droite de la liste | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Quand il clique sur "Nouvelle demande"<br>Alors un panneau latéral s'affiche à droite de l'écran<br>Et le formulaire de création d'une demande est affiché dans le panneau<br>Et la "Liste des demandes" reste visible en arrière-plan | UI |
| TC-003 | Le champ "Nature du mandat" propose deux valeurs | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que le panneau de création est ouvert<br>Quand il consulte les valeurs du champ "Nature du mandat"<br>Alors le champ "Nature du mandat" propose la valeur "Renouvellement"<br>Et le champ "Nature du mandat" propose la valeur "Nouveau" | Fonctionnel |
| TC-004 | La nature Renouvellement affiche quatre champs et pas le champ Reprise | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que le panneau de création est ouvert<br>Quand il sélectionne la nature "Renouvellement"<br>Alors le formulaire affiche les champs "Entité ID", "N° Requête BSC", "Affectée à" et "Millésime"<br>Mais le champ "Reprise" n'est pas affiché | Fonctionnel |
| TC-005 | La nature Nouveau affiche en plus le champ Reprise | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que le panneau de création est ouvert<br>Quand il sélectionne la nature "Nouveau"<br>Alors le formulaire affiche les champs "Entité ID", "Reprise", "N° Requête BSC", "Affectée à" et "Millésime"<br>Et le champ "Reprise" propose la valeur "Oui"<br>Et le champ "Reprise" propose la valeur "Non" | Fonctionnel |
| TC-006 | Le champ "Entité ID" n'accepte pas de code saisi librement | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"<br>Quand il saisit le code "ENT-LIBRE-99" dans le champ "Entité ID"<br>Alors le code "ENT-LIBRE-99" n'est pas retenu comme valeur du champ "Entité ID" | Fonctionnel |
| TC-007 | Le champ "N° Requête BSC" accepte une saisie libre | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"<br>Quand il saisit "BSC-TEST-01" dans le champ "N° Requête BSC"<br>Alors le champ "N° Requête BSC" affiche "BSC-TEST-01" | Fonctionnel |
| TC-008 | Le champ "Affectée à" propose par défaut le nom du compte connecté | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que le nom du compte "ADM-TEST-01" est "Admin Test"<br>Quand il clique sur "Nouvelle demande"<br>Et qu'il sélectionne la nature "@nature"<br>Alors le champ "Affectée à" affiche "Admin Test" | Fonctionnel |
| TC-009 | Le champ "Affectée à" accepte le nom d'un collaborateur connu | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que le collaborateur "Collaborateur Test" est connu des collaborateurs KPMG<br>Et que le panneau de création est ouvert avec la nature "Renouvellement"<br>Quand il renseigne "Collaborateur Test" dans le champ "Affectée à"<br>Alors le champ "Affectée à" affiche "Collaborateur Test" | Fonctionnel |
| TC-010 | Le champ "Millésime" s'ouvre sur l'année fiscale en cours | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Quand il clique sur "Nouvelle demande"<br>Et qu'il sélectionne la nature "@nature"<br>Alors le champ "Millésime" affiche l'année fiscale en cours | Fonctionnel |
| TC-011 | Les bornes de la liste "Millésime" pour un Renouvellement | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que le panneau de création est ouvert avec la nature "Renouvellement"<br>Quand il ouvre la liste du champ "Millésime"<br>Alors le millésime "@millesime" est proposé dans la liste | Fonctionnel |
| TC-012 | Un champ obligatoire vide bloque la création | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que l'entité "ENT-TEST-01" n'a pas encore de statut<br>Et que le panneau de création est ouvert avec la nature "Renouvellement"<br>Quand il sélectionne l'entité "ENT-TEST-01"<br>Et qu'il laisse le champ "N° Requête BSC" vide<br>Et qu'il clique sur "Valider la création"<br>Alors la création est refusée<br>Et un message d'erreur s'affiche<br>Et aucune demande n'est créée pour l'entité "ENT-TEST-01" | Fonctionnel |
| TC-013 | Une entité sans statut ou au statut validé permet de créer la demande | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que l'entité "@entite" @etat<br>Et que le panneau de création est ouvert avec la nature "@nature"<br>Quand il renseigne tous les champs obligatoires avec l'entité "@entite"<br>Et qu'il clique sur "Valider la création"<br>Alors une demande est créée pour l'entité "@entite"<br>Et un message de confirmation s'affiche<br>Et il est redirigé vers la page du formulaire | Fonctionnel |
| TC-014 | Une entité avec une demande en cours, en retard ou en révision bloque la création | Étant donné que l'utilisateur "ADM-TEST-01" est connecté avec le rôle "Admin"<br>Et qu'il est sur la page "Liste des demandes"<br>Étant donné que l'entité "@entite" a une demande au statut "@statut"<br>Et que le panneau de création est ouvert avec la nature "@nature"<br>Quand il renseigne tous les champs obligatoires avec l'entité "@entite"<br>Et qu'il clique sur "Valider la création"<br>Alors la création est refusée<br>Et un message d'erreur s'affiche<br>Et aucune nouvelle demande n'est créée pour l'entité "@entite"<br>Et la demande existante de l'entité "@entite" est toujours au statut "@statut" | Fonctionnel |

TC-001 : paramètres

| cas | @compte | @role | @affichage |
|---|---|---|---|
| rôle autorisé | ADM-TEST-01 | Admin | est affiché |
| rôle autorisé | SAD-TEST-01 | SuperAdmin | est affiché |
| rôle non autorisé | USR-TEST-01 | User | n'est pas affiché |

TC-008 : paramètres

| cas | @nature |
|---|---|
| parcours Renouvellement | Renouvellement |
| parcours Nouveau | Nouveau |

TC-010 : paramètres

| cas | @nature |
|---|---|
| parcours Renouvellement | Renouvellement |
| parcours Nouveau | Nouveau |

TC-011 : paramètres

| cas | @millesime |
|---|---|
| borne basse | année fiscale en cours moins 20 ans |
| borne haute | année fiscale en cours plus 10 ans |

TC-013 : paramètres

| cas | @nature | @entite | @etat |
|---|---|---|---|
| Renouvellement, entité sans statut | Renouvellement | ENT-TEST-01 | n'a pas encore de statut |
| Renouvellement, statut validé | Renouvellement | ENT-TEST-02 | a une demande au statut "validé" |
| Nouveau, entité sans statut | Nouveau | ENT-TEST-06 | n'a pas encore de statut |
| Nouveau, statut validé | Nouveau | ENT-TEST-08 | a une demande au statut "validé" |

TC-014 : paramètres

| cas | @nature | @entite | @statut |
|---|---|---|---|
| Renouvellement, en cours | Renouvellement | ENT-TEST-03 | en cours |
| Renouvellement, en retard | Renouvellement | ENT-TEST-04 | retard |
| Renouvellement, en révision | Renouvellement | ENT-TEST-05 | révision |
| Nouveau, en cours | Nouveau | ENT-TEST-07 | en cours |
