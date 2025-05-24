from ente import Ente

class Personaje(Ente):
    def __init__(self, juego,nombre, vidas=5):
        super().__init__()
        self.nombre = nombre
        self.vidas = vidas
        self.juego=juego

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

    def curar(self, cantidad=1):
        self.vidas += cantidad
        print(f"{self.nombre} se cura. Vidas: {self.vidas}")

    def atacar(self, bicho):
        modo = getattr(self, "modo", "normal")
        if modo == "mago":
        # El mago elimina al bicho directamente
            if hasattr(self, "posicion") and self.posicion and bicho in self.posicion.bichos:
                self.posicion.bichos.remove(bicho)
                print(f"{self.nombre} (mago) ha eliminado a {bicho}")
        else:
        # El personaje normal le quita 2 de vida al bicho
            if hasattr(bicho, "vidas"):
                bicho.vidas -= 2
                print(f"{self.nombre} ha atacado a {bicho}. Vidas restantes del bicho: {bicho.vidas}")
                if bicho.vidas <= 0 and hasattr(self, "posicion") and self.posicion and bicho in self.posicion.bichos:
                    self.posicion.bichos.remove(bicho)
                    print(f"{self.nombre} ha eliminado a {bicho}")

    def __str__(self):
        return f"Personaje {self.nombre}"