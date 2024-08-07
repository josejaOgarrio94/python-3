"""
Variables locales y globales

Las variables locales son aquellas que se definen dentro de una función y solo pueden ser utilizadas dentro de la misma.
Las variables globales son aquellas que se declaran fuera de una función y están disponibles dentro y fuera de las funciones.
"""

# Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    # Variable local
    frase = "Hola mundo!!"
    print("Dentro de la función:")
    print(frase)
    
    year = 2021
    print(year)
    
    # Definir variable global
    global website
    website = "victorroblesweb.es"

holaMundo()
# Se podría utilizar la variable global website
# después de invocar la función holaMundo()
print(website)