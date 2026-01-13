class clase_vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def descripcion(self):
        return f"Vehículo de la marca: {self.marca}"