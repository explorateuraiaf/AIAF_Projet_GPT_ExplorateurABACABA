import unittest
from aiaf_core.afa_engine import generate_abacaba_sequence, is_abacaba_like

class TestAfaEngine(unittest.TestCase):
    def test_generate(self):
        self.assertEqual(generate_abacaba_sequence(0), "A")
        self.assertEqual(generate_abacaba_sequence(1), "ABA")
        self.assertEqual(generate_abacaba_sequence(2), "ABACABA")

    def test_is_like(self):
        self.assertTrue(is_abacaba_like("A"))
        self.assertTrue(is_abacaba_like("ABA"))
        self.assertTrue(is_abacaba_like("ABACABA"))
        self.assertFalse(is_abacaba_like("ABC"))

if __name__ == "__main__":
    unittest.main()
