# Agent QA : analyse critique de la version proposée

Date : 20/10/2026. Porte sur l'agent au format Claude Code (`notes-lecture/`), ses six skills, le contexte projet et les présentations de `doc/`.

## Ce qui tient

1. Le découpage est propre : l'agent porte les règles, les skills la méthode, le contexte la connaissance du projet, le script le contrôle sans IA.
2. Le principe « rien d'inventé » est outillé : chaque règle a un statut, une règle floue devient une question, le script refuse les résultats vagues. Testé : 0 erreur sur l'US 417829, les 6 erreurs attendues trouvées sur un exemple volontairement mauvais.
3. La configuration Azure DevOps est sortie de l'agent : le même agent sert à n'importe quel projet.
4. Les présentations gardent les points forts de l'agent actuel et disent : si les mesures ne sont pas meilleures, on garde l'agent actuel.

## Ce qui est faible

| # | Faiblesse | Pourquoi c'est un problème | Correction proposée |
|---|---|---|---|
| 1 | Rien n'a tourné pour de vrai | La comparaison oppose une vraie sortie d'agent à une application manuelle des consignes | Lancer l'agent dans Claude Code sur l'US 417829 avant de montrer les résultats |
| 2 | Le dépôt est public | Les présentations de `doc/` nomment le projet et critiquent un outil interne | Passer le dépôt en privé, ou retirer `doc/` |
| 3 | Personne ne tient le contexte après la fin de la mission | Un contexte non tenu devient faux, et un agent qui lit un contexte faux fait pire que pas d'agent | Nommer un responsable avant le déploiement |
| 4 | La mesure n'est pas outillée | Les 3 US de référence et la cible « zéro cas inventé » ne sont écrites que dans une diapo | Une grille : règles inventées, questions pertinentes, cas acceptés sans retouche, temps passé |
| 5 | Le « oui » peut devenir automatique | À la dixième US, on valide sans lire ; le contexte grossit et il est relu en entier à chaque analyse | Cinq propositions au plus par US, revue du contexte à chaque sprint |
| 6 | Une US modifiée après l'analyse n'est pas détectée | Le rapport ne note pas la révision de l'US : des scénarios publiés peuvent être faux sans que personne ne le voie | Noter la révision Azure DevOps dans le rapport, la comparer avant publication |
| 7 | Les garde-fous techniques sont fragiles | Le script lit le texte des commandes ; une écriture faite en Python lui échappe ; sans `python3` il ne tourne pas, sans le signaler ; il ne s'applique pas sous Copilot | Le vrai verrou reste un PAT en lecture seule ; tester le script sur un poste de l'équipe |
| 8 | Les conventions Gherkin ne sont pas validées par l'équipe | Français, une action par ligne, pas de tags : cohérent, mais choisi seul | Validation par la Test Manager avant le premier import |
| 9 | L'envoi du PRD et du DAG à l'outil IA n'est pas autorisé | C'est la base de `/init-contexte` | Obtenir l'accord avant tout le reste |

## Conclusion

La conception est solide ; rien n'est encore prouvé. Deux risques ne sont pas techniques : la visibilité publique du dépôt et la continuité du contexte après la fin de la mission. Priorités : points 1, 2 et 3.
