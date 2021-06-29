largo=float(input("Coloca el largo en metros:"))
ancho = float(input("Coloca el ancho en metros:"))
m2xcaja = float(input("Coloca los metros cuadrados por caja:"))
precioxm2 = float(input("Coloca el precio por metro cuadrado:"))
precioxcaja = (m2xcaja * precioxm2)
m2Cuarto = largo * ancho
cajas = m2Cuarto/m2xcaja
precioTotal= cajas * precioxcaja
print("Total de cajas que se necesitan: ", cajas)
print("Precio total", precioTotal)