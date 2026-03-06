"""
GRUPO A - Ejercicio 3

Instrucciones:
  a) El código no produce un error de sintaxis pero el resultado es incorrecto.
     ¿Cuál es el problema lógico?
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

from functools import reduce

ventas = [300, 150, 420, 80, 560, 200]

ventas_filtradas = filter(lambda x: x > 200, ventas)
total = reduce(lambda acc, x: acc + x, ventas)

print(f"Total ventas mayores a 200: {total}")
