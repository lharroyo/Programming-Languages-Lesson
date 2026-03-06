"""
GRUPO B - Ejercicio 1

Instrucciones:
  a) Identifique el error, en qué línea ocurre y qué tipo de excepción genera.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

estudiantes = ["Ana", "Luis", "María", "Carlos"]
aprobados = []

for i in range(len(estudiantes) + 1):
    aprobados.append(estudiantes[i])

print(aprobados)
