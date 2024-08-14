from io import open
import pathlib
import shutil

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + '/archivo.txt'
archivo = open(ruta, 'a+')

# Escribir archivo
archivo.write('***** Soy un texto metido desde Python *****\n')

# Cerrar archivo
archivo.close()


# Abrir archivo
ruta = str(pathlib.Path().absolute()) + '/archivo.txt'
archivo_lectura = open(ruta, 'r')

# Leer contenido
#contenido = archivo_lectura.read()
# for elemento in contenido:
#     print(elemento)
#print(contenido)

# Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for elemento in lista:
    lista_frase = elemento.split()
    print(lista_frase)
    #print(" - " + elemento.upper())

# Copiar archivo
shutil.copyfile(ruta, str(pathlib.Path().absolute()) + '/archivo_copiado.txt')

# Mover archivo
shutil.move(ruta, str(pathlib.Path().absolute()) + '/archivo_movido.txt')

# Eliminar archivo
import os
os.remove(str(pathlib.Path().absolute()) + '/archivo_copiado.txt')
# Comprobar si existe el directorio
# si ponemos os.path.abspath("./") nos devuelve la ruta absoluta del directorio actual
print(os.path.abspath("./"))
if os.path.isfile(os.path.abspath("./") + '/archivo_movido.txt'):
    print("El archivo existe")
else:
    print("El archivo no existe")