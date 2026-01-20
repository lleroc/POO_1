from Persona import Persona 
class Empleado(Persona):
    def __init__(self,nombre, edad, cedula, salario):
        super().__init__(nombre, edad, cedula)
        self.salario = salario
    
    def mostrar_datos(self):
        print("Nombre es: ",self.nombre)
        print("Edad es: ",self._edad) #protegido (permitido solo con herencia)
        print("Salario es: ",self.salario) 
        #no hacer esta linea
        #print("Cedula es: ",self.__cedula) #privado (no permitido)
        ####################################

        print("Cedula es: ",self.mostrar_cedula()) #privado (no permitido)