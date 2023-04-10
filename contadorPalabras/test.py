import unittest
from contadorPalabras import contadorPalabras
class TestCountLetters(unittest.TestCase):
    def test_simple(self):
        result = contadorPalabras('hola')
        self.assertEqual(result, {"hola":1})

if __name__ == '__main__':
    unittest.main()