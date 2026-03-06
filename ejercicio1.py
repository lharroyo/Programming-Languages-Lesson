"""
GRUPO A - Ejercicio 1

Instrucciones:
  a) Identifique y explique el error en el código. Indique en qué línea se encuentra.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

def calcular_factorial(n):
    resultado = 1
    for i in range(1, n):
        resultado *= i
    return resultado

print(calcular_factorial(5))  # Imprime 24 en lugar de 120
