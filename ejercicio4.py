"""
GRUPO C - Ejercicio 4

Instrucciones:
  a) Identifique el error en la llamada a Deportista.__init__ y explique por qué falla.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, carrera: str):
        super().__init__(nombre, edad)
        self.carrera = carrera


class Deportista(Persona):
    def __init__(self, nombre: str, edad: int, deporte: str):
        super().__init__(nombre, edad)
        self.deporte = deporte


class EstudianteDeportista(Estudiante, Deportista):
    def __init__(self, nombre: str, edad: int, carrera: str, deporte: str):
        Estudiante.__init__(self, nombre, edad, carrera)
        Deportista.__init__(nombre, edad, deporte)   # <- revisar esta línea


ed = EstudianteDeportista("Carlos", 20, "Ingeniería", "Fútbol")
ed.presentarse()
