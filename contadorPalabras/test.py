import unittest
from contadorPalabras import contador
class TestCountLetters(unittest.TestCase):
    def test_simple(self):
        result = contador("hola")
        self.assertEqual(result, {"hola":1})
    def test_Dos(self):
        result = contador("hola como como andas todo bien")
        self.assertEqual(result, {"andas":1,"bien":1,"como":2,"hola":1,"todo":1})

if __name__ == '__main__':
    unittest.main()