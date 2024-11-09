import unittest 

import function3 as nm

class Test_Notas (unittest.TestCase):
    def test_media_notas_one(self):
        """ Wether the average mark is correctly calculated for one student"""
        estudiante = {'Ana': [5, 5, 5, 5]}
        respuesta = nm.nota_media(estudiante, 'Ana')
        esperada = 5
        self.assertEqual(respuesta, esperada)

    def test_media_notas_one_dos_decimales(self):
        """ Wether the average mark is correctly calculated for one student. With 2 decimals"""
        estudiante = {'Ana': [10, 1, 0]}
        respuesta = nm.nota_media(estudiante, 'Ana')
        esperada = 3.67
        self.assertEqual(respuesta, esperada)
        
    def test_media_varios_alumnos(self):
        """ Wether the average mark is correctly calculated for one student among several students"""
        estudiante = {'Ana': [10, 1, 0], 'Pepe': [2, 6, 9, 10, 10], 'Maria': [5]}
        respuesta = nm.nota_media(estudiante, 'Pepe')
        esperada = 7.4
        self.assertEqual(respuesta, esperada)

    def test_media_notas_lista_vacia(self):
        """ Wether the average mark is correctly calculated when the marks list is empty"""
        estudiante = {'Ana': []}
        respuesta = nm.nota_media(estudiante, 'Ana')
        esperada = None
        self.assertEqual(respuesta, esperada)

    def test_media_notas_student_unknown(self):
        """ Wether the function warns that the student is not in the dictionary"""
        estudiante = {'Ana': [10, 1, 0]}
        respuesta = nm.nota_media(estudiante, 'Pepe')
        esperada = None
        self.assertEqual(respuesta, esperada)

    def test_media_notas_student_floats(self):
        """ Wether the average mark is correctly calculated for student with floats marks"""
        estudiante = {'Ana': [8.2, 1.6, 0.2]}
        respuesta = nm.nota_media(estudiante, 'Ana')
        esperada = 3.33
        self.assertEqual(respuesta, esperada)
    
    def test_media_notas_entrada_vacia(self):
        """ Wether the function warns that the input is empty"""
        estudiante = None
        respuesta = nm.nota_media(None, 'Ana')
        esperada = None
        self.assertEqual(respuesta, esperada)

    def test_media_notas_entrada_vacia2(self):
        """ Wether the function warns that the input is empty"""
        estudiante = {'Ana': [8.2, 1.6, 0.2]}
        respuesta = nm.nota_media(estudiante, None)
        esperada = None
        self.assertEqual(respuesta, esperada)
