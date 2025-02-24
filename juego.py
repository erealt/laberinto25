class ElementoMapa:
    """Clase base para elementos del mapa."""
    def __init__(self):
        pass
    def entrar(self):
        pass

class Decorator(ElementoMapa):
    def __init__(self,em):
        super().__init__()
        self.em = em
        pass
class Bomba(Decorator):
    def __init__(self,em):
        super().__init__(em)
        self.activa = False
    
    def entrar(self):
        if self.activa:
            print("Has chocado con una bomba")
        else:
            self.em.entrar()
class Bicho:
    def __init__(self, vidas, poder, modo, posicion):
        self.vidas = vidas
        self.poder = poder
        self.modo = modo
        self.posicion = posicion

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder = 1
        self.vidas = 5

class Modo:
    def __init__(self):
        pass

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

class Perezoso(Modo):
    def __init__(self):
        super().__init__()



class Habitacion(ElementoMapa):
    def __init__(self, num):
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def entrar(self):
        print(f"Estás en una habitación{self.num}")

    def __repr__(self):
        return f"Habitacion({self.num})"

class Laberinto(ElementoMapa):
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def eliminar_habitacion(self, habitacion):
        self.habitaciones.remove(habitacion)

    def obtener_habitacion(self, num):
        for habitacion in self.habitaciones:
            if habitacion.num == num:
                return habitacion

        return None

    def entrar(self):
        print("Estás en un laberinto")
    

    def __repr__(self):
        return f"Laberinto({self.habitaciones})"

class Pared(ElementoMapa):
    """Representa una pared en el laberinto."""
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("Te has chocado con una pared")

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        print("Te has chocado con una Pared Bomba")
    

class Puerta:
    def __init__(self, lado1, lado2):
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def entrar(self):
        if self.abierta:
            print("La puerta está abierta")
        else:
            print("La puerta está cerrada")

    def __repr__(self):
        return f"Puerta(abierta={self.abierta}, lado1={self.lado1}, lado2={self.lado2})"

class Juego:
    def __init__(self, laberinto):
        self.laberinto = laberinto

    def __repr__(self):
        return f"Juego(laberinto={self.laberinto})"
        
    def crearLaberinto2Habitaciones(self):
        laberinto = Laberinto()
        hab1 = Habitación(1)
        hab1.este = Pared()
        hab1.oeste = Pared()
        hab1.norte = Pared()

        hab2 = Habitación(2)
        hab2.sur = Pared()
        hab2.este = Pared()
        hab2.oeste = Pared()

        puerta = Puerta(hab1, hab2)
        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.sur = puerta
        hab2.norte = puerta

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto

    def crearLaberinto2HabitacionesFM(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        hab2 = creator.fabricarHabitacion(2)
        puerta = creator.fabricarPuerta(hab1, hab2)
        hab1.sur = puerta
        hab2.norte = puerta

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto
    
    def crearLaberinto2HabitacionesFMD(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        hab2 = creator.fabricarHabitacion(2)

        pared1 = creator.fabricarPared()
        bomba1 = creator.fabricarBomba(pared1)
        hab1.este = bomba1

        pared2 = creator.fabricarPared()
        bomba2 = creator.fabricarBomba(pared2)
        hab2.oeste = bomba2

        puerta = creator.fabricarPuerta(hab1, hab2)
        hab1.sur = puerta
        hab2.norte = puerta

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto
    
    def crearLaberinto4H4BFMD(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        hab2 = creator.fabricarHabitacion(2)
        hab3 = creator.fabricarHabitacion(3)
        hab4 = creator.fabricarHabitacion(4)

        puerta1 = creator.fabricarPuerta(hab1, hab2)
        hab1.sur = puerta1
        hab2.norte = puerta1

        puerta2 = creator.fabricarPuerta(hab1, hab3)
        hab1.este = puerta2
        hab3.oeste = puerta2

        puerta3 = creator.fabricarPuerta(hab2, hab4)
        hab2.este = puerta3
        hab4.oeste = puerta3

        puerta4 = creator.fabricarPuerta(hab3, hab4)
        hab3.sur = puerta4
        hab4.norte = puerta4

        bicho1 = creator.fabricarBichoAgresivo()
        bicho2 = creator.fabricarBichoAgresivo()
        bicho3 = creator.fabricarBichoPerezoso()
        bicho4 = creator.fabricarBichoPerezoso()

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        laberinto.agregar_habitacion(hab3)
        laberinto.agregar_habitacion(hab4)
        self.agregar_bicho(bicho1)
        self.agregar_bicho(bicho2)
        self.agregar_bicho(bicho3)
        self.agregar_bicho(bicho4)

        bicho1.posicion = hab1
        bicho2.posicion = hab3
        bicho3.posicion = hab2
        bicho4.posicion = hab4
        return laberinto
    
    def obtenerHabitacion(self, num):
        return self.laberinto.obtener_habitacion(num)
    
    def crearLaberinto1H1BB(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        bichoBoss = creator.fabricarBoss()
        laberinto.agregar_habitacion(hab1)
        self.agregar_bicho(bichoBoss)
        bichoBoss.posicion = hab1
        return laberinto


