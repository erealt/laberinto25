from oro import Oro
from plata import Plata
from super_moneda import SuperMoneda
class FactoriaMonedas:
    def __init__(self):
        self._monedas = {}

    def getMoneda(self, key):
        if key not in self._monedas:
            if key == "oro":
                self._monedas[key] = Oro()
            elif key == "plata":
                self._monedas[key] = Plata()
            elif key == "super":
                self._monedas[key] = SuperMoneda()
            else:
                raise ValueError(f"Tipo de moneda desconocido: {key}")
        return self._monedas[key]