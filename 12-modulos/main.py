"""
Módulos. Son funcionalidades ya hechas para reutilizar.
En Python hay muchos módulos, que los puedes consultar aquí:
https://docs.python.org/3/py-modindex.html

Podemos conseguir módulos que ya vienen en el lenguaje, módulos en internet y también podemos crear nuestros propios módulos.
"""

# Importar módulo propio
#import mimodulo
#from mimodulo import holaMundo
from mimodulo import *

# print(mimodulo.holaMundo("David"))
# print(mimodulo.calculadora(3, 5, True))

print(holaMundo("David"))

# Módulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada ", fecha_personalizada)

print(datetime.datetime.now().timestamp())

# Módulo matemáticas
import math

print("Raíz cuadrada de 10: ", math.sqrt(10))
print("Número Pi: ", float(math.pi))
print("Redondear: ", math.ceil(6.56789)) # Redondea hacia arriba
print("Redondear: ", math.floor(6.56789)) # Redondea hacia abajo

# Módulo random
import random

print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))