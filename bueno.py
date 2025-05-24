import time
from modo import Modo
class Bueno(Modo):
    def __init__(self):
        super().__init__()
        

    def ayudar(self, personaje):
        personaje.curar(3)
        print(f"{personaje.nombre} ha sido curado por un bicho bueno (+3 vidas)")