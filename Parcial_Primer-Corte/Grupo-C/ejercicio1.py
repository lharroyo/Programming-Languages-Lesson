"""
GRUPO C - Ejercicio 1

Instrucciones:
  a) Identifique el error lógico. ¿Para qué valor(es) falla la función y qué retorna?
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

def clasificar_temperatura(temp):
    if temp < 0:
        return "Congelante"
    elif temp < 15:
        return "Frío"
    elif temp < 25:
        return "Templado"
    elif temp > 25:
        return "Caliente"


print(clasificar_temperatura(25))  # Imprime None
