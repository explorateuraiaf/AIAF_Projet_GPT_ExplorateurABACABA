import unittest
from aiaf_core.prompt_optimizer import generate_prompt, score_prompt, compare_prompts

class TestPromptOptimizer(unittest.TestCase):
    def test_generate_prompt(self):
        template = "Quel est le score de {motif} dans {jeu} ?"
        variables = {"motif": "ABACABA", "jeu": "EuroMillions"}
        result = generate_prompt(template, variables)
        self.assertIn("ABACABA", result)
        self.assertIn("EuroMillions", result)

    def test_score_prompt(self):
        score = score_prompt("Analyse fractale de probabilité", [])
        self.assertGreaterEqual(score, 0.5)

    def test_compare_prompts(self):
        prompts = ["A", "probabilité fractale", "motif aléatoire"]
        results = compare_prompts(prompts, [])
        self.assertTrue(results[0][1] >= results[-1][1])

if __name__ == "__main__":
    unittest.main()
