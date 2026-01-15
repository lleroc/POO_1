class clase_empleado:
    def __init__(self, max_empleados):
        self.max_empleados = max_empleados
        self.empleados = []
    
    def agregar_empleado(self, nombre, apellido, salario):
        if len(self.empleados) < self.max_empleados:
            empleado = {
                'nombre': nombre,
                'apellido': apellido,
                'salario': salario
            }
            self.empleados.append(empleado)
        else:
            print("No se pueden agregar más empleados, se ha alcanzado el máximo.")
    def obtener_empleados(self):
        return self.empleados
    
    def total_emplados(self):
        return len(self.empleados)
    
    def salario_total(self):
        return sum(empleado['salario'] for empleado in self.empleados)