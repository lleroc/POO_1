from Empleado import Empleado

class EmpleadoTiempoParcial(Empleado):
    """
    Clase EmpleadoTiempoParcial que hereda de Empleado.
    Representa a un empleado que trabaja a tiempo parcial.
    Empleado de tiempo parcial trabaja por horas
    y su salario se calcula en función de las horas trabajadas
    """
    def __init__(sefl,nombre:str, cedula:str, horas_trabajadas:int, tarifa_por_hora:float):
        super().__init__(nombre, cedula)
        if horas_trabajadas < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas.")
        if tarifa_por_hora < 0:
            raise ValueError("La tarifa por hora no puede ser negativa.")
        sefl.horas_trabajadas = horas_trabajadas #atributo horas trabajadas
        sefl.tarifa_por_hora = tarifa_por_hora   #atributo tarifa por hora
    def calcular_salario(self):
        """
        Método para calcular el salario del empleado a tiempo parcial.
        Salario = horas_trabajadas * tarifa_por_hora
        """
        return self.horas_trabajadas * self.tarifa_por_hora
    
  