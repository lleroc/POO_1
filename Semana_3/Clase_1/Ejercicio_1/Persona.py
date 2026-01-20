#herencia (public, protected, private)
class Persona:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre          # Atributo público
        self._edad = edad             # Atributo protegido
        self.__cedula = cedula        # Atributo privado
    
    def mostrar_cedula(self):
        return self.__cedula
