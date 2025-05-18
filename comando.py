class Comando:
    def __init__(self, receptor):
        self.receptor = receptor

    def ejecutar(self, *args, **kwargs):
        raise NotImplementedError("Debes implementar este método en la subclase")