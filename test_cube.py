import unittest
import cube as c

class TestVolumeCube (unittest.TestCase):
    def test_volumen(self):
        side_test = 3
        answer = c.volumen_cube(side_test)
        expected = 27 
        self.assertEqual(answer, expected)

    def test_volumen_emptyinput(self):
        side_test = None
        answer = c.volumen_cube(side_test)
        expected = 0 
        self.assertEqual(answer, expected)
    
    def test_volumen_nonpositive(self):
        side_test = -5
        answer = c.volumen_cube(side_test)
        expected = -1 
        self.assertEqual(answer, expected)






