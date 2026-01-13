#String nombre = "Ana";
#nombre:str = "Juan"

class Persona:  #clase padre
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")


class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")


est1 = Estudiante("Ana", "Ingeniería")

est1.saludar()
est1.estudiar()