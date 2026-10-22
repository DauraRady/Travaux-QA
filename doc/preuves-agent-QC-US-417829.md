# Agent QC actuel : chaque affirmation et sa preuve

US 417829 « Créer une nouvelle demande ». Revérifié le 20/10/2026 sur trois sources :

1. La description de l'US, sections 1 à 5.
2. La sortie de l'agent : cas TC-001 à TC-014, début de TC-015, et sa liste de cas UI.
3. Son fichier de consignes `qc.agent.md`. « l. » renvoie au numéro de ligne.

## Ce qu'on n'a pas vu, donc ce qu'on ne dit pas

1. La sortie de l'agent continue après TC-015. Toutes les affirmations portent donc sur « TC-001 à TC-015 ».
2. Les parties 1 (analyse), 2 (risques) et 4 (cas limites) de sa sortie n'ont pas été relues. On ne dit pas qu'il n'a vu aucun risque. On dit seulement que son format ne prévoit aucune place pour une question au PO.
3. Aucune publication réelle n'a été observée. On dit que la publication est « bien outillée » dans ses consignes, pas qu'elle « fonctionne bien ».
4. Les 4 commentaires de l'US n'ont pas été lus.

## Les textes de référence

US §4 Validation, 4e point :
« une création de demande possible avec une entité ID qui n'a pas encore de statut ou bien un statut validé (erreur si une entité ID a déjà une demande en statut : en cours, retard ou révision) »

US §3 Parcours 2, Entité ID :
« pas de possibilité pour l'utilisateur de saisir librement un code » ; « si l'utilisateur valide la création avec une entité ID alors surlignage en rouge du champs, titre du champs en rouge et message d'erreur sous le champs disant "entité ID inconnue" »

## Affirmations vérifiées

| # | Affirmation | Preuve | Statut |
|---|---|---|---|
| 1 | Chaque cas tient en une ligne Given, When, Then, sans Et | TC-001 à TC-014 ; consignes l. 205 et 206 (tableau à 4 colonnes, Gherkin dans la cellule) | Vérifié |
| 2 | Le type est « Fonctionnel » partout | Colonne Type of test, TC-001 à TC-014 | Vérifié |
| 3 | Ni rôle, ni écran, ni données | TC-005 : « Given le formulaire de création ouvert » ; TC-003 : « un rôle autre qu'Admin ou SuperAdmin » | Vérifié |
| 4 | L'exemple à copier est vague | Consignes l. 232 : « Given un utilisateur actif » | Vérifié |
| 5 | Actions résumées en une clause | TC-008 : « saisit un nom ou prénom de collaborateur KPMG connu et le sélectionne » ; TC-012 : « tous les champs Renouvellement renseignés » | Vérifié |
| 6 | Résultat impossible à vérifier | TC-008 : « le collaborateur est affecté à la demande », alors que la demande n'est pas encore créée ; TC-013 : « la redirection vers le formulaire adapté a lieu » | Vérifié |
| 7 | Règle de validation : 1 situation sur 5 | US §4 (texte ci-dessus) ; dans TC-001 à TC-015, seul TC-012 la touche : « Given une entité sans demande existante » | Vérifié, dans TC-001 à TC-015 |
| 8 | Ajout absent de l'US | Liste UI de l'agent : « Désactivation du bouton pendant l'envoi (anti double clic) » ; l'US n'en parle nulle part | Vérifié |
| 9 | Le point ambigu de l'entité inconnue n'est pas relevé | Liste UI : « États d'erreur conformes aux maquettes : champ surligné en rouge, titre rouge, message sous le champ (« Entité ID inconnue ») » ; TC-011 : « seule une sélection parmi les entités InfoCAC/référentiel est possible » | Vérifié |
| 10 | Pas de place pour une question au PO | Consignes l. 177 à 198 (5 parties fixes) ; l. 207 : « Do not add any extra sections » | Vérifié |
| 11 | TC-013 et TC-014 : même résultat écrit | TC-013 : « la demande est créée et la redirection vers le formulaire adapté a lieu » ; TC-014 : « la demande est créée et redirigée vers le formulaire correspondant » ; l'US ne dit pas ce que change Reprise | Vérifié |
| 12 | Un plan de test créé pour chaque US | Consignes l. 51 (« you MUST automatically create a Test Plan ») ; l. 68 à 76 (nom « QC - [titre de l'US] ») | Vérifié |
| 13 | Publication obligatoire | Consignes l. 173 : « This auto-creation is mandatory whenever the user provides a work item ID » | Vérifié |
| 14 | Seuls les cas « Fonctionnel » sont publiés | Consignes l. 90 et 91, l. 170 | Vérifié |
| 15 | L'adresse des commentaires est donnée, rien ne demande de les lire | Consignes l. 32 | Vérifié |
| 16 | Publication bien outillée | Consignes l. 30, l. 41 à 46 (codes HTTP), l. 136 à 140 (vérification des liens) | Vérifié |
| 17 | Bon sur l'écran | TC-001 à TC-006 (§1 à §3), TC-004 (§2), TC-005 (Reprise absente en Renouvellement), TC-007 (« Jean Dupont »), TC-010 (-20 à +10 ans, §3) | Vérifié |

## Affirmations corrigées ou retirées

| Ancienne affirmation | Pourquoi elle était fausse ou trop forte | Nouvelle formulation |
|---|---|---|
| « Bornes du millésime : 1 cas, sans les bornes » | TC-010 vérifie justement la plage de -20 à +10 ans | Retirée : pas de différence sur le millésime |
| « Contradiction de l'US sur l'entité inconnue » | La phrase de l'US est incomplète (« avec une entité ID ») ; une entité du référentiel peut être inconnue d'InfoCAC | « Point ambigu », à poser au PO |
| « Entité inconnue : ni cas, ni question » | L'agent prévoit bien de tester ce message, dans sa liste UI | « Prévue en test UI sans relever que la saisie libre est impossible » |
| « Une seule clause When imposée » | Rien de tel dans les consignes | « Une seule ligne par cas, imposée par le tableau » |
| « Doublon Reprise Oui et Non » | Reprise peut changer le formulaire ; l'US ne le dit pas | « Même résultat écrit ; l'US ne dit pas ce que change Reprise » |
| « La publication fonctionne bien » | Aucune publication observée | « Publication bien outillée dans ses consignes » |
| « Non testé » pour 4 situations | La sortie continue après TC-015 | « Non trouvé dans TC-001 à TC-015 » |
| « Entité sans demande » | L'US dit « entité qui n'a pas encore de statut » | Texte de l'US repris tel quel ; notre lecture « aucune demande » est à confirmer |

## Résultat du nouvel agent (lancé dans Claude Code, modèle Claude Sonnet 5.5)

| Chiffre | Où le vérifier |
|---|---|
| 22 cas exécutables, 14 scénarios, 0 erreur au contrôle | `resultat-agent-US-417829.md`, contrôlé par `build_tc.py check` puis `csv` |
| 5 situations de la règle de validation couvertes | Même rapport, fonctionnalité « Valider la création d'une demande » |
| 12 questions au PO, dont 6 bloquantes | Même rapport, section 4 |
| Premier passage trop prudent (2 situations sur 5), consigne corrigée puis agent relancé | Skill `us-analysis`, règle sur les détails manquants |
