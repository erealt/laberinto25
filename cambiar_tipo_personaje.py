from comando import Comando
# cambiar_tipo_personaje.py
class CambiarTipoPersonaje(Comando):
    def __init__(self, receptor, nuevo_tipo):
        super().__init__(receptor)
        self.nuevo_tipo = nuevo_tipo

    def ejecutar(self):
        self.receptor.cambiarTipo(self.nuevo_tipo)