import unittest

def decimal_to_roman(decimal):
    total = ''
    if decimal >= 100:
        centena = decimal // 100
        total = 'C' * centena
        decimal = decimal % 100 
    if decimal <= 3:
        total += 'I' * decimal
    elif decimal == 5:
        total += 'V'
    elif decimal == 10:
        total += "X"
    return total



class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')

    def test_ciento_uno(self):
        resultado = decimal_to_roman(101)
        self.assertEqual(resultado, 'CI')

    def test_ciento_tres(self):
        resultado = decimal_to_roman(103)
        self.assertEqual(resultado, 'CIII')

    def test_ciento_cinco(self):
        resultado = decimal_to_roman(105)
        self.assertEqual(resultado, 'CV')

    def test_ciento_diez(self):
        resultado = decimal_to_roman(110)
        self.assertEqual(resultado, 'CX')

    def test_docientos_tres(self):
        resultado = decimal_to_roman(203)
        self.assertEqual(resultado, 'CCIII')



if __name__ == '__main__':
    unittest.main()