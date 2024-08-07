"""
SET (Conjuntos)
Es un tipo de dato, para tener una colección de valores, pero no 
tiene ni indice ni orden
"""

personas = {
    "Víctor",
    "Manolo",
    "Francisco"
}

# Funciones más usadas
personas.remove("Manolo")
personas.add("Manolo")

print(personas)
print(type(personas))
