# Cohérence du sprint 4 : US 429709, 426408, 426409, 429428

Projet : InfoCAC. Rapport du 30/10/2026. Aucun écart n'est tranché : chaque ligne est une question au PO ou à la Test Manager.

## 1. Sources

Azure DevOps n'est pas joignable dans cet environnement. Les US sont lues dans les exports de `docs/projets/infocac/sources/`.

| US | Titre | Source lue | Révision (System.Rev) | Date de lecture | Passages non lus |
|---|---|---|---|---|---|
| 429709 | Description du mandat : ajouter les numéros d'engagement | `sources/US-429709.md` | Non fournie par l'export | Transcrit le 30/10/2026 | Fin de la phrase « En tant que… » (« empêchan[t … ») ; maquette Figma |
| 426408 | Adapter les sections du formulaire au Type de mandat | `sources/US-426408.md` | Non fournie par l'export | Transcrit le 30/10/2026 | RG-SEC-06 et suivantes ; 1 commentaire non exporté ; maquette Figma |
| 426409 | Sauvegarder automatiquement la Description du mandat | `sources/US-426409.md` | Non fournie par l'export | Transcrit le 30/10/2026 | Aucun passage signalé ; maquette non citée |
| 429428 | Persister les données de la création d'une demande | `sources/US-429428.md` | Non fournie par l'export | Transcrit le 30/10/2026 | Suite de l'étape 4, étape 5, début de l'étape 6 (RG-PERSIST-DM-05 et 06) ; deux maquettes Figma |

US plus anciennes consultées :

| US | Passages lus | Comment |
|---|---|---|
| 417829 (sprint 1) | §1 à §5, en entier | `sources/US-417829.md` ; 4 commentaires non exportés |
| 424890, 426402, 426235, 426973, 426406, 426407, 427092, 422727, US Contrôles (sprint 3) | Aucun | Connues seulement par le CONTEXTE (S3). Les cas de test (`cas-de-test/`) ne sont pas dans ce dépôt. Les citations de ces US sont celles du CONTEXTE, pas une lecture directe. À vérifier avant de poser les questions au PO. |

Contexte : `docs/projets/infocac/CONTEXTE.md`, version 0.2 du 30/10/2026. Les références CONF-S4-xx renvoient à sa section 9. Les écarts marqués « Nouveau » n'y figurent pas encore.

## 2. Carte du sprint

Objets cités par au moins deux sources. Synonymes rapprochés selon la section 5 du contexte (N° engagement = Numéro d'engagement ; Affectée à = Affecté à ; Panneau Nouvelle demande = fenêtre Nouvelle demande).

N° engagement : condition d'unicité

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| N° engagement : unicité | 424890 (S3) | « déjà associé à une demande » | CONTEXTE RT-04 et CONF-S4-01, non relu dans l'US |
| N° engagement : unicité | 429709 | « déjà associé à un engagement validé » | Flow, étape 4 |
| N° engagement : unicité | 429709 | « Si un numéro est déjà validé, le système bloque son utilisation » | Flow, étape 6 |
| N° engagement : unicité | 429709 | « contrôle d'unicité avant validation » | Flow, paragraphe d'introduction |

N° engagement : nombre

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| N° engagement : nombre | 429709 | « l'association facultative de plusieurs engagements à un mandat » | Flow, paragraphe d'introduction |
| N° engagement : nombre | 429709 | « renseigner un numéro d'engagement » ; « Le champ « N° engagement » » | User Story ; Flow, étapes 2 et 3 |
| N° engagement : nombre | 429428 | « le champ N° engagement de Description du mandat contient la valeur enregistrée » | RG-PERSIST-DM-03 |

N° engagement : où il est saisi, enregistré et restitué

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| N° engagement : emplacement | 424890 (S3) | Champ du panneau Nouvelle demande | CONTEXTE §7 |
| N° engagement : emplacement | 429709 | Champ de la section « Description du mandat » | User Story ; Flow, étape 2 |
| N° engagement : emplacement | 429428 | Saisi à la création, restitué dans Description du mandat | Périmètre ; Flow ; RG-PERSIST-DM-03 |
| N° engagement : sauvegarde automatique | 426409 | Liste d'exemples de champs sans N° engagement | Flow, étape 1 |
| N° engagement : sauvegarde automatique | 429709 | Champ de Description du mandat, avec contrôle avant de poursuivre | Flow, étapes 2 à 6 |

Panneau Nouvelle demande : champs

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| Panneau Nouvelle demande | 417829 | « Entité ID, Reprise, N° Requête BSC, Affectée à, Millésime » ; Nature du mandat | §3, parcours 1 et 2 |
| Panneau Nouvelle demande | 429428 | « CHANGEMENT … Type de mandat, Catégorie du mandat, N° engagement » ; « Type de mandat ; N° engagement ; Affecté à ; Entité ID » renseignés à la création | Périmètre ; Flow, paragraphe sous « L'utilisateur crée une Nouvelle demande » ; RG-PERSIST-DM-01 |

Type de mandat : origine, valeur restituée, valeur sauvegardée

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| Type de mandat | 429428 | « La valeur … enregistrée lors de la création est automatiquement restituée » ; « conserve sa valeur » à la réouverture | RG-PERSIST-DM-02 ; RG-PERSIST-DM-07 |
| Type de mandat | 426409 | Sauvegarde à la sortie du champ ; « les dernières valeurs sauvegardées sont restaurées » | Flow, étapes 1 à 3 et 8 ; RG-AS-01 et RG-AS-08 |
| Type de mandat | 426408 | « L'utilisateur a renseigné : 1. Pays ; 2. Type de mandat » ; modification possible | Étapes 0 et 1 |
| Type de mandat hors France | 426402 (S3) | Certification des comptes imposée hors France | CONTEXTE VAR-01 et CONF-S4-11 |

Pays

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| Pays : origine | 417829 | Aucun champ Pays dans le panneau | §3, parcours 1 et 2 |
| Pays : origine | 429428 | Pays absent des quatre données persistées ; « autres champs de la section Description du mandat » exclus | Flow ; Périmètre, liste des exclusions |
| Pays : origine | 426408 | Pays renseigné avant le calcul des sections | Étape 0 ; RG-SEC-01 et 02 |
| Pays : origine | 426402 (S3) | Pays est un champ de Description du mandat | CONTEXTE §7 |

Sections masquées et sauvegarde

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| Données des sections | 426408 | « les données précédemment sauvegardées sont restaurées » (sections Certification, Durabilité, Entité, Référentiel et Normes) | Étape 6 ; RG-SEC-05 |
| Données des sections | 426409 | « Cette US couvre la sauvegarde automatique des champs de la section : Description du mandat » | Périmètre |
| Complétude et « Remplie » | 426408 | Les données d'une section masquée ne comptent plus dans la complétude | Étape 5 ; RG-SEC-03 |
| Complétude et « Remplie » | 426409 | « Une section ne peut être considérée comme Remplie sur la base d'une donnée qui n'a pas été correctement enregistrée » | RG-AS-09 |

Valeur invalide et sauvegarde

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| Valeur refusée | 426409 | « Une erreur de complétude métier ne bloque pas la sauvegarde d'une valeur valide » | RG-AS-04 |
| Valeur refusée | 426409 | « Une donnée peut être : sauvegardée ; mais non valide fonctionnellement » | RG-AS-10 |
| Valeur refusée | 426409 | « ne couvre pas … les contrôles métier bloquants » | Périmètre |
| Valeur refusée | 429709 | « le système bloque son utilisation » | Flow, étape 6 |

Affectée à

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| Affectée à : affichage | 429428 | « l'Affecté à est affiché dans la section Description du mandat » | Flow ; RG-PERSIST-DM-04 |
| Affectée à : affichage | 427092 (S3) | Affiché avec le titre et le sous-titre | CONTEXTE CONF-S4-07 |
| Affectée à : valeur | 417829 | Nom du compte connecté par défaut, modifiable | §3 |

Entité ID dans l'en-tête

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| Entité ID : en-tête | 429428 | « l'Entité ID est affiché dans l'en-tête du formulaire » | Flow ; RG-PERSIST-DM-07 |
| Entité ID : en-tête | 422727, 427092 (S3) | L'en-tête affiche déjà le nom de l'entité et l'Entité ID | CONTEXTE §7 |

Taxonomie et champs calculés

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| Taxonomie | 426409 | Citée parmi les champs saisis ou modifiés | Flow, étape 1 |
| Taxonomie | 426973 (S3) | Calculée par la Catégorie, non modifiable | CONTEXTE RT-10 |

Périmètre pays et types

| Objet | US | Ce que dit l'US | Source précise |
|---|---|---|---|
| Valeurs du Type de mandat | 426408 | Trois valeurs, avec effet sur les sections | Étape 1 ; RG-SEC-01 |
| Valeurs du Type de mandat | 429428 | Trois valeurs « pour la France » | RG-PERSIST-DM-02 |
| Périmètre de recette | CONTEXTE | France et Certification des comptes uniquement | CONTEXTE §1 ; CONF-S4-10 |

## 3. Écarts

« = CONF-S4-xx » : l'écart est déjà au contexte (section 9), précisé ici avec les citations. « Nouveau » : absent du contexte, voir section 7.

| # | Type | Objet | Source A | Source B | Question | Bloquante pour |
|---|---|---|---|---|---|---|
| E1 | Contradiction | N° engagement : condition et message de refus | 424890 (S3) : « déjà associé à une demande » ; message « Cet engagement est déjà associé à une demande… » (via CONTEXTE RT-04) | 429709 Flow étape 4 : « déjà associé à un engagement validé » ; Messages d'erreur : toaster « Un engagement avec ce numéro existe déjà », sous le champ « Engagement erroné » | Le refus vaut-il pour une demande quelconque ou seulement validée ? Quel message à la création et dans Description du mandat ? = CONF-S4-01 | 429709 étapes 4 et 6 ; RT-04 |
| E2 | Incohérence interne | 429709 : sens de « validé » | 429709 Flow, paragraphe d'introduction : « contrôle d'unicité avant validation » | 429709 Flow étapes 4 et 6 : « engagement validé », « un numéro est déjà validé » ; User Story : phrase coupée à « empêchan[t … » | « Validé » désigne-t-il l'engagement dans le Référentiel Finance ou le statut Validé de la demande rattachée ? Avant la validation de quoi ? Que doit empêcher la fin de la User Story ? Nouveau | 429709 étape 4 |
| E3 | Incohérence interne | N° engagement : un ou plusieurs | 429709 Flow, introduction : « association facultative de plusieurs engagements à un mandat » | 429709 User Story : « un numéro d'engagement » ; Flow étapes 2 et 3 : « Le champ », « un numéro » ; 429428 RG-PERSIST-DM-03 : « le champ N° engagement » | Combien d'engagements par mandat ? Comment en ajouter un deuxième ? = CONF-S4-02 | 429709 ; 429428 |
| E4 | Incohérence interne | Message qui identifie le numéro | 429709 Flow étape 6 : « message explicite permettant d'identifier le numéro concerné » | 429709 Messages d'erreur : « Un engagement avec ce numéro existe déjà » (sans le numéro) | Le numéro figure-t-il dans le message ? = CONF-S4-03 | Texte du résultat attendu (non bloquant) |
| E5 | Interaction | Contrôles de N° engagement dans Description du mandat | 424890 (S3) : existence dans le Référentiel Finance et rattachement à l'entité (via CONTEXTE FLX-02, CONF-S4-04) | 429709 Flow étape 4 : unicité seule | Existence et rattachement à l'entité sont-ils aussi contrôlés ? = CONF-S4-04 | Cas d'erreur de 429709 |
| E6 | Interaction | Contrôle d'unicité et valeur de la demande elle-même | 429428 RG-PERSIST-DM-03 : le N° engagement saisi à la création est déjà dans Description du mandat à l'ouverture | 429709 Flow étape 4 : le système contrôle si le numéro est déjà associé ; 424890 (S3) : « déjà associé à une demande » | Le contrôle exclut-il la demande courante ? Sinon, la valeur créée par l'utilisateur est refusée dès qu'il la modifie puis la remet. Nouveau | 429709 cas nominal |
| E7 | Interaction | Moment du contrôle et valeur refusée enregistrée ou non | 429709 Flow étapes 4 à 6 : contrôle puis blocage, sans dire quand | 426409 RG-AS-01 : sauvegarde à la sortie du champ ; RG-AS-10 : donnée sauvegardable mais non valide ; Périmètre : exclut les contrôles métier bloquants | Le contrôle se déclenche-t-il à la sortie du champ ? Un engagement refusé est-il enregistré ? Idem pour une combinaison interdite de la cascade du sprint 3. = CONF-S4-14 | 429709 ; 426409 ; cascade 426402 à 426407 |
| E8 | Incohérence interne | 426409 : sauvegarde d'une valeur invalide | 426409 RG-AS-04 : « ne bloque pas la sauvegarde d'une valeur valide » | 426409 RG-AS-10 : « Une donnée peut être : sauvegardée ; mais non valide fonctionnellement » | Une valeur invalide est-elle sauvegardée ? RG-AS-04 ne parle que de la valeur valide. Nouveau | 426409 cas de valeur invalide |
| E9 | Évolution | Champs du panneau Nouvelle demande | 417829 §3 : Nature du mandat, Entité ID, Reprise, N° Requête BSC, Affectée à, Millésime | 429428 Périmètre : « CHANGEMENT » ; Flow : Type de mandat, N° engagement, Affecté à, Entité ID renseignés à la création | Le panneau propose-t-il désormais le Type de mandat ? La Nature reste-t-elle ? 417829 sera-t-elle mise à jour ? = CONF-S4-05 | Cas de création des sprints 1 et 3 ; 429428 |
| E10 | Incohérence interne | 429428 : périmètre contre règles | 429428 Périmètre : Type de mandat, Catégorie du mandat, N° engagement | 429428 Flow et RG-PERSIST-DM-01, 04, 07, 08 : Type, N° engagement, Affecté à, Entité ID ; aucune règle sur la Catégorie | Quelles données sont persistées et restituées ? La Catégorie est-elle concernée (lien avec CONF-05) ? = CONF-S4-06 | Couverture de 429428 |
| E11 | Interaction | Pays : où et quand il est renseigné | 426408 Étape 0 : « L'utilisateur a renseigné : 1. Pays ; 2. Type de mandat » ; RG-SEC-01 et 02 | 417829 §3 : pas de champ Pays dans le panneau ; 429428 Flow et Périmètre : Pays non persisté, « autres champs de la section Description du mandat » exclus | Où le Pays est-il choisi ? Quelles sections s'affichent à la première ouverture, avant le Pays ? Nouveau | 426408 premier affichage ; 429428 |
| E12 | Interaction | Type de mandat : valeur de création ou dernière valeur enregistrée | 429428 RG-PERSIST-DM-02 et 07 : valeur de la création restituée, « conserve sa valeur » | 426409 Étapes 1 à 3 et 8, RG-AS-08 : Type sauvegardé à la sortie du champ, dernières valeurs sauvegardées restaurées | Si l'utilisateur change le Type après la création, laquelle des deux valeurs revient à la réouverture ? Nouveau | 429428 DM-07 ; 426409 RG-AS-08 |
| E13 | Interaction | Changement de Type et échec de sauvegarde | 426408 Étapes 1, 2 et 7 : le système détermine les sections et recalcule complétude et état global | 426409 Étape 6 et RG-AS-06 : en cas d'échec, la valeur reste affichée mais n'est pas sauvegardée ; RG-AS-09 : « Remplie » seulement sur donnée enregistrée | Les sections et la complétude suivent-elles la valeur affichée ou la valeur enregistrée ? À quel moment, avant ou après la sauvegarde ? Nouveau | 426408 et 426409, cas d'échec |
| E14 | Interaction | Sauvegarde des champs des autres sections | 426408 Étape 6 et RG-SEC-05 : « données précédemment sauvegardées » restaurées dans les sections Certification, Durabilité, Entité, Référentiel et Normes | 426409 Périmètre : seule la section Description du mandat est couverte | Quelle US sauvegarde les champs des autres sections ? Sans elle, que restaure-t-on ? Nouveau | 426408 étapes 5 et 6 |
| E15 | Hors périmètre de recette | Valeurs hors périmètre | 426408 Étape 1 et RG-SEC-01 : effets visibles avec Durabilité, le type mixte ou un pays hors France ; 429428 RG-PERSIST-DM-02 : trois valeurs de Type | CONTEXTE §1 : recette limitée à France et Certification des comptes | Le sprint 4 élargit-il le périmètre de recette ? = CONF-S4-10 | 426408 presque entier ; 429428 RG-PERSIST-DM-02 |
| E16 | Contradiction | Durabilité hors France | 426408 RG-SEC-02 : hors France, Durabilité jamais affichée, « quel que soit le Type de mandat sélectionné » ; « Les seules sections pouvant être affichées » : Certification et Entité | 426402 (S3, via CONTEXTE VAR-01) : Certification imposée hors France | Le Type Durabilité est-il choisissable hors France ? Quelles sections s'affichent alors, la section Certification en fait-elle partie ? = CONF-S4-11 | 426408 RG-SEC-02 |
| E17 | Incohérence interne | Section Audit contractuel | 426408 RG-SEC-01 : masquée dans les trois cas France | 426408 RG-SEC-02 : absente des sections affichables hors France ; RG-SEC-06 et suivantes non lues | Quand est-elle affichée ? = CONF-S4-09 | Non bloquant |
| E18 | Incohérence interne | Sections toujours affichées | 426408 RG-SEC-01 : ne classe ni Description du mandat ni l'en-tête | 426409 Périmètre et 429428 Flow : les deux supposent Description du mandat et en-tête affichés | Sont-ils toujours affichés ? = CONF-S4-12 | Non bloquant |
| E19 | Interaction | Affectée à : où il s'affiche | 429428 Flow, RG-PERSIST-DM-04 : dans Description du mandat | 427092 (S3, via CONTEXTE CONF-S4-07) : avec le titre et le sous-titre | Les deux affichages coexistent-ils ? = CONF-S4-07 | Cas TIT de 427092 (non bloquant) |
| E20 | Évolution | Entité ID dans l'en-tête | 429428 Flow, RG-PERSIST-DM-07 : « l'Entité ID est affiché dans l'en-tête du formulaire » | 422727 et 427092 (S3, via CONTEXTE §7) : l'en-tête affiche déjà l'Entité ID | 429428 ajoute-t-elle un comportement ou répète-t-elle 422727 ? Nouveau | Doublon de cas (non bloquant) |
| E21 | Interaction | Liste des champs sauvegardés automatiquement | 426409 Étape 1 : « Exemples » dont la Taxonomie ; sans N° engagement ni Affectée à | 426973 (S3) : taxonomie calculée, non modifiable ; 429709 et 429428 : N° engagement et Affectée à dans la section | La liste est-elle complète ? N° engagement et Affectée à sont-ils sauvegardés automatiquement ? = CONF-S4-13 | Non bloquant |
| E22 | Évolution | Cas du sprint 3 sur « affiché mais pas enregistré » | 426235 (S3, via CONTEXTE CONF-S4-18) : une valeur affichée n'est pas forcément enregistrée | 426409 RG-AS-01 : enregistrement à la sortie du champ | Quels cas du sprint 3 faut-il réécrire ? = CONF-S4-18 | Non bloquant |
| E23 | Incohérence interne | Échec partiel de persistance à la création | 429428 RG-PERSIST-DM-09 : l'erreur ne doit pas être silencieuse | 429428 RG-PERSIST-DM-09, dernier paragraphe : « refus complet de création » ou « création … avec signalement d'une anomalie », à arbitrer | Quel comportement ? = CONF-S4-08 | Cas d'erreur de 429428 |
| E24 | Interaction | Profil habilité et modification | 429709 User Story : « habilité à créer ou modifier un mandat » ; 426408 et 426409 : « collaborateur habilité à compléter une demande » | 429428 User Story : « Admin ou SuperAdmin » ; Périmètre : exclut « la modification des données après validation » (CONTEXTE CONF-02) | Le champ N° engagement est-il modifiable après validation ? Par quel rôle ? Nouveau | Cas de rôle de 429709 (non bloquant) |
| E25 | Testabilité | Indicateurs de sauvegarde | 426409 Étapes 4 à 6, RG-AS-02, 03, 06 : indicateurs « en cours », « succès », « non sauvegardée », relance | Aucun texte ni emplacement dans l'export ; maquette non citée | Textes et emplacements ? = CONF-S4-15 | Texte des résultats attendus |
| E26 | Testabilité | Erreur technique à provoquer | 426409 RG-AS-06 et 07 | 429428 RG-PERSIST-DM-09 | Comment provoquer un échec de sauvegarde ou de persistance en préprod ? = CONF-S4-16 | Cas d'échec de 426409 et 429428 |
| E27 | Testabilité | Demande au statut Retard | 417829 §4 : erreur si l'entité a une demande « en cours, retard ou révision » | CONTEXTE CONF-S4-17 : aucune demande Retard en préprod | Qui crée ou injecte une demande Retard ? = CONF-S4-17 | Cas Retard de la création (RT-01) |

## 4. Cas de test existants à revoir

Les cas ne sont pas dans ce dépôt : les noms viennent du CONTEXTE (section 2). À ouvrir et vérifier avant toute réécriture.

| Fichier ou cas | Pourquoi | US qui le change |
|---|---|---|
| `cas-de-test/creer-une-demande.md` (TC05, TC06, TC07) | Champs du panneau de création : Type de mandat et N° engagement à la création (E9) | 429428 |
| `cas-de-test/sprint-3/US-controles-creation.md` | Message « Un engagement étant déjà existant… » et champs du panneau (E1, E9) | 429709, 429428 |
| `cas-de-test/sprint-3/US-424890-numero-engagement.md` | Condition et message d'unicité, contrôles d'existence et de rattachement, emplacement du champ (E1, E5, E6) | 429709, 429428 |
| `cas-de-test/sprint-3/US-426235-indicateurs-DA.md` | Cas « valeur affichée non enregistrée » devenu faux avec la sauvegarde automatique (E22) | 426409 |
| `cas-de-test/sprint-3/US-426402-caracteristiques-mandat.md` | Pays, Type, Certification imposée hors France ; interaction avec les sections et avec les valeurs de Type (E11, E16) | 426408, 429428 |
| `cas-de-test/sprint-3/US-426973-taxonomie-certification-france.md` | Taxonomie calculée, citée parmi les champs sauvegardés (E21) | 426409 |
| `cas-de-test/sprint-3/US-426406-AGP-categorie-entite-type-EIP.md` et `US-426407-marches-cotation.md` | Cascade : une combinaison interdite est-elle enregistrée ? (E7) | 426409 |
| `cas-de-test/sprint-3/US-427092-titre-sous-titre-affectation.md` (cas TIT) | Affichage de Affectée à (E19) | 429428 |
| `cas-de-test/sprint-3/US-422727-entete-formulaire.md` | Entité ID dans l'en-tête, doublon possible (E20) | 429428 |

## 5. Données et moyens de test à demander

| Besoin | Pour quelle règle | À qui |
|---|---|---|
| Engagement associé à une demande au statut Validé (DEM-TEST-01, ENT-ENG-12, engagement 1021002, déjà prévu : à injecter) | 429709 étape 4 : refus d'un engagement validé | Développeur |
| Engagement associé à une demande En cours, non validée | 429709 : distinguer « demande quelconque » de « demande validée » (E1, E2) | Développeur, après réponse du PO |
| Engagement du Référentiel Finance rattaché à une autre entité ; numéro absent (9999999 existe) | 429709 : contrôles hérités de 424890 (E5) | Développeur |
| Moyen de provoquer un échec de sauvegarde et un échec de persistance en préprod | 426409 RG-AS-06 et 07 ; 429428 RG-PERSIST-DM-09 (E26) | Développeur ou Test Manager |
| Demande au statut Retard (signalé oralement le 28/10) | RT-01, création refusée | Développeur |
| Demande France avec des données dans Durabilité et Référentiel et Normes, Type Durabilité accessible | 426408 RG-SEC-03 à 05 (E15) | Développeur, Test Manager |
| Pays hors France et listes complètes de Pays et de Type en préprod | 426408 RG-SEC-02 ; CONF-07 (E16) | PO, Test Manager |
| Au moins un champ saisissable dans chaque section (Certification, Durabilité, Entité, Référentiel et Normes) | 426408 : vérifier la conservation et la restauration des données ; le contenu des sections n'est pas décrit | PO |
| Au moins deux entités sans demande par exécution pour comparer deux demandes | 429428 RG-PERSIST-DM-08 (isolation) ; ENT-ENG-01 à 08 sont consommées à chaque création | QA, Développeur |
| Textes et emplacements des indicateurs de sauvegarde ; maquettes Figma des quatre US (429709 : 1 lien, 426408 : 1 lien, 429428 : 2 liens) | 426409 RG-AS-02, 03, 06 ; E25 | PO |
| Export complet : fin de la User Story 429709, RG-SEC-06 et suivantes et commentaire de 426408, étapes 4 à 6 de 429428, révision (System.Rev) des quatre US | Toutes les règles concernées | PO, ou relecture directe dans Azure DevOps |

## 6. Ordre conseillé pour /us-analysis

| Rang | US | Raison |
|---|---|---|
| 1 | 429428 | Elle fixe d'où viennent Type, N° engagement, Affectée à, Entité ID au moment de la création. Elle modifie le panneau décrit par 417829 (E9) et alimente les trois autres. Ses points ouverts (E9, E10, E23) conditionnent les cas de création. |
| 2 | 429709 | Elle partage le N° engagement avec 429428 et dépend de la condition d'unicité (E1, E2, E3). Plus tôt elle est cadrée, plus tôt la question au PO peut partir. |
| 3 | 426409 | Elle s'applique aux champs des deux US précédentes et à la cascade du sprint 3. Son analyse a besoin des réponses sur E7, E8 et E12. |
| 4 | 426408 | Elle dépend du Pays et du Type (E11, E12, E13) et d'une décision de périmètre de recette (E15). Elle est presque entièrement non testable dans le périmètre actuel, donc la plus sensible à CONF-S4-10. |

## 7. Propositions pour le contexte

À ajouter dans la section 9 du contexte, après « oui » et `/maj-contexte sprint-4`. Numérotation à partir de CONF-S4-19.

| # | Proposition (une ligne) | Section du contexte | Type | Source |
|---|---|---|---|---|
| P1 | CONF-S4-19 : « validé » dans 429709 désigne-t-il l'engagement ou la demande ? Fin de la User Story tronquée (E2) | 9 | Point à confirmer, bloquant | 429709 Flow introduction et étapes 4 et 6 ; User Story |
| P2 | CONF-S4-20 : le contrôle d'unicité exclut-il la demande courante ? (E6) | 9 | Point à confirmer, bloquant | 429709 Flow étape 4 ; 429428 RG-PERSIST-DM-03 |
| P3 | CONF-S4-21 : où est choisi le Pays, et que s'affiche-t-il avant son choix ? (E11) | 9 | Point à confirmer, bloquant | 426408 étape 0 ; 417829 §3 ; 429428 Périmètre |
| P4 | CONF-S4-22 : à la réouverture, valeur du Type de la création ou dernière valeur sauvegardée ? (E12) | 9 | Point à confirmer, bloquant | 429428 RG-PERSIST-DM-07 ; 426409 RG-AS-08 |
| P5 | CONF-S4-23 : sections et complétude selon la valeur affichée ou enregistrée en cas d'échec de sauvegarde (E13) | 9 | Point à confirmer, bloquant pour ce cas | 426408 étapes 1, 2, 7 ; 426409 étape 6 et RG-AS-09 |
| P6 | CONF-S4-24 : quelle US sauvegarde les champs des autres sections que Description du mandat ? (E14) | 9 | Point à confirmer, bloquant | 426408 RG-SEC-05 ; 426409 Périmètre |
| P7 | CONF-S4-25 : 426409 RG-AS-04 (« valeur valide ») contre RG-AS-10 : une valeur invalide est-elle enregistrée ? (E8) | 9 | Point à confirmer, bloquant pour ce cas | 426409 RG-AS-04 et RG-AS-10 |
| P8 | CONF-S4-26 : 429428 répète-t-elle 422727 pour l'Entité ID de l'en-tête ? (E20) | 9 | Point à confirmer, non bloquant | 429428 Flow ; CONTEXTE §7 |
| P9 | CONF-S4-27 : N° engagement modifiable après validation, par quel rôle ? (E24) | 9 | Point à confirmer, non bloquant | 429709 User Story ; 429428 Périmètre |
| P10 | Enrichir CONF-S4-14 : préciser le moment du contrôle d'unicité (sortie de champ ou validation) (E7) | 9 | Complément | 429709 étapes 4 à 6 ; 426409 RG-AS-01 |
| P11 | Enrichir CONF-S4-10 : 429428 RG-PERSIST-DM-02 cite trois valeurs de Type, dont deux hors du périmètre de recette (E15) | 9 | Complément | 429428 RG-PERSIST-DM-02 |
| P12 | Ligne de données : engagement associé à une demande En cours, non validée (à injecter) | 8 | Donnée de test | 429709 ; E1, E2 |
| P13 | Ligne de données : au moins deux entités sans demande par exécution pour l'isolation | 8 | Donnée de test | 429428 RG-PERSIST-DM-08 |
| P14 | Sources : noter 426408 « 1 commentaire non exporté » et la fin de User Story de 429709 non lue | 2 | Source à compléter | Exports du 30/10/2026 |

Pour analyser la première US : /us-analysis 429428. Pour enrichir le contexte : /maj-contexte sprint-4.
