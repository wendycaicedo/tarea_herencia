# WENDY TATIANA CAICEDO CAICEDO
class cuentacorriente:
    def __init__(self, credito, debito, mostrar, pagar_cheque,):
        cuentacorriente.contador_cuenta_ahorro +=1
        self._credito=credito
        self._debito = debito
        self._mostrar = mostrar
        self._pagar_cheque = pagar_cheque
    def __bool__(self)-> bool:
        return f' cuentacorriente [credito: {self._credito}, debito: {self._debito}, mostrar: {self._mostrar}, pagar_cheque: {self._pagar_cheque}]'
    @property
    def credito(self):
        return self._credito
    @credito.setter
    def credito(self,credito):
        self._credito=credito

    @property
    def credito(self):
        return self._credito

    @credito.setter
    def credito(self, credito):
        self._credito = credito

    @property
    def debito(self):
        return self._debito

    @debito.setter
    def debito(self, debito):
        self._debito = debito

    @property
    def mostrar(self):
        return self._mostrar

    @mostrar.setter
    def mostrar(self, mostrar):
        self._mostrar = mostrar

    @property
    def pagar_cheque(self):
        return self._pagar_cheque

    @pagar_cheque.setter
    def pagar_cheque(self, pagar_cheque):
        self._pagar_cheque = pagar_cheque

cuentacorriente= input("ingrese el numero de cuenta: ")
propietario=input(str("ingrese el nombre del propietario: "))
cuenta=int(input("Ingrese el saldo anterior: "))
retiro=int(input("Ingrese el monto a retirar: " ))
RST= cuenta-retiro
print("el saldo de su cuenta es: ", RST)



