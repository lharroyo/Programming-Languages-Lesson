"""
GRUPO B - Ejercicio 2

Instrucciones:
  a) Identifique el error y explique qué efecto tiene al ejecutar cuenta.retirar(200).
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto: float):
        self.saldo += monto
        print(f"Depósito exitoso. Saldo: {self.saldo}")

    def retirar(monto: float):      # <- revisar esta línea
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo: {self.saldo}")
        else:
            print("Saldo insuficiente")


cuenta = CuentaBancaria("Pedro", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
