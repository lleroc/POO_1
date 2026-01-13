class clase_cuenta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def mostrar_saldo(self):
        print(f"El saldo de {self.titular} es: {self.saldo}")