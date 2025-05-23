import unittest
from director import Director

class LaberintoBuilderTest(unittest.TestCase):
    def setUp(self):
        self.director = Director()
        self.director.procesar("laberintos/lab4HabIzd4Bichos.json")
        self.juego = self.director.obtenerJuego()
        self.juego.agregar_personaje("Pepe",5)

    def test_iniciales(self):
        self.assertIsNotNone(self.juego)
        self.assertIsNotNone(self.juego.laberinto)

    def test_personaje(self):
        person = self.juego.personaje
        self.assertIsNotNone(person)
        hab = self.juego.obtenerHabitacion(1)
        self.assertEqual(hab, person.posicion)
        self.assertEqual(5, person.vidas)

    def test_bicho_ataca(self):
        hab1 = self.juego.obtenerHabitacion(1)
        bicho = self.juego.bichos[0]
        person = self.juego.personaje
        hab1.entrar(bicho)
        hab1.entrar(person)
        self.assertEqual(bicho.posicion, person.posicion)
        vidas = person.vidas
        bicho.atacar()
        self.assertEqual(vidas, person.vidas + bicho.poder)

if __name__ == '__main__':
    unittest.main()