"""
GRUPO B - Ejercicio 4

Instrucciones:
  a) Identifique el error y explique por qué ocurre en Python específicamente.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

class Figura:
    def area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


figuras = [Circulo(5), Rectangulo(4, 6), Circulo(3)]

for figura in figuras:
    print(f"Área: {figura.Area()}")   # <- revisar esta línea
