"""
GRUPO C - Ejercicio 2

Instrucciones:
  a) Identifique el error. ¿Cómo se debería acceder correctamente al salario?
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
     ¿Qué principio de la POO se está violando?
"""

class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def aumentar_salario(self, porcentaje: float):
        self.__salario *= (1 + porcentaje)


emp = Empleado("Laura", 3000)
emp.aumentar_salario(0.10)
print(f"Salario: {emp.__salario}")   # <- revisar esta línea
