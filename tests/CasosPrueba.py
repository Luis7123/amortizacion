import unittest
import payments
from pandas.util.testing import assert_frame_equal
import pandas.testing as pd_testing

class CreditCardTest(unittest.TestCase):

    #Evert unittest it's a method of the class
    def testPayment1(self):
        amount = 200000
        interest = 3.1
        payment_time = 36
        cuota = 134726.5
        result = payments.calcularCuota( amount, interest, payment_time )
        # Test to see if 2 variables are equal
        self.assertEqual( cuota, round(result,1)  )

    def testPayment2(self):
        amount = 850000
        interest = 3.4
        payment_time = 24
        cuota = 407059.9
        result = payments.calcularCuota( amount, interest, payment_time )
        # Test to see if 2 variables are equal

        self.assertEqual( cuota, round(result,1)  )


    def testPayment3(self):
        amount = 850000
        interest = 0
        payment_time = 48
        cuota = 0
        result = payments.calcularCuota( amount, interest, payment_time )
        # Test to see if 2 variables are equal
        self.assertEqual( cuota, round(result,1)  )
 
    
    def testPayment4(self):
        amount = 50000
        interest = 12.4
        payment_time = 60
        cuota = 0
        result = payments.calcularCuota( amount, interest, payment_time )
        # Test to see if 2 variables are equal
        self.assertEqual( cuota, round(result,1)  )
        try:
            result = payments.calcularCuota( amount, interest, payment_time )
        
            self.assertEqual( result, 0 )  
        except  payments.interestExcesiva  :
            pass


    def testPayment5(self):
        amount = 90000
        interest = 2.4
        payment_time = 1
        cuota = 0
        result = payments.calcularCuota( amount, interest, payment_time )
        # Test to see if 2 variables are equal
        self.assertEqual(cuota, round(result,1))

    def testPayment6(self):
        amount = 0
        interest = 2.4
        payment_time = 60
        cuota = 0
        result = payments.calcularCuota( amount, interest, payment_time )
        # Test to see if 2 variables are equal
        self.assertEqual(cuota, round(result,1))
        try:
            result = payments.calcularCuota( amount, interest, payment_time )
           
            self.assertEqual( result, 0 ) 
        except  payments.montoInexistente  :
            pass

    def testPayment7(self):
        amount = 50000
        interest = 1
        payment_time = -10
        cuota = 0
        result = payments.calcularCuota( amount, interest, payment_time )
        # Test to see if 2 variables are equal
        self.assertEqual(cuota, round(result,1))
        try:
            result = payments.calcularCuota( amount, interest, payment_time )
            
            self.assertEqual( result, 0 )  
        except  payments.payment_timeNegativo  :
            pass
    
    def testAmortizacion(self):
        amount = 850000
        interest = 3.4
        payment_time = 24
        deposit=90000
        month_deposit =  5
        df_amortization = payments.dataframe_amortizacion( amount, interest, payment_time ,deposit, month_deposit )
        
        list_df_amortization = list(df_amortization.iloc[1])
        list_correct_values=[52.377 , 28.900 , 23.477 ,826.522]
        self.assert_frame_equal(pd.DataFrame(list_correct_values),pd.DataFrame(list_df_amortization))
        

if __name__ == '__main__':
    unittest.main()
