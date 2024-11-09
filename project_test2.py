import unittest 
import buscarpatron as bp

class Project_test_Buscar_Patrones(unittest.TestCase):
    def test_contar_patron(self):
        numero = bp.contar_patron([1, 3, 5, 7, 9, 18], 5)
        esperado = 3 
        self.assertEqual(numero, esperado)


