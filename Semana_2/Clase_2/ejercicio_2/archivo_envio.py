class clase_envio:
    def __init__(self, peso: float):
        self.peso = peso

    def calcular_costo(self):
        return self.peso * 5