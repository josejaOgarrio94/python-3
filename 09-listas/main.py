""" 
LISTAS(arrays)
Son colecciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un índice numérico.
Se inicia desde el índice 0.
"""

pelicula = "Batman"

# Definir una lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))
years = list(range(2020,2050))
variada = ["Javier", 30, 4.4, True, "Texto"]


print(pelicula)
print(peliculas)
print(cantantes)
print(years)

# Indices
# Acceder a un elemento de la lista
print(peliculas[1]) # Spiderman
print(peliculas[-2]) # Spiderman
print(cantantes[1:3]) # Drake, Jennifer Lopez
print(cantantes[0:1]) # 2pac, si quisiéramos los dos primeros, sería [0:2]
print(cantantes[1:]) # Drake, Jennifer Lopez. 

# Sustitur un valor de la lista
peliculas[1] = "Aquaman"
print(peliculas)

# Añadir elementos a una lista
cantantes.append("Calle 13") # Añade al final de la lista
print(cantantes)
cantantes.insert(1, "David Bisbal") # Añade en la posición que le indiquemos
print(cantantes)

# Recorrer lista
print("\n**********LISTADO DE PELÍCULAS**********")

while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva película: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)
        

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
    
# Listas multidimensionales. Listas dentro de listas
print("\n**********LISTADO DE CONTACTOS**********")
contactos = [
    [
        'Antonio',
        'antonio@gmail.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]
print(contactos[1][1]) # Mostrar el email de Luis

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")