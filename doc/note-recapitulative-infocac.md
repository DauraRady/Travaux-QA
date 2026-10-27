# InfoCAC : note récapitulative pour la recette

Mise à jour le 27/10/2026, après l'ajout des cas d'erreur du sprint 3. Ce document explique le projet, la façon d'exécuter les tests et les pièges à surveiller. Il s'appuie sur le PRD consolidé du 23/09/2026 (lu en captures), le PRD reconstitué, les US des sprints 1 à 3 et les cas déjà rédigés dans ce dépôt. Ce qui vient d'une interprétation est signalé comme tel.

## 1. Le projet en une page

InfoCAC tient la liste officielle des mandats de commissariat aux comptes (CAC) de KPMG pour la France, le Maghreb et l'Afrique francophone, et la transmet aux autres applications. Il remplace la partie mandats d'IBS, un CRM arrêté en avril 2027.

Périmètre testé aujourd'hui : France uniquement, et mandats de Certification des comptes uniquement. La Durabilité, le type mixte et les autres pays décrits dans le PRD et dans certaines US sont hors périmètre ; aucun cas ne les teste. La mise en production est prévue en mars 2027, en une seule version, sans évolution prévue après le go-live (information orale du PM).

Un mandat CAC, c'est KPMG nommé commissaire aux comptes d'une entreprise cliente (l'entité) pour plusieurs exercices (mandat de 3 ou 6 ans). Dans InfoCAC, tout mandat commence par une demande, que le back-office (BSC) remplit, contrôle et fait valider. Seule une donnée validée est envoyée aux autres applications : c'est le principe de « source unique de vérité ».

Pourquoi la qualité compte ici : les données de mandats alimentent des déclarations réglementaires (CNCC, Déclaration d'Activités) et le suivi des rotations des associés. Une erreur saisie dans InfoCAC se propage et ressort plus tard, dans un autre outil, où elle est difficile à rattacher à sa cause.

## 2. Le vocabulaire métier

| Terme | Sens | D'où vient l'info |
|---|---|---|
| Entité, Entité ID | L'entreprise cliente et son identifiant dans le référentiel | PRD, US |
| Demande | Le dossier qui deviendra un mandat une fois validé | PRD |
| Nature du mandat | Nouveau ou Renouvellement, choisi à la création ; « Reprise » est alors un champ Oui ou Non | Cas de création de ce dépôt |
| Catégorie du mandat | Nouveau, Reprise ou Renouvellement, dans la section Description du mandat | US 426402 |
| Type de mandat | Certification des comptes (audit légal) dans le périmètre testé ; l'US décrit aussi Durabilité et un type mixte, hors périmètre | US 426402 |
| Millésime | L'exercice fiscal concerné ; l'année fiscale va d'octobre à septembre | US, PRD |
| Numéro d'engagement | Le code de la mission dans le Référentiel Finance (engagementCode) | US 424890 |
| Requête BSC | Le numéro de ticket du back-office ; plusieurs PV peuvent partager le même | US Contrôles |
| Indicateurs DA | Deux Oui/Non pour la Déclaration d'Activités ; pour un mandat de Certification des comptes : Certification à Oui, Durabilité à Non | US 426235 |
| Taxonomie | Code de classement du mandat, par exemple AA11 CAC Nouveau, AA12 CAC Maintien | US 426973 |
| EIP | Entité d'intérêt public (sociétés cotées, banques, assureurs, mutuelles), soumise à des règles plus strictes | US 426406 |
| OPC | Organisme de placement collectif (un fonds) | US 426406 |
| AGP | Sigle non expliqué dans les US : à demander (Q-29) | US 426406 |
| Marché de cotation | Bourse où les titres de l'entité sont cotés ; « Non coté » sinon | US 426407 |
| PV d'AG | Procès-verbal d'assemblée générale qui nomme le CAC ; lu par OCR pour préremplir le formulaire | PRD |

Le mot « Reprise » a deux sens dans le projet : la reprise des données d'IBS (migration de 15 000 mandats environ) et une catégorie de mandat. Dans la taxonomie, une Reprise donne AA11 comme un Nouveau. L'idée que « Reprise veut dire renouvellement » est donc à revérifier avec le PO (Q-22).

## 3. Les acteurs et les droits

| Rôle | Qui | Ce qu'il fait |
|---|---|---|
| SuperAdmin | Risk Management et certains BSC | Tout, y compris modifier après validation, annuler, importer en masse, voir le journal |
| Admin | BSC | Crée et complète les demandes de son périmètre ; ne modifie pas une fiche validée selon le PRD |
| User | Collaborateurs KPMG | Consulte les données validées, sans écriture |

L'authentification passe par le SSO, les droits sont donnés par SailPoint. Deux contradictions de droits restent ouvertes et touchent le sprint 3. L'US S1-03 laisse l'Admin modifier une demande validée, le PRD l'interdit (Q6). Les US de liste et de recherche ouvrent les demandes non validées au User, le PRD le limite aux données validées (Q5).

Règle de test : un droit se vérifie côté serveur, pas seulement par un bouton masqué. Un bouton absent ne prouve rien si l'appel à l'API passe quand même.

## 4. Le parcours d'une demande

1. L'équipe Audit demande un mandat (aujourd'hui par ServiceNow, ressaisi à la main dans InfoCAC en V1).
2. Le BSC clique sur « Nouvelle demande » dans la Liste des demandes : un panneau s'ouvre à droite. Il choisit la Nature, saisit l'Entité ID, la Reprise, la requête BSC, la personne affectée, le millésime et, depuis le sprint 3, le numéro d'engagement. Il clique sur « Valider la création ».
3. La demande est créée au statut « En cours ». Le BSC remplit le formulaire, section par section ; certains champs se calculent à partir d'autres.
4. Le PV d'AG est attaché, l'OCR propose des valeurs, le BSC les confirme (sprints à venir).
5. La demande passe la porte de validation : refusée s'il manque un champ obligatoire, un document, ou une confirmation d'une valeur OCR.
6. Validée, elle part vers Référentiel France (quotidien), Déclaration d'Activités et MyRotations (toutes les 15 minutes en heures ouvrées).
7. Une correction après validation (SuperAdmin) la fait passer en Révision, puis revalidation et nouvel envoi.

Statuts cités dans les sources : En cours, Analyse OCR, Retard (plus de 60 jours sans validation), Validé, Révision, Annulé. Le référentiel exact des statuts reste à trancher entre le PRD et les US.

## 5. L'architecture en bref

| Élément | Choix |
|---|---|
| Front | Vue 3 sur Azure WebApp |
| Back | .NET sur Azure WebApp, API documentée en OpenAPI |
| Données | SQL Azure ; documents dans Azure Storage |
| Entrées | Référentiel des entités (Engage vers Référentiel France), Annuaire CNCC, Référentiel Finance pour les engagements (sprint 3) |
| Sorties | Référentiel France, Déclaration d'Activités, MyRotations |
| Environnements | Dev, préprod, prod. Pas d'ITG. La QA teste en préprod, puis le métier y fait sa recette |

Au 27/10/2026, la préprod est accessible. Restent à confirmer : un compte par rôle, les données de test et les demandes validées à injecter. L'ordre d'exécution est dans `doc/ordre-execution-sprints-1-a-3.md`.

## 6. Ce que construisent les sprints 1 à 3

| Sprint | Contenu | Cas dans ce dépôt |
|---|---|---|
| 1 et 2 | Side panel Discovery, groupes de sécurité, création d'une demande, liste, filtres | `cas-de-test/*.md` (38 cas dans ce dépôt pour 43 annoncés ; Discovery et groupes de sécurité sans fichier ici) |
| 3 | Numéro d'engagement et contrôles à la création, recherche par Entité ID, en-tête du formulaire, section Description du mandat (pays, type, catégorie, indicateurs DA, taxonomie, qualification EIP, marchés de cotation) | `cas-de-test/sprint-3/` (65 scénarios, 139 exécutions, dont 27 scénarios d'erreur, de refus ou de contournement par l'API) |

Ce qui n'a pas encore de sprint et porte pourtant le plus de risque : la reprise des 15 000 mandats IBS, le cycle de vie des statuts, la porte de validation, le journal d'activité, les flux sortants, le multi-millésime.

## 7. Le cœur du sprint 3 : un formulaire en cascade

Le sprint 3 livre surtout des champs qui en commandent d'autres. Les anomalies se cachent rarement dans la première saisie ; elles se cachent quand on revient en arrière.

| Champ saisi | Ce qu'il commande | Règle |
|---|---|---|
| Type de mandat | Indicateurs DA | Certification des comptes : Certification à Oui, Durabilité à Non ; non modifiables |
| Catégorie du mandat | Taxonomie | Nouveau ou Reprise donne AA11, Renouvellement donne AA12 ; recalcul à chaque changement ; non modifiable |
| Catégorie d'entité | AGP et Type d'EIP | EIP : AGP forcé à Non, Type d'EIP obligatoire et multiple ; Non-EIP ou OPC : Type d'EIP à N/A |
| Marché de cotation 1 | Marchés 2 et 3 | Non coté : les deux autres à Non coté et verrouillés ; sinon un marché réel une seule fois |
| Entité ID | Numéro d'engagement | L'engagement doit être rattaché à l'entité |

Chaque flèche se teste dans les deux sens : poser la valeur, puis la changer et vérifier que l'aval suit.

## 8. Avant d'exécuter

1. Obtiens les comptes Admin et SuperAdmin (et User pour plus tard), et vérifie leur rôle dans Paramètres avant la première campagne. Un compte avec deux rôles fausse tous les résultats de droits.
2. Demande aux développeurs ce qu'ils peuvent injecter : une demande au statut « Validé » (HEAD-04, ENG-11, ENG-12), un Référentiel Finance indisponible (ENG-15, ENG-16), des engagements de test rattachés à des entités connues.
3. Relève la liste réelle des engagements et des entités de préprod, et fais la correspondance avec les identifiants fictifs du README du sprint 3.
4. Crée dans Azure Test Plans les étapes partagées (Se connecter, Ouvrir la création, Ouvrir la liste) et le paramètre partagé « Profils habilités ».
5. Vérifie la version déployée en préprod (release note) : une US « To be tested » n'est pas forcément livrée sur l'environnement que tu testes.
6. Ouvre les outils de développement du navigateur (onglet Réseau et Console) pendant toute la campagne : c'est là que tu verras les codes d'erreur, les ProblemDetails, les appels en double et les erreurs JavaScript.

## 9. Pendant l'exécution : à quoi faire attention

1. Ordre de jeu : d'abord 427092 (déjà « To be tested »), puis les créations avec engagement (424890), puis le formulaire en cascade, puis la recherche et l'en-tête.
2. Une donnée par exécution : chaque création réussie consomme son entité et son engagement. Rejouer un cas avec les mêmes données donne un faux échec (« déjà associé », ou TC07 « l'entité a déjà une demande en cours »).
3. Un refus se vérifie deux fois : le message, puis l'absence de la donnée (la demande n'apparaît pas dans la liste après rechargement). Un message affiché alors que la demande a quand même été créée est l'anomalie la plus grave.
4. Recharge la page après chaque saisie qui doit être enregistrée : une valeur visible à l'écran n'est pas forcément enregistrée (cas réel de 426235, qui ne sauvegarde rien au sprint 3).
5. Compare chaque message au texte de l'US, au caractère près, y compris le point final. Si la maquette Figma et l'US diffèrent, c'est une question au PO, pas une anomalie.
6. Joue chaque scénario avec chaque profil de ses Exemples : un écart entre Admin et SuperAdmin est un résultat en soi.
7. Note la version, le compte, l'heure et les données de chaque échec, et capture l'onglet Réseau : sans ça, l'anomalie sera difficile à reproduire.
8. Un comportement sur une règle « Non rédigée » s'observe et se note, mais devient une question au PO, pas une anomalie.
9. Fais une session exploratoire de 60 minutes sur la cascade après la première vague (section 10, thème 3).

## 10. Pièges et cas limites, par thème

### Thème 1 : le numéro d'engagement

1. Les zéros en tête (0001234) : si le numéro est stocké en nombre, il devient 1234. Vérifie la valeur enregistrée, pas seulement l'affichage.
2. Copier-coller depuis Excel ou Outlook : espaces, tirets ou caractères invisibles autour du numéro.
3. Double clic sur « Valider la création », et deux onglets qui créent en même temps avec le même engagement : une seule demande doit exister (contrôle en base exigé par l'US).
4. Contournement de l'écran : la même création envoyée directement à l'API doit être refusée (contrôle front et back exigé par l'US).
5. Changer l'Entité ID après avoir choisi un engagement compatible : l'engagement reste-t-il accepté (Q-16) ?
6. Référentiel Finance lent ou indisponible : aucune suggestion ne doit pouvoir être validée, et la saisie ne doit pas être perdue.
7. Engagement d'une demande annulée ou supprimée : redevient-il disponible (Q-18) ?

### Thème 2 : l'entité et les doublons

1. Contradiction ouverte : l'US Contrôles accepte une Entité ID inconnue et plusieurs demandes par entité, alors que les cas de création (TC06, TC07) bloquent les deux (Q-19). Ne conclus à aucune anomalie avant la réponse du PO.
2. Nom de l'entité collé à la place de l'identifiant, ou identifiant avec des espaces.
3. Entité inconnue acceptée : que deviendra-t-elle dans le flux vers Référentiel France ?

### Thème 3 : la cascade du formulaire

1. Allers-retours : Nouveau vers Renouvellement puis retour ; EIP vers OPC puis EIP ; Non coté vers Euronext puis Non coté. Vérifie à chaque fois les champs dépendants.
2. Valeur imposée qui écrase une valeur saisie : AGP à Oui puis passage en EIP.
3. Valeur héritée qui doit disparaître : « Non coté » des marchés 2 et 3 quand le marché 1 devient réel ; types d'EIP quand on quitte EIP.
4. Rien ne doit revenir tout seul : en repassant à EIP, aucun ancien type n'est restauré (RG-EIP-08).
5. Rechargement entre deux changements : l'état affiché après rechargement doit être le dernier saisi.
6. Champ désactivé à l'écran mais modifiable par l'API : à vérifier quand la sauvegarde existera.
7. Incohérences métier que personne n'interdit encore : une EIP « titres admis sur un marché réglementé de l'UE » avec le marché 1 à « Non coté » (Q-31).

### Thème 4 : les droits

1. User face aux demandes non validées, à l'écran et par l'API (Q5).
2. Rôle retiré dans SailPoint pendant une session ouverte.
3. Session expirée au milieu d'une saisie : la saisie est-elle perdue, la demande créée en double au retour ?

### Thème 5 : la recherche et la liste

1. Recherche partielle, en minuscules, avec des espaces avant ou après (Q-32).
2. Recherche combinée à un filtre, puis filtre retiré : la recherche doit rester active.
3. Données partagées : une recherche sur une entité utilisée par d'autres tests affiche des demandes en plus. Utilise des entités réservées (ENT-RECH).

### Thème 6 : le temps et les millésimes

1. Le millésime courant change au 1er octobre (année fiscale d'octobre à septembre) : la valeur par défaut et les bornes de la liste (N-20 à N+10 selon S1-02, N-2 à N+2 selon le PRD) changent avec lui.
2. Le statut Retard apparaît après 60 jours : il faut des demandes datées artificiellement pour le tester.

### Thème 7 : l'environnement

1. Une seule préprod partagée avec la recette métier : tes données de test seront visibles par le métier, et les leurs peuvent fausser tes listes. Préfixe tout ce que tu crées.
2. Les champs évoluent à chaque sprint : un cas écrit au sprint 3 peut devenir faux au sprint 4 sans que la fonction ait régressé. Relis les cas touchés à chaque nouvelle US.

## 11. Les contradictions à faire trancher en premier

| # | Sujet | Sources en conflit | Impact |
|---|---|---|---|
| Q-19 | Entité ID inconnue et doublons de demandes | US Contrôles contre TC06 et TC07 | Création, flux vers Référentiel France |
| Q-13 | Message d'engagement déjà associé | US Contrôles contre 424890 | Texte des messages |
| Q-22 | Sens de Reprise ; Nature, Reprise et Catégorie | Création, 426402, 426973 | Taxonomie, déclarations |
| Q5 | Le User voit les demandes non validées | 425530, liste, contre PRD | Confidentialité |
| Q6 | L'Admin modifie une demande validée | S1-03 contre PRD | Intégrité des données envoyées |
| Q-26 | Indicateurs DA enregistrés ou non | 426235 contre lui-même | Flux vers DA |
| Q-40 | Que proposent les listes Pays et Type de mandat ? | 426402 (18 pays, 3 types) contre le périmètre France et Certification | Formulaire, filtres de la liste |

La liste complète des questions est dans `cas-de-test/sprint-3/README.md`.

## 12. L'automatisation, plus tard

Rien n'est automatisé au sprint 3 : le formulaire gagne des champs à chaque sprint, et les indicateurs DA et la taxonomie ne sont pas encore enregistrés. Le démarrage est envisagé vers le sprint 6 ou 7, avec Playwright (API et UI), un dépôt GitHub et une CI dans Azure Pipelines. Les meilleurs candidats du sprint 3 sont les contrôles serveur de l'engagement (ENG-10, ENG-12, ENG-13), les contournements par l'API de la cascade (EIP-10, EIP-11, MC-08, MC-09), le refus d'écriture du User (DM-05), les droits du User sur la liste (Q5) et la table de décision de la taxonomie, une fois enregistrée.

## 13. Où trouver quoi

| Besoin | Fichier |
|---|---|
| Cas de test des sprints 1 et 2 | `cas-de-test/*.md` |
| Cas de test du sprint 3, données, questions | `cas-de-test/sprint-3/` |
| Règles de rédaction et script de contrôle | `skills/gherkin-test-generation/` |
| Estimation de la recette | `doc/estimation-recette-sprints-1-a-5.md` |
| Ordre d'exécution des sprints 1 à 3 | `doc/ordre-execution-sprints-1-a-3.md` |
| Messages déjà envoyés (environnements, automatisation) | `doc/message-teams-*.md` |
