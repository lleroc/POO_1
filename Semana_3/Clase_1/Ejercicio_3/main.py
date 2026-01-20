#Ejercicio 1: Sistema de Empleados
#Crea un sistema de empleados con las siguientes clases:

#Empleado (clase base)
#EmpleadoTiempoCompleto (hereda de Empleado)
#EmpleadoTiempoParcial (hereda de Empleado)
#Gerente (hereda de EmpleadoTiempoCompleto)
#Implementa constructores adecuados, métodos para 
# calcular salarios y métodos para mostrar información.

from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto
from EmpleadoTiempoParcial import EmpleadoTiempoParcial
from Gerente import Gerente

def main():
    # Crear instancias de cada tipo de empleado
    empleado_tc = EmpleadoTiempoCompleto("Juan Perez", "123456789", 3000.00)
    empleado_tp = EmpleadoTiempoParcial("Ana Gomez", "987654321", 20.00, 80)  # $20 por hora, 80 horas trabajadas
    gerente = Gerente("Carlos Lopez", "112233445", 5000.00, 1000.00)  # Salario mensual + bono mensual

    # Mostrar información y salarios
    print(empleado_tc.mostrar_informacion())
    print(empleado_tp.mostrar_informacion())
    print(gerente.mostrar_informacion())

if __name__ == "__main__":
    main()
