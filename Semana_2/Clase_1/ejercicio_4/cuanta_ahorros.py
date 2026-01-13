from cuenta_bancaria import clase_cuenta_bancaria
class clase_cuenta_ahorros(clase_cuenta_bancaria):
    def __init__(self, titular, saldo, interes):
        super().__init__(titular, saldo)
        self.interes = interes
    
    def mostrar_interes(self):
        print(f"El interés de la cuenta de {self.titular} es: {self.interes}%") 