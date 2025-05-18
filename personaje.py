from ente import Ente

class Personaje(Ente):
    def __init__(self, nombre, vidas=10):
        super().__init__()
        self.nombre = nombre
        self.vidas = vidas

    def esta_vivo(self):
        return self.vidas > 0

    def esAtacadoPor(self, atacante):
        self.vidas -= atacante.poder
        print(f"{self.nombre} ha sido atacado por {atacante}. Vidas restantes: {self.vidas}")
        if self.vidas <= 0:
            print(f"{self.nombre} ha muerto.")
    
    def cambiarTipo(self, nuevo_tipo):
     self.tipo = nuevo_tipo
     print(f"{self.nombre} ahora es de tipo {self.tipo}")

    def __str__(self):
        return f"Personaje {self.nombre}"