#empleado
    #nombre
    #salario

#empleadostiempocompleto
    #bono
#clases protegidas
class Empleado:
    def __init__(self, nombre:str, salario:float):
        self._nombre = nombre
        self._salario = salario
    
    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre}, Salario: {self._salario}")
    
    def calcular_salario_anual(self) -> float:
        return self._salario * 12

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre:str, salario:float, bono:float):
        super().__init__(nombre, salario)
        self._bono = bono

    def mostrar_informacion(self):
        return super().mostrar_informacion()

    def calcular_salario_anual(self) -> float:
        salario_anual = super().calcular_salario_anual()
        print( salario_anual + self._bono)

emp1 = EmpleadoTiempoCompleto("Luis Llerena",3000,5000)
emp1.mostrar_informacion()
emp1.calcular_salario_anual()
