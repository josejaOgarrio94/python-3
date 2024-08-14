# Programación orientada a objetos (POO o OOP)

# Definir una clase (molde para crear más objetos de ese tipo
# (Coche) con características similares)

class Coche:
    
    # Atributos o propiedades (variables)
    # Características del coche
    color = "Amarillo"
    marca = "Lamborguini"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    # Métodos, son acciones que hace el objeto (coche) (funciones)
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
# Fin definición clase

# Crear objetos / Instanciar la clase
coche = Coche()
print(coche.marca, coche.getColor())
print("Velocidad actual:", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("Velocidad nueva:", coche.getVelocidad())

# Crear más objetos
coche2 = Coche()
print(coche2.getVelocidad())