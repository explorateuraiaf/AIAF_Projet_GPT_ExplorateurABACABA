import unittest
import os
from aiaf_core.report_generator import generate_markdown_report, simulate_ia_interaction, save_interaction_log

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        data = {"name": "Explorateur ABACABA", "score": 0.95}
        template_path = "report_template.md"
        with open(template_path, "w") as f:
            f.write("Nom : {{name}}\nScore : {{score}}")
        report = generate_markdown_report(data, template_path)
        self.assertIn("Explorateur ABACABA", report)

    def test_simulation(self):
        result = simulate_ia_interaction("Quelle est la probabilité fractale ?")
        self.assertIn("Réponse simulée", result["response"])

    def test_log_save(self):
        log_path = "interaction_log.json"
        entry = simulate_ia_interaction("Test log")
        save_interaction_log(entry, log_path)
        self.assertTrue(os.path.exists(log_path))

if __name__ == "__main__":
    unittest.main()
