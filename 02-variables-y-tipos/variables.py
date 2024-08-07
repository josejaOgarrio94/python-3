"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto.
"""
# Crear y mostrar variables
texto = "Master en Python"

print(texto)

"""
Python es un lenguaje débilmente tipado, es decir, no es necesario
indicar de qué tipo es la variable, si no que el propio lenguaje interpreta
de qué tipo es la variable en función al contenido.
"""

texto2 = "con Victor Robles"
numero = 45
decimal = 6.7

print (texto2)
print(numero)
print(decimal) 

print("-------------------------------------------------")

# Sustituir el valor de una variable
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("-------------------------------------------------")

# Concatenación
nombre = "Victor"
apellidos = "Robles"
web = "victorroblesweb.es"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))
