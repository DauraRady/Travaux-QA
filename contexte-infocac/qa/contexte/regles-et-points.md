# Contexte projet : InfoCAC : regles-et-points

Sources et US du projet, règles transverses, points à confirmer, variations, flux. Lu par la cohérence et l'analyse.

## 2. Sources

| ID | Document ou décision | Date ou version | État | Emplacement |
|---|---|---|---|---|
| SRC-01 | PRD consolidé | 23/09/2026 | Partiel : connu par la note récapitulative de la QA, non exporté ici | `doc/note-recapitulative-infocac.md` |
| SRC-02 | Cas de création des sprints 1 et 2 (TC05, TC06, TC07) | Sprints 1-2 | Cas de test, pas une source métier : à relier à leur US | `cas-de-test/creer-une-demande.md` |
| SRC-03 | Questions ouvertes des sprints 1 à 3 (Q5 à Q-41) | 27/10/2026 | À jour | `cas-de-test/sprint-3/README.md` |

US du projet connues de l'agent :

| US | Titre | Sprint | Source lue | Cas de test |
|---|---|---|---|---|
| 417829 | Créer une nouvelle demande | 1 | Texte exporté : `sources/US-417829.md` | `cas-de-test/creer-une-demande.md` |
| Contrôles création (identifiant non visible) | Contrôles à la création | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-controles-creation.md` |
| 424890 | Numéro d'engagement à la création | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-424890-numero-engagement.md` |
| 426402 | Pays, Type et Catégorie du mandat | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-426402-caracteristiques-mandat.md` |
| 426235 | Indicateurs DA | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-426235-indicateurs-DA.md` |
| 426973 | Taxonomie Certification France | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-426973-taxonomie-certification-france.md` |
| 426406 | AGP, catégorie d'entité, Type d'EIP | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-426406-AGP-categorie-entite-type-EIP.md` |
| 426407 | Marchés de cotation | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-426407-marches-cotation.md` |
| 425530 | Recherche par Entité ID | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-425530-recherche-entite-id.md` |
| 422727 | En-tête du formulaire et bouton Retour | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-422727-entete-formulaire.md` |
| 427092 | Titre, sous-titre, affectation | 3 | Par les cas (S3) | `cas-de-test/sprint-3/US-427092-titre-sous-titre-affectation.md` |
| 429709 | Numéros d'engagement dans Description du mandat | 4 | Texte exporté : `sources/US-429709.md` | Aucun |
| 426408 | Sections du formulaire selon Pays et Type de mandat | 4 | Texte exporté, règles RG-SEC-06 et suivantes non lues : `sources/US-426408.md` | Aucun |
| 426409 | Sauvegarde automatique de Description du mandat | 4 | Texte exporté : `sources/US-426409.md` | Aucun |
| 429428 | Persistance des données de création dans le formulaire | 4 | Texte exporté, étapes 4 à 6 en partie non lues : `sources/US-429428.md` | Aucun |

## 6. Règles transverses et décisions

| ID | Règle ou décision | Périmètre | Source et date | Statut | Remplacée par |
|---|---|---|---|---|---|
| RT-01 | Création possible si l'entité n'a pas de statut ou un statut Validé ; erreur si elle a une demande En cours, Retard ou Révision | Création d'une demande | US 417829 §4 | confirmée | |
| RT-02 | Tous les champs du panneau Nouvelle demande sont obligatoires | Création | US 417829 §3 | confirmée ; requête BSC facultative selon l'US Contrôles (CONF-04) | |
| RT-03 | Le numéro d'engagement est facultatif | Création et Description du mandat | 424890 (S3) ; US 429709 étape 2 | confirmée | |
| RT-04 | Un engagement déjà utilisé est refusé ; contrôle à l'écran et côté serveur | Création | 424890 (S3) | confirmée ; condition et message différents en sprint 4 (CONF-S4-01) | |
| RT-05 | Un champ d'une section masquée est conservé, mais ne compte plus dans la complétude ni dans la validation ; il réapparaît si la section redevient applicable | Formulaire | US 426408 RG-SEC-03 à 05 | confirmée | |
| RT-06 | Chaque valeur de Description du mandat est sauvegardée à la sortie du champ, même si la demande est incomplète ; un échec laisse la valeur affichée, informe et propose de relancer ; les valeurs sont restaurées à la réouverture | Description du mandat | US 426409 RG-AS-01 à 08 | confirmée | |
| RT-07 | Une donnée peut être sauvegardée sans être valide fonctionnellement ; une section n'est pas « Remplie » sur une donnée non enregistrée | Formulaire | US 426409 RG-AS-09, 10 | confirmée | |
| RT-08 | Type de mandat, N° engagement, Affectée à et Entité ID saisis à la création sont restitués dans le formulaire sans modification, et propres à chaque demande | Création vers formulaire | US 429428 RG-PERSIST-DM-01 à 08 | confirmée | |
| RT-09 | Les indicateurs DA sont déterminés par le Type de mandat ; Certification des comptes : Certification à Oui, Durabilité à Non, non modifiables | Description du mandat | 426235 (S3) | confirmée | |
| RT-10 | La taxonomie est calculée par la Catégorie (Nouveau ou Reprise : AA11 ; Renouvellement : AA12) et n'est pas modifiable | Description du mandat | 426973 (S3) | confirmée ; listée comme champ saisi dans 426409 (CONF-S4-13) | |
| RT-11 | EIP : AGP forcé à Non, Type d'EIP obligatoire et multiple ; Non-EIP ou OPC : Type d'EIP à N/A | Description du mandat | 426406 (S3) | confirmée | |
| RT-12 | Marché 1 « Non coté » : marchés 2 et 3 à Non coté et verrouillés ; sinon un marché réel une seule fois | Description du mandat | 426407 (S3) | confirmée | |
| RT-13 | Seule une donnée validée est envoyée aux autres applications | Flux sortants | SRC-01 | confirmée | |

## 9. Points à confirmer et écarts

Une ligne ouverte ne produit aucun résultat attendu.

Points des sprints 1 à 3 (détail dans SRC-03) :

| ID | Sujet | Ce qui est connu | Question | Impact si sans réponse | Bloquante ? | État |
|---|---|---|---|---|---|---|
| CONF-01 | Visibilité du User (Q5) | 425530 ouvre les demandes non validées au User, le PRD le limite aux validées | Le User voit-il les demandes non validées ? | Droits sur liste, recherche, en-tête | oui | ouvert |
| CONF-02 | Admin et demande validée (Q6) | Une US l'autorise, le PRD l'interdit | L'Admin modifie-t-il une demande validée ? | Droits après validation, statut Révision | oui | ouvert |
| CONF-03 | Entité inconnue et doublons (Q-19) | L'US Contrôles accepte une entité inconnue et plusieurs demandes ; 417829 §3-4 et TC06, TC07 les refusent | Laquelle fait foi ? | Création, flux vers Référentiel France | oui | ouvert |
| CONF-04 | Requête BSC (Q-19) | Obligatoire (417829 §3) contre facultative (US Contrôles) | Laquelle fait foi ? | Création | oui | ouvert |
| CONF-05 | Nature, Reprise, Catégorie (Q-22) | Nature (Nouveau, Renouvellement) et Reprise à la création ; Catégorie (Nouveau, Reprise, Renouvellement) dans le formulaire | Ces champs se recoupent-ils ? Que veut dire Reprise ? | Taxonomie, persistance (429428) | oui | ouvert |
| CONF-06 | Champs obligatoires du formulaire (Q-21) | « Obligatoire » sans moment ni message de contrôle | Quand et comment le contrôle se déclenche-t-il ? | Complétude, validation | oui | ouvert |
| CONF-07 | Listes Pays et Type de mandat (Q-40) | 426402 décrit 18 pays et 3 types ; le périmètre testé est France et Certification | Que proposent les listes ? | Formulaire, sections (426408) | oui | ouvert |

Points nouveaux du sprint 4 :

| ID | Sujet | Ce qui est connu | Question | Impact si sans réponse | Bloquante ? | État |
|---|---|---|---|---|---|---|
| CONF-S4-01 | Engagement déjà utilisé : condition et message | Création : « déjà associé à une demande », message « Cet engagement est déjà associé à une demande… » (424890) ; US Contrôles : « Un engagement étant déjà existant… » ; Description du mandat : « déjà associé à un engagement validé », toaster « Un engagement avec ce numéro existe déjà » et « Engagement erroné » sous le champ (429709) | Quelle condition (demande quelconque ou validée) et quel message, à la création et dans Description du mandat ? | Refus d'engagement (429709 étapes 4 et 6) | oui | ouvert |
| CONF-S4-02 | Un ou plusieurs engagements par mandat | 429709 : objectif « plusieurs engagements », mais un champ « N° engagement » et « un numéro » ; 429428 restitue un seul N° engagement | Combien d'engagements par mandat, et comment en ajouter un deuxième ? | 429709, 429428 | oui | ouvert |
| CONF-S4-03 | Message explicite sur le numéro | 429709 étape 6 : message « permettant d'identifier le numéro concerné » ; le texte du toaster ne contient pas le numéro | Le numéro apparaît-il dans le message ? | Texte du résultat attendu | non | ouvert |
| CONF-S4-04 | Contrôles de 424890 dans Description du mandat | 424890 contrôle aussi l'existence dans le Référentiel Finance et le rattachement à l'entité ; 429709 ne cite que l'unicité | Ces contrôles s'appliquent-ils aussi dans Description du mandat ? | Cas d'erreur de 429709 | oui | ouvert |
| CONF-S4-05 | Champs du panneau Nouvelle demande | 417829 (sprint 1) : Nature, Entité ID, Reprise, N° Requête BSC, Affectée à, Millésime ; 429428 (sprint 4, « CHANGEMENT ») : Type de mandat, N° engagement, Affecté à, Entité ID saisis à la création | Le panneau propose-t-il désormais le Type de mandat ? La Nature reste-t-elle ? 417829 sera-t-elle mise à jour ? | Cas de création des sprints 1 et 3, 429428 | oui | ouvert |
| CONF-S4-06 | Périmètre de 429428 | Le périmètre cite Type, Catégorie et N° engagement ; le flow et les règles citent Type, N° engagement, Affecté à et Entité ID ; la Catégorie n'a aucune règle | Quelles données sont persistées et restituées ? | Couverture de 429428 | oui | ouvert |
| CONF-S4-07 | Où s'affiche Affectée à | 429428 : dans Description du mandat ; 427092 : avec le titre et le sous-titre | Les deux affichages coexistent-ils ? | Cas TIT de 427092 | non | ouvert |
| CONF-S4-08 | Échec partiel de persistance | 429428 RG-PERSIST-DM-09 : « reste à arbitrer » entre refus complet et création avec anomalie | Quel comportement ? | Cas d'erreur de 429428 | oui pour ce cas | ouvert |
| CONF-S4-09 | Section Audit contractuel | Masquée dans tous les cas décrits par RG-SEC-01 ; RG-SEC-06 et suivantes non lues | Quand est-elle affichée ? | 426408 | non | ouvert |
| CONF-S4-10 | Périmètre de recette et 426408 | La recette teste France et Certification ; 426408 n'a d'effet visible qu'avec Durabilité, le type mixte ou un pays hors France | Le sprint 4 élargit-il le périmètre de recette ? | 426408 presque entièrement non testable sinon | oui | ouvert |
| CONF-S4-11 | Hors France et Type Durabilité | 426408 RG-SEC-02 masque Durabilité hors France ; 426402 impose Certification hors France (S3) | Durabilité peut-il être choisi hors France ? Que s'affiche-t-il alors ? | 426408 | non | ouvert |
| CONF-S4-12 | Sections toujours affichées | 426408 ne classe ni Description du mandat ni l'en-tête | Sont-ils toujours affichés ? | 426408 | non | ouvert |
| CONF-S4-13 | Champs sauvegardés automatiquement | 426409 donne une liste d'« exemples » qui inclut la taxonomie, calculée et non modifiable (426973), et n'inclut pas N° engagement ni Affectée à, présents dans la section au sprint 4 | La liste est-elle complète ? N° engagement et Affectée à sont-ils sauvegardés automatiquement ? | 426409, 429709 | non | ouvert |
| CONF-S4-14 | Valeur refusée et sauvegarde automatique | 426409 RG-AS-10 : une donnée peut être sauvegardée sans être valide ; 429709 bloque un engagement déjà validé ; 426409 exclut les contrôles métier bloquants | Un engagement refusé, ou une combinaison interdite de la cascade, est-il enregistré ? | Interaction 426409 et 429709, cascade du sprint 3 | oui | ouvert |
| CONF-S4-15 | Indicateurs de sauvegarde | 426409 décrit des indicateurs « en cours », « succès », « non sauvegardée » et une action de relance, sans texte ni emplacement | Textes et emplacements (maquette) ? | Texte des résultats attendus | non | ouvert |
| CONF-S4-16 | Simuler une erreur technique | 426409 RG-AS-06, 07 et 429428 RG-PERSIST-DM-09 décrivent des échecs techniques | Comment provoquer un échec de sauvegarde en préprod ? | Cas d'échec de 426409 et 429428 | oui pour ces cas | ouvert |
| CONF-S4-17 | Demande au statut Retard | Retard au bout de 60 jours sans validation (SRC-01) ; aucune donnée de ce type en préprod | Qui crée ou injecte une demande en Retard en préprod ? | Refus de création RT-01, cas Retard | oui pour ce cas | ouvert ; signalé oralement le 28/10 |
| CONF-S4-18 | Cas du sprint 3 touchés par la sauvegarde | Les cas du sprint 3 vérifient qu'une valeur affichée n'est pas forcément enregistrée (426235) ; 426409 enregistre désormais | Quels cas du sprint 3 faut-il réécrire ? | Régression des cas existants | non | ouvert |

## 10. Variations

| ID | Varie selon | Valeurs | Ce qui change | Source | Statut |
|---|---|---|---|---|---|
| VAR-01 | Pays | France, hors France | Sections affichées (hors France : Certification et entité seulement) ; type imposé hors France | US 426408 RG-SEC-01, 02 ; 426402 (S3) | confirmée |
| VAR-02 | Type de mandat | Certification, Durabilité, Certification & Durabilité | Sections affichées ; indicateurs DA | US 426408 RG-SEC-01 ; 426235 (S3) | confirmée |
| VAR-03 | Nature du mandat | Renouvellement, Nouveau | Champ Reprise (Nouveau) ; origine de l'entité ; plage du millésime | US 417829 §3 | confirmée |
| VAR-04 | Catégorie du mandat | Nouveau, Reprise, Renouvellement | Taxonomie AA11 ou AA12 | 426973 (S3) | confirmée |
| VAR-05 | Catégorie d'entité | EIP, Non-EIP, OPC | AGP, Type d'EIP | 426406 (S3) | confirmée |
| VAR-06 | Rôle | SuperAdmin, Admin, User | Bouton de création, écriture | US 417829 §1 ; SRC-01 | confirmée |
| VAR-07 | Statut de la demande existante sur l'entité | Aucune, Validé, En cours, Retard, Révision | Création acceptée ou refusée | US 417829 §4 | confirmée |

## 11. Flux entrants et sortants

| ID | Sens | Système | Déclencheur | Données échangées | Ce qu'on peut vérifier en test | Source | Statut |
|---|---|---|---|---|---|---|---|
| FLX-01 | entrant | Référentiel des entités (Engage, Référentiel France) | Choix de l'Entité ID | Entité ID, nom de l'entité | Entité proposée à la création, nom dans l'en-tête | US 417829 §3 ; SRC-01 | confirmé ; lien InfoCAC et référentiel à préciser |
| FLX-02 | entrant | Référentiel Finance | Saisie du N° engagement | Numéro, description, entité de rattachement | Suggestions, refus d'un numéro absent ou d'une autre entité | 424890 (S3) | confirmé ; propriété de rattachement inconnue (Q-14) |
| FLX-03 | entrant | Annuaire des collaborateurs KPMG | Saisie dans Affectée à | Nom, prénom | Collaborateur proposé | US 417829 §3 | confirmé ; système exact à préciser |
| FLX-04 | entrant | Annuaire CNCC | | | | SRC-01 | à confirmer |
| FLX-05 | sortant | Référentiel France | Quotidien | Données validées | Donnée validée présente côté Référentiel France | SRC-01 | confirmé |
| FLX-06 | sortant | Déclaration d'Activités, MyRotations | Toutes les 15 minutes en heures ouvrées | Données validées | Donnée validée transmise | SRC-01 | confirmé |
| FLX-07 | entrant | SSO, SailPoint | Connexion | Rôle | Rôle effectif dans l'application | SRC-01 | confirmé |
