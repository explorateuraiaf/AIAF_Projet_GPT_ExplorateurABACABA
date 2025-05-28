import random

def generate_prompt(template: str, variables: dict) -> str:
    return template.format(**variables)

def score_prompt(prompt: str, history: list) -> float:
    score = 0
    if any(p in prompt for p in ["probabilité", "fractal", "cohérence"]):
        score += 0.5
    score += len(set(prompt.split())) / 50  # diversité des mots
    return round(min(score, 1.0), 3)

def compare_prompts(prompts: list, history: list) -> list:
    scored = [(p, score_prompt(p, history)) for p in prompts]
    return sorted(scored, key=lambda x: x[1], reverse=True)
