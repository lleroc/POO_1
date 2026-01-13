from archivo_vehiculo import clase_vehiculo

class clase_auto(clase_vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def descripcion(self):
        return f"{super().descripcion()} con {self.puertas} puertas"

