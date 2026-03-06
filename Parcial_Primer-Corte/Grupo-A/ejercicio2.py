"""
GRUPO A - Ejercicio 2

Instrucciones:
  a) Identifique y explique el error en el código. Indique en qué línea se encuentra.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

class Vehiculo:
    def __init__(self, marca: str, velocidad_max: int):
        self.marca = marca
        self.velocidad_max = velocidad_max

    def describir(self):
        print(f"Vehículo: {self.marca}, Vel. máx: {self.velocidad_max} km/h")


class Carro(Vehiculo):
    def __init__(self, marca: str, velocidad_max: int, num_puertas: int):
        super().__init__(marca)   # <- revisar esta línea
        self.num_puertas = num_puertas


mi_carro = Carro("Toyota", 180, 4)
mi_carro.describir()
