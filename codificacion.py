#Mi comentario
"""Mi comentario
de varias lineas"""

def validar(message):
    #whiel se ejecurara varias veces y finalizara cuando se ejecute return
    while True:
        try:
            #En esta linea pedimos un valor de tipo flotante
            data=float(input("Coloca" + message))
            #Si el valor es de tipo flotante regresamos el valor
            return data        
        except ValueError:
            #SE imprime el mensaje cuando surge un error en try
            print("El dato debe ser entero o decimal")

#Datos de entrada
largo=validar("Coloca el largo en metros:")
ancho = validar("Coloca el ancho en metros:")
m2xcaja = validar("Coloca los metros cuadrados por caja:")
precioxm2 = validar("Coloca el precio por metro cuadrado:")
""" Regla de tres
1m2=162
1.5m2=? """
precioxcaja = (m2xcaja * precioxm2)
#Estamos obteniendo los metros cuadrados que tiene el cuarto
m2Cuarto = largo * ancho
#Cuantas veces caben a loseta de la caja en el cuarto
cajas = m2Cuarto/m2xcaja
#Obetenr el precio de todas las cajas 
precioTotal= cajas * precioxcaja
print("Total de cajas que se necesitan: ", cajas)
print("Precio total", precioTotal)