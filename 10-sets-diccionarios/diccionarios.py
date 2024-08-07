"""
Diccionarios
Un diccionario es una colección de elementos que están indexados, no están ordenados y se pueden modificar. 
Son escritos entre llaves y tienen claves y valores.
"""

persona = {
    "nombre": "Víctor",
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}

print(persona)
print(type(persona))
print(persona["apellidos"])

# Lista con diccionarios
contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

print(contactos)
print(contactos[0]["nombre"])

# Cambiar uno de los elementos de uno de los diccionarios
contactos[0]["nombre"] = "Antoñito"
print(contactos[0]["nombre"]) # Antoñito

print("\n**********LISTADO DE CONTACTOS**********")
print("-----------------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-----------------------------------")
    print("\n")