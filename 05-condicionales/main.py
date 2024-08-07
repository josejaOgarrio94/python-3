# Operadores de comparación
# == Igual
# != Diferente
# < Menor que
# > Mayor que
# <= Menor o igual que
# >= Mayor o igual que

# Operadores lógicos
# and Y
# or O
# ! Negación
# not NO



# Ejemplo de condicionales en Python

print("########## EJEMPLO 1 ##########")

color = "rojo"
# color = input("Adivina el color: ")
if color == "rojo":
    print("Enhorabuena!!")
    print("El color es rojo")
else:
    print("Ohhh!!")
    print("El color no es rojo")
    
# Ejemplo 2 
print("\n########## EJEMPLO 2 ##########")

#year = 2020

year = int(input("En que año estamos?: "))
if year >= 2020:
    print("Estamos de 2020 en adelante!!")
else:
    print("Es un año anterior a 2020!!")


# Ejemplo 3
print("\n########## EJEMPLO 3 ##########")

nombre = "David"
ciudad = "Barcelona"
continente = "Europa"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    
    if continente != "Europa":
        print("El usuario no es Europeo")
    else:
        print(f"Es Europeo y de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")
    
# Ejemplo 4
print("\n########## EJEMPLO 4 ##########")

dia = input("Introduce el día de la semana: ")

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")
    
# Ejemplo 5
print("\n########## EJEMPLO 5 ##########")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")

# Ejemplo 6
print("\n########## EJEMPLO 6 ##########")

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")
    
# Ejemplo 7
print("\n########## EJEMPLO 7 ##########")

pais = "España"
if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es un país de habla hispana")
else:
    print(f"{pais} es un país de habla hispana")
    
# Ejemplo 8
print("\n########## EJEMPLO 8 ##########")

pais = "Colombia"
if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un país de habla hispana")
else:
    print(f"{pais} es un país de habla hispana")