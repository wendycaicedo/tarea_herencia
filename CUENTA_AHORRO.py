# WENDY TATIANA CAICEDO CAICEDO
class cuenta_ahorro:
    def __init__(self, interes, credito, debito, mostrar, pagar_interes,):
        cuenta_ahorro.contador_cuenta_ahorro += 1
        self._interes = interes
        self._credito = credito
        self._debito = debito
        self._mostrar = mostrar
        self._pagar_interes = pagar_interes

    def __float__(self)-> float:
        return f' cuenta_ahorro [interes: {self._interes}, credito: {self._credito}, debito: {self._debito}, mostrar: {self._mostrar}, pagar_interes: {self._pagar_interes}]'

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, interes):
        self._interes = interes

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
    def pagar_interes(self):
        return self._pagar_interes

    @pagar_interes.setter
    def pagar_interes(self, pagar_interes):
        self._pagar_interes = pagar_interes

cuenta_ahorro= input("Ingrese el numero de cuenta: ")
propietario= input(str(" ingrese el nombre del propietario: "))
cuenta= int(input(" Ingrese el saldo anterior: "))
deposito= int(input(" Ingrese el monto a depositar: "))
suma= cuenta+deposito
print(" El saldo de su cuenta es: ", suma)