"""
# Bucle while
Estructura de control de flujo que repite un bloque de instrucciones
mientras una condición sea verdadera.

while condición:
    bloque de instrucciones
    actualización de contador
"""

contador = 1
while contador <= 100:
    print(f"Estoy en el número: {contador}")
    contador += 1

print("-------------------------")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1
    
print(muestrame)

print("####### EJEMPLO ########")
numero_usuario = int(input("De qué número quieres la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1
    
print(f"### Tabla de multiplicar del número {numero_usuario} ###")

contador = 1
while contador <= 10:
    if numero_usuario == 45:
        print("No se pueden mostrar números prohibidos!!")
        break
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1
else:
    print("Tabla finalizada")