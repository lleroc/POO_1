from abc import ABC, abstractmethod

class Empleado(ABC):
    """
    Clase base abstracta Empleado.
    Clase base (plantilla) para todos los empleados.
    """
    def __init__(self,nombre:str, cedula:str):
        self.nombre = nombre #atributo nombre
        self.cedula = cedula #atributo cedula
    
    @abstractmethod
    def calcular_salario(self):
        """
        Metodo obligatorio.
        Método abstracto para calcular el salario del empleado.
        Debe ser implementado por las clases derivadas.
        """
        pass

    def mostrar_informacion(self):
        """
        Método para mostrar la información del empleado.
        """
        return (f"Nombre: {self.nombre},\n"
                 f" Cédula: {self.cedula},\n"
                 f" Tipo: {self.__class__.__name__},\n"
                 f" Salario: {self.calcular_salario():.2f}")
