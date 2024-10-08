"""
Ejercicio 3. Escribir un programa que muestre los cuadrados (un número multiplicado por sí mismo) de los 60 primeros números naturales.
Resolverlo con for y con while
"""

# While
contador = 0
while contador <= 60:
    print(f"El cuadrado de {contador} es {contador * contador}")
    contador += 1

# For
contador = 0
for contador in range(61):
    print(f"El cuadrado de {contador} es {contador * contador}")
    