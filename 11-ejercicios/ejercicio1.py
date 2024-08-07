"""
Ejercicio 1: Crear un programa que tenga una lista de 8 elementos y que haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer una función que recorra listas de números y devuelva un string con el número mayor
- Ordenarla y buscarla
- Mostrar su longitud
- Buscar algún elemento (que el usuario pida por teclado)
"""

# Crear una lista
numeros = [13, 56, 78, 23, 45, 67, 89, 12]

# Recorrer la lista y mostrarla
print("**********LISTADO DE NÚMEROS**********")
print("-----------------------------------")
for numero in numeros:
    print(numero)
print("\n")

# Función que recorra listas de números y devuelva un string con el número mayor
def devolverMayor(lista):
    mayor = 0
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    return f"El número mayor es: {mayor}"

print(devolverMayor(numeros))

# Ordenar la lista
numeros.sort()
print(numeros)

# Buscar un elemento
busqueda = int(input("Introduce el número a buscar: "))
comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el número a buscar: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"### Buscar en la lista el número {busqueda} ###")

search = numeros.index(busqueda)

if search:
    print(f"El número {busqueda} se encuentra en la posición {search} de la lista")
else:
    print("El número no está en la lista")

# Mostrar la longitud de la lista
print(len(numeros))
