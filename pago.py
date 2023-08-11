class interesInexistente( Exception ): 
    pass
class TasaExcesiva( Exception ): 
    pass
class montoInexistente( Exception ): 
    pass
class montoNegativo( Exception ): 
    pass
class plazoNegativo( Exception ): 
    pass

import pandas as pd
def calcularCuota (compra, interes, plazo):
    if interes == 0 :
        return 0
    
    if interes*12 > 100:
        raise TasaExcesiva( "La tasa no debe ser superior a 100")
    
    if plazo == 1: 
        return 0
    
    if compra <= 0: 
        if compra== 0 :
            raise montoInexistente( "debe existir un monto")
        else:
            raise montoNegativo( "monto negativo")
        
    if plazo <= 0: 
        if plazo== 0 :
            return 0
        else:
            raise plazoNegativo( "el plazo debe ser positivo")    
    else:
        i= interes/100
        cuota=(compra * i) / (1 - (1 + i) ** (-plazo))
        return (cuota*plazo) - compra 
    
a=[1,2,3,4,5]
df= pd.DataFrame(a,columns=["Numeros"])
print(df)