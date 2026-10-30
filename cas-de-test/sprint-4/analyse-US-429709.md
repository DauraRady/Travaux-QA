# US 429709 : Description du mandat, ajouter les numéros d'engagement

Projet : InfoCAC. Analyse du 30/10/2026. Sprint 4.

## 1. Sources

| Source | État |
|---|---|
| US 429709 | Lue dans l'export `docs/projets/infocac/sources/US-429709.md` (Azure DevOps non joignable). Révision (System.Rev) et date de modification : non fournies par l'export. 0 commentaire. |
| Passages non lus | Fin de la phrase « En tant que… » (« empêchan[t … »). Maquette Figma non exportée. Ils ne sont pas complétés : ils deviennent des questions. |
| Critères d'acceptation | L'US n'en a pas. Le Flow utilisateur (étapes 1 à 6) et les Messages d'erreur en tiennent lieu. Citations : « Flow é.N » et « Messages ». |
| Contexte projet | `CONTEXTE.md` version 0.2, mis à jour le 30/10/2026, lu en entier. |
| Autres sources | `qc-reports/sprint-4-coherence.md` (30/10/2026). Cas `cas-de-test/sprint-3/US-424890-numero-engagement.md` lus directement : l'US 424890 elle-même n'est pas lue. |

Aucune donnée client ou personnelle réelle dans l'US.

## 2. Règles

| ID | Règle (reformulation fidèle) | Source | Statut | Question si À arbitrer |
|---|---|---|---|---|
| R1 | Le champ « N° engagement » est disponible dans la section « Description du mandat » et il est facultatif. | US « Je veux », Flow é.2 ; RT-03 | Rédigeable | |
| R2 | L'utilisateur peut ne renseigner aucun engagement. | Flow é.3 | Rédigeable | |
| R3 | Si aucun conflit n'est détecté sur le numéro renseigné, l'utilisateur peut poursuivre le parcours. | Flow é.5 | Rédigeable | |
| R4 | Pour le numéro renseigné, le système contrôle s'il est déjà associé à un engagement validé. S'il l'est, le système bloque son utilisation. | Flow é.4 et é.6 | Rédigeable | |
| R5 | En cas de blocage, un message s'affiche dans le toaster : « Un engagement avec ce numéro existe déjà ». | Messages | Rédigeable | |
| R6 | En cas de blocage, le message « Engagement erroné » s'affiche sous le champ. | Messages | Rédigeable | |
| R7 | En cas de blocage, le champ est surligné en rouge. | Messages | Rédigeable | |
| R8 | Le champ est destiné à l'utilisateur « habilité à créer ou modifier un mandat ». Le User ne peut pas écrire dans une demande. | US « En tant que » ; contexte §3 (rang 3) | Rédigeable | |
| R9 | Numéro déjà associé à une demande non validée : l'US ne dit pas si c'est un « conflit ». | Flow é.4, é.5 | À arbitrer | Q1 |
| R10 | Association de « plusieurs engagements » à un mandat. | Flow, introduction (contre « un numéro », « le champ ») | À arbitrer | Q2 |
| R11 | Contrôles autres que l'unicité : existence dans le Référentiel Finance, rattachement à l'entité, format, suggestions. L'US ne cite que l'unicité. | Flow é.4 ; contexte FLX-02, CONF-S4-04 | À arbitrer | Q3 |
| R12 | Moment du contrôle et sort d'un numéro refusé (enregistré par la sauvegarde automatique, restitué à la réouverture, ou non). | Flow é.4 à é.6 ; RT-06, RT-07 (US 426409) | À arbitrer | Q4 |
| R13 | Numéro déjà porté par la demande en cours de modification : l'US ne dit pas s'il est contrôlé contre lui-même. | Flow é.4 ; RT-08 (US 429428) | À arbitrer | Q5 |
| R14 | « Modifier un mandat » : le champ est-il modifiable après validation, et par quel rôle ? | US « En tant que » ; contexte §3, CONF-02 | À arbitrer | Q6 |
| R15 | Sens de « validé » et finalité de la US (« tout en empêchan[t … »). | US « Je veux » ; Flow, introduction contre é.4 et é.6 | À arbitrer | Q7 |

Détails non bloquants des règles Rédigeables : voir section 4 (Q8 à Q10).

## 3. Préconditions et combinaisons

Préconditions :

| Précondition | Valeur | Source |
|---|---|---|
| Rôle et compte connectés | Admin `AD-TEST-01` ou SuperAdmin `SA-TEST-01`. Pour R8, User `US-TEST-01`. | US « En tant que » lue comme Admin et SuperAdmin (contexte §3, S3) ; contexte §4 |
| Écran de départ | Formulaire de la demande, section « Description du mandat » | Flow é.1 ; contexte §7 |
| État de la demande | Demande au statut « En cours » (statut à la création). Cas validé : voir R14. | Contexte §5. L'US ne dit pas le statut de la demande ouverte. |
| Données existantes | Un engagement déjà validé : `DEM-TEST-01`, `ENT-ENG-12`, engagement 1021002 | Contexte §8 |
| Données existantes | Un engagement libre : aucun n'est donné pour la section Description du mandat | Voir testabilité |

Combinaisons :

| Conditions | Résultat attendu | Source | Statut |
|---|---|---|---|
| Admin ou SuperAdmin + champ vide | Aucun engagement associé, pas de blocage | Flow é.2, é.3 | Rédigeable |
| Admin ou SuperAdmin + numéro sans conflit | L'utilisateur peut poursuivre | Flow é.5 | Rédigeable |
| Admin ou SuperAdmin + numéro déjà validé | Utilisation bloquée ; toaster, message sous le champ, champ en rouge | Flow é.6 ; Messages | Rédigeable |
| User + champ N° engagement | Écriture non possible. Manière de refuser inconnue (Q10). | Contexte §3 (rang 3) | Rédigeable |
| Numéro associé à une demande non validée | Non écrit | Flow é.5 | À arbitrer (R9) |
| Plusieurs numéros | Non écrit | Flow, introduction | À arbitrer (R10) |
| Numéro absent du Référentiel Finance, ou d'une autre entité | Non écrit | Flow é.4 | À arbitrer (R11) |
| Numéro refusé, puis sortie du champ ou réouverture | Non écrit | Flow é.4 à é.6 | À arbitrer (R12) |
| Numéro de la demande courante ressaisi | Non écrit | Flow é.4 | À arbitrer (R13) |
| Demande Validée ou en Révision, Admin ou SuperAdmin | Non écrit | US « modifier » | À arbitrer (R14) |

Variations du contexte : VAR-06 (rôle) est retenue. VAR-01 (pays), VAR-02 (type) et VAR-07 n'ont aucun effet écrit sur ce champ. La recette couvre France et Certification des comptes (CONF-S4-10). Flux : FLX-02 (Référentiel Finance) n'est cité par l'US qu'à travers R11.

Filtrage mixte : l'US n'emploie ni « uniquement », ni « seulement », ni « exclut ». Aucune combinaison à ajouter.

Limites : aucun nombre, date, durée ou plafond Rédigeable. Le nombre maximal d'engagements est inconnu (R10).

Testabilité :

| Règle | Ce qu'il faut | Pourquoi ce n'est pas immédiat | À demander à |
|---|---|---|---|
| R4, R5, R6, R7 | Un engagement associé à une demande Validée (`DEM-TEST-01`, `ENT-ENG-12`, 1021002) | À injecter. Il faut que cette donnée corresponde bien à « engagement validé » (Q7). | Développeur, PO |
| R3 | Un engagement libre, accepté pour la demande testée | Le contexte §8 ne donne que 1021002 (validé) et 9999999 (absent). Un numéro libre est consommé à chaque usage dans les cas du sprint 3. | Développeur, Test Manager |
| R1 à R7 | Une demande « En cours » par exécution | Chaque création réussie consomme une entité `ENT-ENG-xx` (contexte §8) | QA |
| R5, R6, R7 | Emplacement et aspect du toaster, du message et du rouge | Maquette Figma non exportée | PO |

Écarts avec les autres US :

| ID | Type | Cette US | Autre source | Question | Point ouvert |
|---|---|---|---|---|---|
| E1 | Contradiction | « déjà associé à un engagement validé » ; toaster « Un engagement avec ce numéro existe déjà » ; sous le champ « Engagement erroné » | 424890 : « déjà associé à une demande » ; champ « Numéro déjà existant. » ; toaster « Cet engagement est déjà associé à une demande. Il n'est pas possible de créer une nouvelle demande avec ce numéro. Vous pouvez laisser le champ vide pour poursuivre la création. » (cas ENG-11, lus dans `cas-de-test/sprint-3/`) | Q1 | CONF-S4-01 |
| E2 | Contradiction interne | Flow, introduction : « contrôle d'unicité avant validation » | Flow é.4, é.6 : « engagement validé » ; US coupée à « empêchan[t » | Q7 | Nouveau |
| E3 | Contradiction interne | Introduction : « plusieurs engagements » | « un numéro », « le champ » ; 429428 RG-PERSIST-DM-03 : un seul N° engagement | Q2 | CONF-S4-02 |
| E4 | Interaction | Unicité seule | 424890 : « Numéro inconnu. », « Numéro incompatible. » ; ici un seul message sous le champ, « Engagement erroné » | Q3 | CONF-S4-04 |
| E5 | Interaction | Contrôle puis blocage, sans moment | 426409 RG-AS-01 : sauvegarde à la sortie du champ ; RG-AS-10 : donnée enregistrable même invalide | Q4 | CONF-S4-14 |
| E6 | Interaction | Contrôle « déjà associé » | 429428 RG-PERSIST-DM-03 : le N° engagement saisi à la création est déjà dans le champ à l'ouverture | Q5 | Nouveau |
| E7 | Interaction | Champ de Description du mandat | 426409 : liste d'exemples sans N° engagement | Q9 | CONF-S4-13 |
| E8 | Interaction | « créer ou modifier un mandat » | 429428 : exclut la modification après validation ; CONF-02 | Q6 | Nouveau, lié à CONF-02 |

Cas de test existants à revoir (fichier `cas-de-test/sprint-3/US-424890-numero-engagement.md`) :

| Cas | Pourquoi |
|---|---|
| ENG-11 et ENG-12 | Condition « associé à une demande » et messages « Numéro déjà existant. » : à relire après la réponse à Q1. Ils valent pour la création, pas pour Description du mandat. |
| ENG-13 | Message « Numéro déjà existant. » pour une double soumission : même point. |
| ENG-01 à ENG-16 | Le champ est décrit dans le panneau Nouvelle demande. À relire si le champ n'y est plus (CONF-S4-05). |

## 4. Questions au PO

Règles À arbitrer :

| # | Règle | Ce qui manque | Question | Bloquante |
|---|---|---|---|---|
| Q1 | R9 | L'US bloque un numéro « déjà validé » et laisse poursuivre « si aucun conflit ». Elle ne dit rien d'un numéro associé à une demande En cours. | Un numéro associé à une demande non validée est-il un conflit (refusé) ou accepté ? Quel message dans ce cas ? | Oui |
| Q2 | R10 | L'introduction parle de « plusieurs engagements », le reste d'un champ et d'« un numéro ». | Combien d'engagements un mandat peut-il porter ? Comment en ajouter un deuxième ? | Oui |
| Q3 | R11 | L'US ne cite que l'unicité. | Dans Description du mandat, le numéro doit-il aussi exister dans le Référentiel Finance et appartenir à l'entité ? Le champ garde-t-il les suggestions et la saisie numérique de 424890 ? Quels messages ? | Oui |
| Q4 | R12 | Le moment du contrôle n'est pas dit. 426409 sauvegarde à la sortie du champ. | Le contrôle se déclenche-t-il à la sortie du champ ou à une autre action ? Un numéro refusé est-il enregistré, et affiché à la réouverture ? | Oui |
| Q5 | R13 | Le N° engagement saisi à la création est déjà présent dans le champ (429428). | Le contrôle exclut-il la demande en cours ? Sinon, une demande qui porte déjà son numéro est-elle refusée dès qu'on le ressaisit ? | Oui |
| Q6 | R14 | « Modifier un mandat » n'est pas défini. | Le N° engagement est-il modifiable après validation ? Par quel rôle (Admin : CONF-02 ; SuperAdmin) ? | Non |
| Q7 | R15 | La fin de la phrase « tout en empêchan[t … » est illisible. « Validé » désigne peut-être l'engagement dans le Référentiel Finance ou le statut Validé de la demande rattachée. | Que doit empêcher la US ? « Validé » désigne-t-il l'engagement ou la demande ? Avant la validation de quoi le contrôle a-t-il lieu ? | Oui |

Détails non bloquants des règles Rédigeables :

| # | Règle | Question |
|---|---|---|
| Q8 | R5, R6 | Le numéro figure-t-il dans le message, comme le dit « permettant d'identifier le numéro concerné » (CONF-S4-03) ? Les deux messages sont-ils ceux de la maquette ? |
| Q9 | R3 | Le numéro valide est-il enregistré à la sortie du champ (CONF-S4-13) ? |
| Q10 | R8 | Comment le User est-il empêché d'écrire : champ non modifiable, masqué, ou refus au serveur ? |

Écarts avec le contexte projet : l'US n'en contredit aucune règle confirmée. RT-04 (création) et CONF-S4-01 restent ouverts, Description du mandat n'est pas tranché par cette US.

Idées exploratoires (hors de ce que l'US promet) :

1. Corriger un numéro refusé : le vider ou en saisir un autre, et vérifier que toaster, message et rouge disparaissent (comparer ENG-02 et ENG-08 à la création).
2. Saisie d'un numéro avec lettres, espace ou zéros en tête dans Description du mandat (comparer ENG-05 et ENG-07).
3. Deux demandes qui reçoivent le même numéro en même temps (comparer ENG-13).

## 5. Verdict

Partiellement prête : le champ facultatif, le numéro sans conflit et le blocage d'un numéro déjà validé avec ses trois signaux (R1 à R8) sont écrits, mais le sens de « validé », le nombre d'engagements, les contrôles complémentaires et le sort d'un numéro refusé (R9 à R15) attendent des réponses.

Scénarios à rédiger pour R1 à R8 seulement. Pour R4 à R7, la donnée « engagement validé » est à confirmer avec Q7.

## 6. Propositions pour le contexte

| # | Proposition (une ligne) | Section du contexte | Type | Source |
|---|---|---|---|---|
| 1 | Confirmer RT-03 : le N° engagement est facultatif dans Description du mandat | 6 (RT-03) | confirmation | US 429709 Flow é.2 |
| 2 | Ajouter la règle : un numéro déjà associé à un engagement validé est bloqué dans Description du mandat, avec toaster « Un engagement avec ce numéro existe déjà », message « Engagement erroné » sous le champ, champ en rouge (condition et messages de création différents : voir CONF-S4-01) | 6 | ajout | US 429709 Flow é.4, é.6 ; Messages |
| 3 | Point à confirmer : sens de « validé » et fin de la User Story | 9 | point à confirmer | US 429709 Flow, introduction, é.4, é.6 |
| 4 | Point à confirmer : le contrôle d'unicité exclut-il la demande en cours | 9 | point à confirmer | US 429709 Flow é.4 ; US 429428 RG-PERSIST-DM-03 |
| 5 | Point à confirmer : le N° engagement est-il modifiable après validation, par quel rôle (lien CONF-02) | 9 | point à confirmer | US 429709 « En tant que » ; contexte §3 |
| 6 | Compléter CONF-S4-04 : format numérique et suggestions de 424890 dans Description du mandat | 9 (CONF-S4-04) | point à confirmer | US 429709 Flow é.4 ; cas ENG-03, ENG-05 |
| 7 | Les points CONF-S4-01, -02, -03, -04, -13 et -14 restent ouverts : cette US ne les tranche pas | 9 | confirmation | US 429709 |

Rien n'est écrit dans le contexte.

Pour enrichir le contexte : /maj-contexte 429709
Étape suivante : /gherkin-test-generation 429709 (scénarios pour R1 à R8 seulement)
