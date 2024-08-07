# Description: Tipos de datos en Python

# None expresa la nada, es un tipo de dato que se utiliza para definir una variable sin valor
nada = None
cadena = "Hola soy Victor Robles"
entero = 99
flotante = 4.2
booleano = True
# la lista no es más que una colección de datos. Se pueden guardar cualquier tipo de dato
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta", 30, "cuarenta"]
# la tupla es una lista de datos que no se puede modificar
tupla = ("master", "en", "python")
# el diccionario es un tipo de dato que almacena un conjunto de datos. Es como un JSON o un array asociativo con clave-valor.
diccionario = {
    "nombre": "Victor",
    "apellidos": "Robles",
    "curso": "Master en Python"
}
# el rango es un tipo de dato que se utiliza para generar una secuencia de números
rango = range(9)
congelado = frozenset({"manzana", "pera", "naranja"})
# el byte es un tipo de dato que se utiliza para almacenar datos binarios
dato_byte = b"Probando"


# mostrar variable
print(dato_byte)
# mostrar tipo de dato
print(type(dato_byte))

print("-------------------------------------------------")

texto = "Hola soy un texto"
numerito = str(776)

print(texto + " " + numerito)

