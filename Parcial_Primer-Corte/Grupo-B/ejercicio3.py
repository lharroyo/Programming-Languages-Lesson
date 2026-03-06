"""
GRUPO B - Ejercicio 3

Instrucciones:
  a) Identifique el error en la llamada a filter y explique cómo corregirlo.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

palabras = ["python", "java", "javascript", "kotlin", "ruby", "go"]

resultado = sorted(
    map(str.upper, filter(len(w) > 4, palabras))
)

print(resultado)
