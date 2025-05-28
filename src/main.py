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
