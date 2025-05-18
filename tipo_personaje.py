import time

class TipoPersonaje:
    def esAtacadoPor(self, personaje, atacante):
        personaje.vidas -= atacante.poder
        print(f"{personaje.nombre} ha sido atacado por {atacante}. Vidas restantes: {personaje.vidas}")
        if personaje.vidas <= 0:
            print(f"{personaje.nombre} ha muerto.")

    def __str__(self):
        return "Normal"

