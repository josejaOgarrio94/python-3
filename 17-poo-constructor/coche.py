class Coche:
    
    # Atributos o propiedades (variables)
    # Características del coche
    color = "Amarillo"
    marca = "Lamborguini"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    soy_publico = "Hola, soy un atributo público"
    __soy_privado = "Hola, soy un atributo privado"
    
    # Constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
    
    # Métodos, son acciones que hace el objeto (coche) (funciones)
    def getPrivado(self):
        return self.__soy_privado
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    def getVelocidad(self):
        return self.velocidad
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getInfo(self):
        info = "----- Información del coche -----"
        info += "\nColor: " + self.getColor()
        info += "\nMarca: " + self.marca
        info += "\nModelo: " + self.getModelo()
        info += "\nVelocidad: " + str(self.getVelocidad())
        return info