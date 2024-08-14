import os, shutil

# Crear directorio
if not os.path.isdir('./mi_carpeta'):
    os.mkdir('./mi_carpeta')
else:
    print("El directorio ya existe")
    
# Eliminar directorio
#os.rmdir('./mi_carpeta')

# Copiar directorio
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_copiada"

shutil.copytree(ruta_original, ruta_nueva)
os.rmdir('./mi_carpeta_copiada')

print("Directorio copiado correctamente")

# Listar directorio
print("Contenido de mi carpeta:")
contenido = os.listdir('./mi_carpeta')
print(contenido)

for elemento in contenido:
    print("Fichero: " + elemento)