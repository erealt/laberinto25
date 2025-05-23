import time
from modo import Modo

class Caotico(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Cazador: Durmiendo 3 segundos...")
        time.sleep(3)

    def actua(self, bicho):
        print("Cazador: Atacando a todos en la habitación...")
        bicho.atacarATodos()
    
    def __str__(self):
        return "Soy cazador"