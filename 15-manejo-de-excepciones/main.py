# Capturar excepciones y manejar errores de código
# susceptible a fallos/errores

try:
    nombre = input("¿Cuál es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)

except: 
    print("Ha ocurrido un error, introduce bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteración")
    
# Multiples excepciones
try:
    numero = int(input("Dime un número para elevarlo al cuadrado: "))
    print(f"El cuadrado del número es: {numero*numero}")
except TypeError:
    print("Debes convertir tus cadenas a enteros en el código")
#except ValueError:
#    print("Introduce un número correcto")
except Exception as e:
    print(type(e))
    print(f"Ha ocurrido un error: {type(e).__name__}")

# Excepciones personalizadas o lanzar excepciones
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("¿Cuál es tu edad?: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Ha ocurrido un error: ", e)
finally:
    print("Fin de la iteración")