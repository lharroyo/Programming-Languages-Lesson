"""
GRUPO D - Ejercicio 1

Instrucciones:
  a) El código no produce error de sintaxis pero el resultado es incorrecto.
     Identifique el error lógico e indique en qué línea se encuentra.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 3)  # <- revisar esta línea


for i in range(6):
    print(f"fibonacci({i}) = {fibonacci(i)}")
