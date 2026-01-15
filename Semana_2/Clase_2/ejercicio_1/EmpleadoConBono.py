from Empleado import Empleado

class EmpleadoConBono(Empleado):
    def __init__(self, nombre, salario_base, bono_fijo):
        super().__init__(nombre, salario_base)
        self.bono_fijo = bono_fijo
    

    #sobreescritura del metodo calcular_salario
    def calcular_salario(self, porcentaje: float | None = None) -> float:
        #version 1
        if porcentaje is None:
            return self.salario_base + self.bono_fijo
        
        #controles de errores
        if porcentaje < 0:
            raise ValueError("El porcentaje no puede ser negativo")
        
        bono = self.salario_base * porcentaje
        return self.salario_base + bono

        

        
        
