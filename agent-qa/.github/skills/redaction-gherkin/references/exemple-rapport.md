# QC agent : US 9001 Valider une demande (exemple fictif)

## 4- Cas de test


### TC-01 - Valider une demande soumise la fait passer au statut Validée
| AC | Règle | Famille | Priorité | État |
|---|---|---|---|---|
| AC-1 | R1 | Nominal | 1 | Exécutable |

Technique : transitions d'état (transition autorisée de R1)
Détecte : une validation qui laisse la demande au statut Soumise ou la passe à un autre statut.

```gherkin
Scénario: Valider une demande soumise la fait passer au statut Validée
  Étant donné que l'utilisateur "VAL-TEST-01" est connecté avec le rôle "Valideur"
  Et que la demande "DEM-TEST-01" est au statut "Soumise"
  Quand il valide la demande "DEM-TEST-01"
  Alors la demande "DEM-TEST-01" est au statut "Validée"
```

### TC-02 - Une demande en brouillon ne peut pas être validée
| AC | Règle | Famille | Priorité | État |
|---|---|---|---|---|
| AC-2 | R2 | Négatif | 1 | Exécutable |

Technique : transitions d'état (transition interdite décrite par R2)
Détecte : une demande en brouillon validée malgré le message de refus.

```gherkin
Scénario: Une demande en brouillon ne peut pas être validée
  Étant donné que l'utilisateur "VAL-TEST-01" est connecté avec le rôle "Valideur"
  Et que la demande "DEM-TEST-02" est au statut "Brouillon"
  Quand il tente de valider la demande "DEM-TEST-02"
  Alors le message "Seules les demandes soumises peuvent être validées" est affiché
  Et la demande "DEM-TEST-02" est toujours au statut "Brouillon"
```

### TC-03 - La saisie du commentaire de validation s'arrête à 500 caractères
| AC | Règle | Famille | Priorité | État |
|---|---|---|---|---|
| AC-3 | R3 | Limite | 3 | Exécutable |

Technique : valeurs limites (juste au-delà de la borne de R3)
Détecte : un champ qui accepte un 501e caractère.

```gherkin
Scénario: La saisie du commentaire de validation s'arrête à 500 caractères
  Étant donné que l'utilisateur "VAL-TEST-01" est connecté avec le rôle "Valideur"
  Et que la demande "DEM-TEST-03" est au statut "Soumise"
  Quand il saisit un commentaire de "501" caractères sur la demande "DEM-TEST-03"
  Alors le champ commentaire contient "500" caractères
```


## 5- Cas limites
