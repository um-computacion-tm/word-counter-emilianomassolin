from romanToDecimal import roman_to_decimal
import unittest
class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)
    def test_II(self):
        resultado = roman_to_decimal('II')
        self.assertEqual(resultado, 2)    
    def test_IV(self):
        resultado = roman_to_decimal('IV')
        self.assertEqual(resultado, 4)  
    def test_IX(self):
        resultado = roman_to_decimal('IX')
        self.assertEqual(resultado, 9) 
    def test_XL(self):
        resultado = roman_to_decimal('XL')
        self.assertEqual(resultado, 40)     
    
    def test_XC(self):
        resultado = roman_to_decimal('XC')
        self.assertEqual(resultado, 90)   
    def test_C(self):
        resultado = roman_to_decimal('C')
        self.assertEqual(resultado, 100)  
    def test_CD(self):
        resultado=roman_to_decimal('CD')
        self.assertEqual(resultado,400)    
    def test_CDL(self):
        resultado=roman_to_decimal('CDL')
        self.assertEqual(resultado,450)     
    def test_DLX(self):
        resultado=roman_to_decimal('DLX')
        self.assertEqual(resultado,560)    
    def test_DLXII(self):
        resultado=roman_to_decimal('DLXII')
        self.assertEqual(resultado,562)    
  
  


if __name__ == '__main__':
    unittest.main()