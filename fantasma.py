from tipo_personaje import TipoPersonaje

class Fantasma(TipoPersonaje):
    def esAtacadoPor(self, personaje, atacante):
        print(f"{personaje.nombre} está en modo fantasma y no recibe daño.")

    def __str__(self):
        return "Fantasma"