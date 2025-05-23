import unittest
from director import Director
from norte import Norte  # Importa tus orientaciones singleton
from sur import Sur
from este import Este
from oeste import Oeste
from estado_puerta import Cerrada
from estado_puerta import Abierta

class PuertasTest(unittest.TestCase):
    def setUp(self):
        self.director = Director()
        self.director.procesar("laberintos/lab4HabIzd4Bichos.json")
        self.juego = self.director.obtenerJuego()
        self.juego.agregar_personaje("Pepe", 5)

    def test_puerta_abre_cierra(self):
        hab = self.juego.obtenerHabitacion(1)
        # Usa el objeto Orientacion, no el string
        puerta = hab.obtenerElementoEnOrientacion(Sur())

        self.assertIsNotNone(puerta)
        self.assertTrue(hasattr(puerta, "abrir"))
        self.assertTrue(hasattr(puerta, "cerrar"))
        self.assertIsInstance(puerta.estadoPuerta, Cerrada)

        puerta.abrir()
        self.assertIsInstance(puerta.estadoPuerta, Abierta)

        puerta.cerrar()
        self.assertIsInstance(puerta.estadoPuerta, Cerrada)

        puerta.cerrar()
       

if __name__ == '__main__':
    unittest.main()