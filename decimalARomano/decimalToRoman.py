import unittest

def decimal_to_roman(decimal):

    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    resultado = ''
    for i in range(len(valores)):
        while decimal >= valores[i]:
            decimal -= valores[i]
            resultado += simbolos[i]
    return resultado
     




