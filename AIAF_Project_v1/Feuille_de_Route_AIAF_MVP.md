# Feuille de Route de Développement – GPT Explorateur ABACABA & AIAF (MVP)

## 🗓️ Mois 1–2 : Développement du Moteur d'Aléa Certifiable (MAC)
- Implémentation de PCG64 (NumPy RNG)
- Tests statistiques NIST-like (Monobit, Runs…)
- Rapport structuré des résultats
- Couverture de tests unitaire via pytest

## 🗓️ Mois 3 : Implémentation du Moteur de Symbolisation Dynamique (MSD)
- Gestion des profils JSON : quantiles, seuils, delta
- Transformation de séquences numériques en symboliques
- Tests de robustesse des profils

## 🗓️ Mois 4 : Développement de l'Analyseur Fractal ABACABA (AFA)
- Détection de motifs ABA, ABACABA niveau 2
- Support du chevauchement des motifs
- Export des résultats d'analyse

## 🗓️ Mois 5–6 : Conception du Noyau IA Probabiliste (NIP)
- Génération stochastique et structure ABACABA
- Appels à des modèles LLM (OpenAI / Huggingface)
- Tests de conformité des séquences générées

## 🗓️ Mois 7 : Intégration finale & Interface utilisateur
- Composition de tous les modules via AIAF_Engine
- Interface utilisateur locale et cloud-ready (Streamlit, HF Spaces)
- Chargement, configuration, visualisation intégrés