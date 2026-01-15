class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        #en esta clase solo devuelve el salario base
        #no tiene comisiones ni bonos
        #no se debe incrementar el salario base
        return self.salario_base