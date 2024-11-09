import unittest
import primos as p

class TestCasePrimos(unittest.TestCase):
    def test_es_primo(self):
        self.assertTrue(p.es_primo(2))
        self.assertTrue(p.es_primo(5))
        self.assertFalse(p.es_primo(8))

    def test_es_primo_menor2(self):
        self.assertFalse(p.es_primo(-1))
        self.assertFalse(p.es_primo(0))
        self.assertFalse(p.es_primo(-10))