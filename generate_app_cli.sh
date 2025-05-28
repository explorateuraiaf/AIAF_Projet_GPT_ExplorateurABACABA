#!/bin/bash

APP_DIR="src"
MODULE_NAME="cli"

echo "📦 Création de l'architecture de l'application CLI..."

mkdir -p "$APP_DIR/$MODULE_NAME"

# Fichier main.py
cat << EOF > "$APP_DIR/main.py"
import argparse
from cli import generate, evaluate

def main():
    parser = argparse.ArgumentParser(description="🎯 Explorateur AIAF – Assistant CLI")
    parser.add_argument("--generate", help="Génère un prompt à partir d’un template", action="store_true")
    parser.add_argument("--evaluate", help="Évalue un prompt donné", action="store_true")
    args = parser.parse_args()

    if args.generate:
        generate.run()

    if args.evaluate:
        evaluate.run()

if __name__ == "__main__":
    main()
EOF

# __init__.py
touch "$APP_DIR/$MODULE_NAME/__init__.py"

# generate.py
cat << EOF > "$APP_DIR/$MODULE_NAME/generate.py"
def run():
    print("🛠 Génération de prompt en cours...")
    # Implémente ici la logique de génération à partir d'un template
EOF

# evaluate.py
cat << EOF > "$APP_DIR/$MODULE_NAME/evaluate.py"
def run():
    print("🧪 Évaluation de prompt en cours...")
    # Implémente ici ta logique d'évaluation
EOF

# setup.py
cat << EOF > setup.py
from setuptools import setup, find_packages

setup(
    name="explorateur_cli",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "explorateur=main:main"
        ]
    },
)
EOF

echo "✅ Structure CLI générée avec succès."
echo "👉 Exécute : pip install -e ."
echo "👉 Puis : explorateur --generate"
