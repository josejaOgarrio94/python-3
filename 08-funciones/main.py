"""
Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto 
que pueden reutilizarse invocando a la función tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # Bloque / conjunto de instrucciones
    
nombreDeMiFuncion(mi_parametro)
"""

# Ejemplo 1
print("\n##### Ejemplo 1 #####")
def muestraNombre():
    print("Victor")
    print("Juan")
    print("Pepe")
    print("Francisco")
    print("\n")

# Invocar función
muestraNombre()

# Ejemplo 2
print("\n##### Ejemplo 2 #####")
def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    print("\n")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)

# Ejemplo 3
print("\n##### Ejemplo 3 #####")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")
    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")
    print("\n")
    
tabla(3)
tabla(7)

# Ejemplo 3.1
print("\n##### Ejemplo 3.1 #####")
for numero_tabla in range(1, 11):
    tabla(numero_tabla)

# Ejemplo 4
print("\n##### Ejemplo 4 #####")
# Parametros opcionales
def getEmpleado(nombre, dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")
    print("\n")

getEmpleado("Victor", "123456789")
getEmpleado("Juan")

# Ejemplo 5: return o devolver datos
print("\n##### Ejemplo 5 #####")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("Victor"))

# Ejemplo 6
print("\n##### Ejemplo 6 #####")

def calculadora(numero1, numero2, basicas = False):
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2
    
    cadena = ""
    
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else: 
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)
        cadena += "\n"
        
    return cadena

print(calculadora(56,5))

# Ejemplo 7
print("\n##### Ejemplo 7 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Javier", "Gomez"))

# Ejemplo 8
print("\n##### Ejemplo 8 #####")

dime_el_year = lambda year: f"El año es {year * 2}"

print(dime_el_year(2020))

