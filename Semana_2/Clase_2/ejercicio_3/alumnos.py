class alumnos:
    def __init__(self, cantidad_alumnos:int):
        self.cantidad_alumnos = cantidad_alumnos

    def info(self)->str:
        print(f"Cantidad de alumnos: {self.cantidad_alumnos}")