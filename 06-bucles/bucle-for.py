"""

# FOR
# for variable in elemento iterable (lista, rango, etc):	
#		bloque de instrucciones

"""

contador = 0
resultado = 0
for contador in range(0, 10):
    print("Voy por el " + str(contador))
    resultado = resultado + contador

print(f"El resultado es: {resultado}")


# Ejemplo tabla de multiplicar
print("\n########## EJEMPLO 1 ##########")

numero_usuario = int(input("¿De qué número quieres la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del número {numero_usuario} ###")

for numero_tabla in range(1, 11):
    if numero_usuario == 45:
        print("No se pueden mostrar números prohibidos!!")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada")