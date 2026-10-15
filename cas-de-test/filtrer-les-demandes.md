# Filtrer les demandes : cas de test

Données fictives uniquement. Dans ADO, remplacer `<param>` par `@param` et saisir les Exemples dans la grille Parameter values. Le Contexte devient une étape partagée (« Jeu de données filtres DEM-F01 à F05 ») insérée en pas 1 de chaque cas.

```gherkin
# language: fr
Fonctionnalité: Filtrer les demandes

  Contexte:
    Étant donné que les demandes suivantes existent :
      | demande | pays    | millesime | type_mandat                            | categorie      | statut      | bu_region | signataire_cac | signataire_durabilite |
      | DEM-F01 | France  | 2026      | Certification des comptes              | Nouveau        | En cours    | BU-TEST-1 | SIG-TEST-A     |                       |
      | DEM-F02 | Maroc   | 2025      | Durabilité                             | Renouvellement | En cours    |           |                | SIGD-TEST-B           |
      | DEM-F03 | France  | 2027      | Certification des comptes & Durabilité | Reprise        | Analyse OCR | BU-TEST-2 | SIG-TEST-A     | SIGD-TEST-B           |
      | DEM-F04 | Sénégal | 2024      | Audit contractuel                      | Nouveau        | En cours    |           | SIG-TEST-C     |                       |
      | DEM-F05 | France  | 2026      | Certification des comptes              | Renouvellement | Analyse OCR | BU-TEST-1 | SIG-TEST-C     |                       |

  # ---------- Cas nominaux ----------

  Scénario: TC01 À l'ouverture, aucun filtre n'est sélectionné et toutes les demandes sont affichées
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Quand j'accède à la "Liste des demandes"
    Alors aucun filtre n'est sélectionné
    Et les demandes "DEM-F01", "DEM-F02", "DEM-F03", "DEM-F04" et "DEM-F05" sont affichées

  Plan du scénario: TC02 Filtrer la liste sur une valeur du filtre <filtre>
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que je suis sur la "Liste des demandes"
    Quand je sélectionne "<valeur>" dans le filtre "<filtre>"
    Alors les demandes <visibles> sont affichées
    Et les demandes <absentes> ne sont pas affichées

    Exemples:
      | filtre                | valeur      | visibles                  | absentes                           |
      | Pays                  | France      | DEM-F01, DEM-F03, DEM-F05 | DEM-F02, DEM-F04                   |
      | Millésime             | 2026        | DEM-F01, DEM-F05          | DEM-F02, DEM-F03, DEM-F04          |
      | Type de mandat        | Durabilité  | DEM-F02                   | DEM-F01, DEM-F03, DEM-F04, DEM-F05 |
      | Catégorie de mandat   | Reprise     | DEM-F03                   | DEM-F01, DEM-F02, DEM-F04, DEM-F05 |
      | Statut                | Analyse OCR | DEM-F03, DEM-F05          | DEM-F01, DEM-F02, DEM-F04          |
      | Signataire CAC        | SIG-TEST-A  | DEM-F01, DEM-F03          | DEM-F02, DEM-F04, DEM-F05          |
      | Signataire Durabilité | SIGD-TEST-B | DEM-F02, DEM-F03          | DEM-F01, DEM-F04, DEM-F05          |

  Scénario: TC03 Sélectionner deux pays affiche les demandes des deux pays
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que je suis sur la "Liste des demandes"
    Quand je sélectionne "France" et "Maroc" dans le filtre "Pays"
    Alors les demandes "DEM-F01", "DEM-F02", "DEM-F03" et "DEM-F05" sont affichées
    Et la demande "DEM-F04" n'est pas affichée

  Scénario: TC04 Combiner deux filtres affiche seulement les demandes qui répondent aux deux
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que le filtre "Pays" est positionné sur "France"
    Quand je sélectionne "2026" dans le filtre "Millésime"
    Alors les demandes "DEM-F01" et "DEM-F05" sont affichées
    Et les demandes "DEM-F02", "DEM-F03" et "DEM-F04" ne sont pas affichées

  Scénario: TC05 Sélectionner une BU/Région sélectionne automatiquement le pays France
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que je suis sur la "Liste des demandes"
    Quand je sélectionne "BU-TEST-1" dans le filtre "BU/Région"
    Alors les demandes "DEM-F01" et "DEM-F05" sont affichées
    Et les demandes "DEM-F02", "DEM-F03" et "DEM-F04" ne sont pas affichées
    Et le pays "France" est sélectionné dans le filtre "Pays"

  Scénario: TC06 Combiner un filtre et la recherche
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que le filtre "Pays" est positionné sur "France"
    Quand je saisis "DEM-F05" dans le champ de recherche
    Alors seule la demande "DEM-F05" est affichée

  Scénario: TC07 Retirer un filtre met la liste à jour avec les filtres restants
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que le filtre "Pays" est positionné sur "France"
    Et que le filtre "Millésime" est positionné sur "2026"
    Quand je retire la valeur "2026" du filtre "Millésime"
    Alors les demandes "DEM-F01", "DEM-F03" et "DEM-F05" sont affichées
    Et les demandes "DEM-F02" et "DEM-F04" ne sont pas affichées

  Scénario: TC08 Retirer tous les filtres réaffiche toutes les demandes
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que le filtre "Pays" est positionné sur "France"
    Et que le filtre "Statut" est positionné sur "Analyse OCR"
    Quand je retire toutes les valeurs sélectionnées
    Alors les demandes "DEM-F01", "DEM-F02", "DEM-F03", "DEM-F04" et "DEM-F05" sont affichées

  Plan du scénario: TC09 Le rôle <role> peut filtrer la liste
    Étant donné que je suis connecté avec le compte "<compte>" ayant le rôle "<role>"
    Et que je suis sur la "Liste des demandes"
    Quand je sélectionne "Maroc" dans le filtre "Pays"
    Alors la demande "DEM-F02" est affichée
    Et les demandes "DEM-F01", "DEM-F03", "DEM-F04" et "DEM-F05" ne sont pas affichées

    Exemples:
      | compte     | role       |
      | AD-TEST-01 | Admin      |
      | SA-TEST-01 | SuperAdmin |
      | US-TEST-01 | User       |

  # ---------- Cas négatifs ----------

  Scénario: TC10 Le type Certification des comptes n'affiche pas les demandes Certification des comptes & Durabilité
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que je suis sur la "Liste des demandes"
    Quand je sélectionne "Certification des comptes" dans le filtre "Type de mandat"
    Alors les demandes "DEM-F01" et "DEM-F05" sont affichées
    Et la demande "DEM-F03" n'est pas affichée

  Scénario: TC11 Une combinaison sans résultat affiche un tableau vide
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que le filtre "Pays" est positionné sur "Maroc"
    Quand je sélectionne "2026" dans le filtre "Millésime"
    Alors le tableau des demandes est vide

  # Bloqué Q2 : l'US dit choix unique, la maquette dit multiselect
  Scénario: TC12 Le filtre Signataire CAC n'accepte qu'une seule personne
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que "SIG-TEST-A" est sélectionné dans le filtre "Signataire CAC"
    Quand je sélectionne "SIG-TEST-C" dans le filtre "Signataire CAC"
    Alors "SIG-TEST-C" remplace "SIG-TEST-A" dans le filtre "Signataire CAC"
    Et les demandes "DEM-F04" et "DEM-F05" sont affichées
    Et les demandes "DEM-F01" et "DEM-F03" ne sont pas affichées

  # ---------- Cas limites ----------

  # À confirmer Q3 : millésime actuel 2026 ou 2027 depuis le 1er octobre
  Scénario: TC13 Le filtre Millésime propose les années N-2 à N+2
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que je suis sur la "Liste des demandes"
    Quand j'ouvre le filtre "Millésime"
    Alors les valeurs proposées sont "2024", "2025", "2026", "2027" et "2028"
    Et les valeurs "2023" et "2029" ne sont pas proposées

  Scénario: TC14 Une demande au millésime N-2 est trouvée par le filtre
    Étant donné que je suis connecté avec le compte "AD-TEST-01" ayant le rôle "Admin"
    Et que je suis sur la "Liste des demandes"
    Quand je sélectionne "2024" dans le filtre "Millésime"
    Alors la demande "DEM-F04" est affichée
    Et les demandes "DEM-F01", "DEM-F02", "DEM-F03" et "DEM-F05" ne sont pas affichées
```

## Questions ouvertes

| Q | Question | Cas |
|---|---|---|
| Q1 | Quelles sont les valeurs du filtre BU/Région ? (BU-TEST-1 et BU-TEST-2 sont fictives) | TC05 |
| Q2 | Signataires : choix unique (US) ou multiple (maquette) ? | TC12 |
| Q3 | Millésime actuel depuis le 1er octobre : 2026 ou 2027 ? | TC13, TC14 |
| Q4 | Un User voit-il toutes les demandes ou seulement les siennes ? | TC09 |
