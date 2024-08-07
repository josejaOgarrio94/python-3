cantantes = ['2pac', 'Drake', 'Jennifer Lopez', 'Marc Anthony']
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar listas
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("Natos y Waor")
cantantes.insert(1, "David Bisbal")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)  # Elimina el elemento de la posición 1
cantantes.remove("Natos y Waor")  # Elimina el elemento Natos y Waor
print(cantantes)

# Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes)  # True
print('David Bisbal' in cantantes)  # False

# Contar elementos
print(cantantes)
print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir un índice
print(cantantes.index("Drake"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)
# Otra forma de unir listas
cantantes = cantantes + numeros
print(cantantes)
# Otra forma de unir listas
cantantes = cantantes + ["Natos y Waor", "Los Chikos del Maíz"]
print(cantantes)
# Otra forma de unir listas
cantantes += ["Natos y Waor", "Los Chikos del Maíz"]
print(cantantes)
# Otra forma de unir listas
cantantes.extend(["Natos y Waor", "Los Chikos del Maíz"])
print(cantantes)

