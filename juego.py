class ElementoMapa:
    """Clase base para elementos del mapa."""
    pass

class Habitacion(ElementoMapa):
    def __init__(self, num):
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def __repr__(self):
        return f"Habitacion({self.num})"

class Laberinto(ElementoMapa):
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def __repr__(self):
        return f"Laberinto({self.habitaciones})"

class Pared(ElementoMapa):
    """Representa una pared en el laberinto."""
    pass

class Puerta:
    def __init__(self, lado1, lado2):
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def __repr__(self):
        return f"Puerta(abierta={self.abierta}, lado1={self.lado1}, lado2={self.lado2})"

class Juego:
    def __init__(self, laberinto):
        self.laberinto = laberinto

    def __repr__(self):
        return f"Juego(laberinto={self.laberinto})"

# Ejemplo de uso
habitacion1 = Habitacion(1)
habitacion2 = Habitacion(2)
puerta = Puerta(habitacion1, habitacion2)

laberinto = Laberinto()
laberinto.agregar_habitacion(habitacion1)
laberinto.agregar_habitacion(habitacion2)

juego = Juego(laberinto)

print(juego)
