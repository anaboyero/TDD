import unittest
import file_max_cell as fc 

""" FUNCTION REQUIREMENTS

It requieres a csv and the name of the column.
Ir returns the max value of the columns: row, column

    Alumno  Edad     Localidad  Examen

001    Juan   30       Madrid      8 

002     Ana    22       Barcelona  9 
    
003    Pedro  21       Valencia   10 



Si le digo (alumnos.csv, Examen)

Devolvería: (003, 10) 

Si le digo (alumnos.csv, Edad)

Devolvería: (001, 30) 

"""


class Project_test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(1, 1)

    def test_max_cell(self):
        a_max, a_series = fc.file_max_cell("scores.csv", "math score")
        self.assertEqual(a_max, 100)
        self.assertEqual(len(a_series), 8)

