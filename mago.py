import time
from tipo_personaje import TipoPersonaje

class Mago(TipoPersonaje):
    def esAtacadoPor(self, personaje, atacante):
        if not getattr(personaje, "invisible", False):
            print(f"{personaje.nombre} es atacado por {atacante} y se vuelve invisible 2 segundos.")
            personaje.invisible = True
            time.sleep(2)
            personaje.invisible = False
            print(f"{personaje.nombre} vuelve a ser visible.")
        else:
            print(f"{personaje.nombre} es invisible y no recibe daño.")

    def __str__(self):
        return "Mago"