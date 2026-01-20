from Empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):
    """
    Empleado con salario fijo mensual.
    """
    def __init__(self, nombre: str, cedula: str, salario_mensual: float):
        super().__init__(nombre, cedula)
        self.salario_mensual = salario_mensual  # Atributo salario mensual

    def calcular_salario(self) -> float:
        """
        Calcula el salario mensual del empleado a tiempo completo.
        """
        return self.salario_mensual