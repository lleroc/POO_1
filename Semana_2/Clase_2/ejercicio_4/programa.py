from Empleado import clase_empleado
from proeycto import proyectos

class programa(clase_empleado, proyectos):
    def __init__(self, max_empleados, nombre, cliente, presupuesto, costo_por_empleado):
        clase_empleado.__init__(self, max_empleados)
        proyectos.__init__(self, nombre, cliente, presupuesto)
        self.costo_por_empleado = costo_por_empleado
    
    def resumen(self, modo:str = "general"):
        if modo == "general":
            return {
                'nombre_proyecto': self.nombre,
                'cliente': self.cliente,
                'presupuesto': self.presupuesto,
                'total_empleados': self.total_emplados(),
                'salario_total': self.salario_total(),
                'costo_por_empleado': self.costo_por_empleado
            }
        elif modo == "detallado":
            return {
                'nombre_proyecto': self.nombre,
                'cliente': self.cliente,
                'presupuesto': self.presupuesto,
                'empleados': self.obtener_empleados(),
                'salario_total': self.salario_total(),
                'costo_por_empleado': self.costo_por_empleado
            }
        else:
            return "Modo no reconocido. Use 'general' o 'detallado'."