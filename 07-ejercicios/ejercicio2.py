"""
Ejercicio 2. Escribir un script que nos muestre por pantalla 
todos los número pares del 1 al 120

"""

contador = 1

for contador in range(1,121):
    if contador % 2 == 0:
        print(contador)
