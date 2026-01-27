from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class EmpleadoFijo(Empleado):
    def __init__(self, salario_mensual:float):
        self.salario_mensual = salario_mensual

    def calcular_salario(self) -> float:
        return self.salario_mensual

class EmpleadoPorHora(Empleado):
    def __init__(self, hora:int, tarifa:float):
        self.hora = hora
        self.tarifa = tarifa
        
    def calcular_salario(self) -> float:
        return self.hora * self.tarifa

def imprimir_salario(listaEmpleados: list[Empleado]):
    total = 0
    for empleado in listaEmpleados:
        total += empleado.calcular_salario()
        print(f'Salario del empleado: {empleado.calcular_salario()}')
    
    print(f'Salario total de la empresa: {total}')

listaEmpleados = [EmpleadoFijo(1500), 
                  EmpleadoPorHora(120, 15), 
                  EmpleadoFijo(2000), 
                  EmpleadoPorHora(100, 20)]
imprimir_salario(listaEmpleados)