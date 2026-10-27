Objet : Agent QC : proposition d'évolution et décisions à prendre

Bonjour Meriem,

Je te propose une évolution de l'agent QC. Les deux présentations jointes servent de support si tu veux qu'on en parle en atelier.

Ce que j'ai constaté sur l'agent actuel, à partir de sa sortie sur l'US 417829 « Créer une nouvelle demande » :

1. Les cas décrivent fidèlement l'écran (TC-001 à TC-011, sections 1 à 3 de l'US) et la publication est bien outillée dans ses consignes (codes HTTP contrôlés, liens vérifiés). Je garde les deux.
2. Chaque cas tient sur une ligne Given, When, Then, sans rôle, sans écran de départ ni données : par exemple TC-005, « Given le formulaire de création ouvert ». Il faut tout reconstituer avant d'exécuter.
3. La règle de validation de la section 4 de l'US décrit 5 situations selon le statut de l'entité (sans statut, validé, en cours, retard, révision). Dans les cas TC-001 à TC-015, une seule est couverte (TC-012).
4. Son format n'a pas de place pour une question au PO. Par exemple, il prévoit de tester le message « entité ID inconnue » (section 3) sans relever que l'entité ne peut pas être saisie librement. Il ajoute aussi un cas que l'US ne décrit pas (désactivation du bouton, anti double clic).

Ce que je propose :

1. Un contexte projet dans le dépôt, créé à partir du PRD et du DAG, puis enrichi après chaque US, uniquement avec ce que l'équipe a validé.
2. Une étape par commande (analyse de l'US, rédaction des scénarios, publication) : l'agent s'arrête après chaque étape pour relecture.
3. Rien d'inventé : une règle floue devient une question au PO, pas un cas de test.
4. Des scénarios en Gherkin français, avec le rôle connecté, l'écran, les données, une action et un résultat exact par ligne.
5. Aucune écriture dans Azure DevOps sans aperçu et accord explicite, contrôlé aussi par un script. Il est aussi possible de produire un CSV à importer dans Test Plans.

Où on en est : j'ai lancé le nouvel agent dans Claude Code sur l'US 417829, avec le même modèle que l'agent actuel (Claude Sonnet 5.5). Au dernier lancement (27/10) : 25 cas exécutables, aucune erreur au contrôle automatique, les 5 situations de la règle de validation couvertes dans les deux natures de mandat, et 14 questions au PO, dont 4 bloquantes (notamment entité ID inconnue, section 3, et documents obligatoires, section 4). L'agent produit aussi le tableau pour Azure DevOps et propose ce qu'il faut ajouter au contexte du projet, sans rien écrire sans accord. Limite : l'agent a lu l'US dans un fichier exporté, sans les commentaires ni les maquettes, et n'a pas encore tourné sur notre Azure DevOps.

Pour avancer, j'aurais besoin de :

1. Ton avis sur la démarche et sur les conventions Gherkin proposées.
2. 3 US déjà traitées à la main, pour comparer les cas de l'agent à des cas validés.
3. L'accord pour envoyer le PRD et le DAG à l'outil IA, ou le nom de la personne qui peut le donner.
4. Une personne qui reprendra le suivi du contexte projet après ma mission, pour qu'il reste à jour.

Dès que j'ai les 3 US, je fais l'essai et je te présente les mesures : nombre de cas inventés (objectif zéro), cas acceptés sans retouche, temps de rédaction. Si l'agent ne fait pas mieux que l'actuel, on garde l'actuel.

Bonne journée,
Daura

Pièces jointes : Agent-QC-actuel-vs-propose.pptx, InfoCAC-agents-QA.pptx
