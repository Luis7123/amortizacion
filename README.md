# Calculo de las amortizaciones e intereses mensuales.

- Empleamos el codigo para conocer el interés existente al dejar un compra a cuotas mensuales, conocer cuanto fue el dinero invertido y el dinero que se invertira, viendo que tan rentable sale al paso de los años
- El caso de prueba .csv es el DataFrame con las respectivas pruebas.
- el caso de prueba .py estaran los unnitest.   
## Ejemplo de ejecución.
    compra = 200000 # Cantidad de dinero gastado en el producto
    interes = 3.1   # Interes puesto por entidad financiera
    plazo = 36      # Cantidad de meses en el cual se pagará la cuota
    
    
    dataf(compra,interes,plazo)

ecuacion usada para el interes 
``` math
\frac{compra * interes} {1 - (1 + interes)^{-plazo}}
```
![image](https://github.com/Luis7123/amortizacion/assets/88041788/f9036d6a-135f-4ec2-92b3-4e363b02949a)

