import json
from datetime import datetime

def generate_markdown_report(data, template_path):
    with open(template_path, "r") as f:
        template = f.read()
    for key, value in data.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))
    return template

def simulate_ia_interaction(prompt):
    # Simulation IA simple
    response = f"Réponse simulée pour le prompt : {prompt}"
    score = len(prompt.split()) / 10.0
    return {
        "prompt": prompt,
        "response": response,
        "score": round(min(score, 1.0), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

def save_interaction_log(entry, log_path):
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            log = json.load(f)
    else:
        log = []
    log.append(entry)
    with open(log_path, "w") as f:
        json.dump(log, f, indent=2)
