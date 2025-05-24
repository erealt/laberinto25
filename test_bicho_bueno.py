# test_bicho_bueno.py

from personaje import Personaje
from bueno import Bueno

class TestBichoBueno:
    def __init__(self):
        self.bichos = []

# Test
def test_bicho_bueno_cura():
    # Crear personaje y bicho bueno
    personaje = Personaje(None, "Pepe", 5)
    bicho_bueno = Bueno()
    habitacion = TestBichoBueno()
    habitacion.bichos.append(bicho_bueno)
    personaje.posicion = habitacion

    # Quitarle vidas al personaje
    personaje.vidas = 4
    # El bicho bueno ayuda
    bicho_bueno.ayudar(personaje)

    assert personaje.vidas == 7, f"Esperado 5 vidas, pero tiene {personaje.vidas}"
    print("Test OK: El bicho bueno cura al personaje correctamente.")

if __name__ == "__main__":
    test_bicho_bueno_cura()