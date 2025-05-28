# Comparateur de Prompts – Phase N5

Ce module permet de générer, scorer et comparer des prompts.
Chaque prompt est évalué selon sa richesse lexicale et son alignement avec les mots-clés du projet.

## Exemples de prompts testés

- "Analyse fractale de probabilité" (score élevé)
- "Motif aléatoire avec structure symétrique"
- "Quel est le prochain tirage du loto ?"

## Méthodes disponibles

- `generate_prompt(template, variables)`
- `score_prompt(prompt, history)`
- `compare_prompts(prompts, history)`
