def validar(message):
    while True:
        try:
            data=float(input("Coloca" + message))
            return data        
        except ValueError:
            print("El dato debe ser entero o decimal")


largo=validar("Coloca el largo en metros:")
ancho = validar("Coloca el ancho en metros:")
m2xcaja = validar("Coloca los metros cuadrados por caja:")
precioxm2 = validar("Coloca el precio por metro cuadrado:")
precioxcaja = (m2xcaja * precioxm2)
m2Cuarto = largo * ancho
cajas = m2Cuarto/m2xcaja
precioTotal= cajas * precioxcaja
print("Total de cajas que se necesitan: ", cajas)
print("Precio total", precioTotal)