from modo import Modo
from agresivo import Agresivo
from ente import Ente

class Bicho(Ente):
    def __init__(self):
        #super().__init__(vidas, poder, posicion)
        self.modo = None
        self.running = True
        self.poder = None
        self.vidas = None
        self.posicion = None

    def actua(self):
        while self.estaVivo():
            self.modo.actuar(self)

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.poder = 1
        self.vidas = 5
        
    def iniCaotico(self):
        self.poder = 1
        self.vidas = 5
    def iniBueno(self):
        self.poder=0
        self.vidas = 1
        
    def atacar(self):
        self.juego.buscarPersonaje(self)
    def caminar(self):
        self.posicion.caminarAleatorio(self)

    def estaVivo(self):
        return self.vidas > 0
   
    def atacarATodos(self): 
     # Ataca al personaje si está en la misma habitación
        if self.posicion.personaje and self.posicion.personaje.esta_vivo():
            self.posicion.personaje.esAtacadoPor(self)
        # Ataca a todos los bichos en la misma habitación (menos a sí mismo)
        for bicho in self.posicion.bichos:
         if bicho is not self and bicho.esta_vivo():
             bicho.esAtacadoPor(self)
    def esAtacadoPor(self, bicho):
        self.vidas -= bicho.poder
        if self.vidas <= 0:
            print(f"{self} ha sido derrotado por {bicho}")
        else:
            print(f"{self} ha sido atacado por {bicho}, le quedan {self.vidas} vidas")  


    def __str__(self):
        return "Soy un bicho"