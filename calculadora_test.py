import unittest 
import calculadora as c

class TestCaseCalculadora(unittest.TestCase):
    def test_sumar(self):
        num1, num2 = 3, 6
        respuesta = c.sumar(num1, num2)
        expected = 9
        self.assertEqual(respuesta, expected)

