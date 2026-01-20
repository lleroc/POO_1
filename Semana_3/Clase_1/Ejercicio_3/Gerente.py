from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto

class Gerente(EmpleadoTiempoCompleto):
    def __init__(self, nombre, cedula, salario_mensual, bono_mensual):
        super().__init__(nombre, cedula, salario_mensual)
        self.bono_mensual = bono_mensual  # Atributo bono mensual

    def calcular_salario(self) -> float:
        """
        Calcula el salario mensual del gerente, incluyendo el bono.
        """
        salario_base = super().calcular_salario()
        return salario_base + self.bono_mensual
    
    def mostrar_informacion(self) -> str:
        """
        Muestra la información del gerente.
        """
        info_base = super().mostrar_informacion()
        return (f"Nombre: {self.nombre},\n"
                 f" Cédula: {self.cedula},\n"
                 f" Tipo: {self.__class__.__name__},\n" 
                 f" Bono Mensual: {self.bono_mensual:.2f}",
                 f" Salario Total: {self.calcular_salario():.2f}")