import unittest
import prism as p 

class TestVolumeCube (unittest.TestCase):

    def test_volume(self):
        """ Does the funciton correctly calculates the volume of a cube?"""
        test_prism = [2, 3, 4]
        answer = p.calculate_volume(test_prism)
        expected = 24
        self.assertEqual(answer, expected) 

    def test_volume_empty_list(self):
        """ Does it warn when it receives an empty list?"""
        test_prism = []
        answer = p.calculate_volume(test_prism)
        expected = 0
        self.assertEqual(answer, expected) 

    def test_volume_not_3Dlist(self):
        """ Does the function warn when it receives a non 3D list?"""
        test_prism = [2, 3]
        answer = p.calculate_volume(test_prism)
        expected = -1
        self.assertEqual(answer, expected) 
    
