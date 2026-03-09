"""
GRUPO D - Ejercicio 4

Instrucciones:
  a) Identifique el error, en qué línea ocurre y qué tipo de excepción genera.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

def contar_palabras(texto):
    conteo = {}
    for palabra in texto.split():
        conteo[palabra] = conteo[palabra] + 1    # <- revisar esta línea
    return conteo


frase = "el gato y el perro y el pez"
resultado = contar_palabras(frase)
print(resultado)
