from contenedor import Contenedor
from bicho import Bicho
from personaje import Personaje

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.bichos = []
        self.personaje=[]
        self.monedad=[]

    def entrar(self, alguien):
        print(f"Entrando en la habitación {self.num}")
        if isinstance(alguien, Bicho):
            self.bichos.append(alguien)
        elif isinstance(alguien, Personaje):
            self.personajes.append(alguien)
        
        alguien.posicion=self

    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)
    def calcularPosicion(self):
        self.forma.calcularPosicion()
    def __str__(self):
        return "Soy una habitacion"