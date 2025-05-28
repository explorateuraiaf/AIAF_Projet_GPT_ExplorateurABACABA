import unittest
from aiaf_core.nip_engine import calculate_probabilities

class TestNipEngine(unittest.TestCase):
    def test_distribution(self):
        self.assertEqual(calculate_probabilities([1, 2, 2]), {1: 1/3, 2: 2/3})

    def test_empty(self):
        self.assertEqual(calculate_probabilities([]), {})

if __name__ == "__main__":
    unittest.main()
