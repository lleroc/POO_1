#Crea un programa para gestionar empleados:
#Define una clase base Empleado con:
    #Atributos: nombre y salario_base
    #Método calcular_salario() que devuelva el salario base sin cambios.
#Define una clase derivada EmpleadoConBono que herede de Empleado y:
    #Sobrescriba (override) el método calcular_salario() para que devuelva el salario base más un bono.
    #Debe permitir calcular el salario de dos maneras:
        #Sin parámetros: usa un bono fijo almacenado en el objeto.
        #Con un porcentaje opcional: si se pasa un porcentaje, 
        # el bono será salario_base * porcentaje.
#Crea ejemplos de uso con al menos dos empleados y muestra los salarios calculados.

from EmpleadoConBono import EmpleadoConBono
from Empleado import Empleado

bono = EmpleadoConBono("Ana", 3000, 500)

normal = Empleado("Luis", 2500)

print(bono.nombre, bono.calcular_salario())  # Salario con bono fijo

print(normal.nombre, normal.calcular_salario())  # Salario base sin bono