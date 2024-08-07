"""
Ejercicio 2: Escribir un programa que añada valores a una lista mientras que su longitud
sea menor a 120 y luego mostrar la lista.
Plus: Usar while y for
"""

coleccion = []

for elemento in range(0, 120):
    coleccion.append(f"Elemento - {elemento}")
    print(f"Mostrando el: {coleccion[elemento]}")
    
print(coleccion)


# Plus: Usar while
coleccion2 = []
contador = 0

while contador < 120:
    coleccion2.append(f"Elemento - {contador}")
    print(f"Mostrando el: {coleccion2[contador]}")
    contador += 1

print(coleccion2)
