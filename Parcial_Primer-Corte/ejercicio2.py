"""
GRUPO D - Ejercicio 2

Instrucciones:
  a) Identifique el error y explique por qué el decorador usado es incorrecto.
     ¿Qué excepción se genera al ejecutar r.area()?
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    @staticmethod
    def area(self):                  # <- revisar esta línea
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


r = Rectangulo(4, 5)
print(f"Área: {r.area()}")
print(f"Perímetro: {r.perimetro()}")
