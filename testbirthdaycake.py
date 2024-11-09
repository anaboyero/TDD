import unittest 
import birthdaycake as bc

class project_test_birthday_cake(unittest.TestCase):
    
    def test_count_longest_candles(self):
        test_list = [1, 2, 3, 4]
        answer = bc.birthday_cake(test_list)
        expected = 1
        self.assertEqual(answer, expected)


    def test_count_longest_candles_empty_list(self):
        test_list = []
        answer = bc.birthday_cake(test_list)
        expected = 0
        self.assertEqual(answer, expected)


    def test_count_longest_candles_not_a_list(self):
        test_list = True
        answer = bc.birthday_cake(test_list)
        expected = 0
        self.assertEqual(answer, expected)







"""
- Contar velas - OK
- Entrada nula
- Entrada no es lista
- Entrada lista vacía- OK
- Alturas negativas

""" 