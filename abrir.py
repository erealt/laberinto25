from comando import Comando
class Abrir(Comando):
    def ejecutar(self):
        self.receptor.abrir()