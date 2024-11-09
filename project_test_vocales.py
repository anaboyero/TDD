import unittest
import correr_vocales as cv

class Project_test_vocales(unittest.TestCase):
    def test_vocales(self):
        cadena_test = "aeiou"
        respuesta = cv.correr_vocales(cadena_test)
        esperada = "eioua"
        self.assertEqual(respuesta, esperada)

    def test_vocales_mayus(self):
        cadena_test = "aEiOu"
        respuesta = cv.correr_vocales(cadena_test)
        esperada = "eIoUa"
        self.assertEqual(respuesta, esperada)

    def test_vocales_soloconsonantes(self):
        cadena_test = "dftGHW"
        respuesta = cv.correr_vocales(cadena_test)
        esperada = "dftGHW"
        self.assertEqual(respuesta, esperada)

    def test_vocales_cadenavacia(self):
        cadena_test = ""
        respuesta = cv.correr_vocales(cadena_test)
        esperada = ""
        self.assertEqual(respuesta, esperada)
    
    def test_vocales_sinparametro(self):
        cadena_test = None
        respuesta = cv.correr_vocales(cadena_test)
        esperada = "No hay ninguna cadena que transformar"
        self.assertEqual(respuesta, esperada)
    
    def test_vocales_numero(self):
        cadena_test = 15
        respuesta = cv.correr_vocales(cadena_test)
        esperada = "Por favor, introduzca una cadena de texto"
        self.assertEqual(respuesta, esperada)

    def test_vocales_fraseconespacios(self):
        cadena_test = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme"
        respuesta = cv.correr_vocales(cadena_test)
        esperada = "In an lager di le Menche, di cayu numbri nu qaoiru ecurdermi"
        self.assertEqual(respuesta, esperada)

    
    
    




