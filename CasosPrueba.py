import unittest
import pago
from pandas.util.testing import assert_frame_equal
import pandas.testing as pd_testing

class CreditCardTest(unittest.TestCase):

    # Cada prueba unitaria es un metodo la clase
    def testPayment1(self):
        compra = 200000
        tasa = 3.1
        plazo = 36
        cuota = 134726.5
        resultado = pago.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,1)  )

    def testPayment2(self):
        compra = 850000
        tasa = 3.4
        plazo = 24
        cuota = 407059.9
        resultado = pago.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,1)  )


    def testPayment3(self):
        compra = 850000
        tasa = 0
        plazo = 48
        cuota = 0
        resultado = pago.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,1)  )
 
    
    def testPayment4(self):
        compra = 50000
        tasa = 12.4
        plazo = 60
        cuota = 0
        resultado = pago.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,1)  )
        try:
            resultado = pago.calcularCuota( compra, tasa, plazo )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  pago.TasaExcesiva  :
            pass


    def testPayment5(self):
        compra = 90000
        tasa = 2.4
        plazo = 1
        cuota = 0
        resultado = pago.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual(cuota, round(resultado,1))

    def testPayment6(self):
        compra = 0
        tasa = 2.4
        plazo = 60
        cuota = 0
        resultado = pago.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual(cuota, round(resultado,1))
        try:
            resultado = pago.calcularCuota( compra, tasa, plazo )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  pago.montoInexistente  :
            pass

    def testPayment7(self):
        compra = 50000
        tasa = 1
        plazo = -10
        cuota = 0
        resultado = pago.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual(cuota, round(resultado,1))
        try:
            resultado = pago.calcularCuota( compra, tasa, plazo )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  pago.plazoNegativo  :
            pass
        

if __name__ == '__main__':
    unittest.main()
