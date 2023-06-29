# WENDY TATIANA CAICEDO CAICEDO
class cuenta:
    def __init__(self,numero, nombrepropietario, saldo,):
        cuenta.contador_cuenta+= 1
        self._numero=numero
        self._nombrepropietario= nombrepropietario
        self._saldo= saldo

    def _str_(self):
        return f'cuenta [numero: {self._numero}, nombrepropietario:{self._nombrepropietario}, saldo:{self._saldo}]'
    @property
    def numero (self):
        return self._numero
    @numero.setter
    def numero(self,numero):
        self ._numero = numero

    @property
    def nombrepropietario(self):
        return self._nombrepropietario

    @nombrepropietario.setter
    def nombrepropietario(self, nombrepropietario):
        self._nombrepropietario = nombrepropietario

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

numero= input("Indique el numero de cuenta: ")
nombrepropietario=input(str("ingrese el nombre del propietario: "))
cuenta=int(input("Ingrese el saldo anterior: " ))
monto=int(input("Ingrese el monto a depositar: "))
SM= cuenta+monto
print(" el saldo de su cuenta es: ", SM)


