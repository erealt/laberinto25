from comando import Comando
class Entrar(Comando):
    def ejecutar(self, alguien):
        self.receptor.entrar(alguien)