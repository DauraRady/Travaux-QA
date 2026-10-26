# Cas de test : gestion des demandes

Cas de test manuels rédigés en Gherkin pour Azure Test Plans. Toutes les données sont fictives.

| Fichier | Fonctionnalité | Cas |
|---|---|---|
| `creer-une-demande.md` | Création d'une demande depuis la liste | Nominaux, négatifs, robustesse |
| `consulter-la-liste-des-demandes.md` | Affichage du tableau, statuts, Retard, tri, pagination | 8 nominaux, 4 négatifs, 3 limites |
| `filtrer-les-demandes.md` | Filtres combinables et recherche | 9 nominaux, 3 négatifs, 2 limites |
| `sprint-3/` | Les 10 US du sprint 3 : engagement, contrôles à la création, recherche, en-tête, section Description du mandat | 58 scénarios, 133 exécutions ; index et questions dans `sprint-3/README.md` |

## Passage vers Azure Test Plans

| Gherkin | Azure Test Plans |
|---|---|
| Titre du scénario | Titre du cas |
| Contexte commun | Étape partagée, insérée en pas 1 |
| Étant donné / Et que | Action du pas 1, résultat attendu vide |
| Quand | Action du pas 2 |
| Alors / Et | Résultat attendu du pas 2 |
| `<param>` et Exemples | `@param` et grille Parameter values |
