from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "Seat", "Panda", 200, 300, 4)
carro2 = Coche("Azul", "Citroen", "Xsara", 180, 250, 4)
carro3 = Coche("Rojo", "Mercedes", "Clase A", 220, 350, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado
carro3 = "Aleatorio"
if type(carro3) == Coche:
    print("Es un objeto correcto!")
else:
    print("No es un objeto!")

# Visibilidad
print(carro.soy_publico)
# print(carro.__soy_privado)
print(carro.getPrivado())
