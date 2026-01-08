

class Persona:
    def __init__(self, nombre, edad, apellido="Perez"):
        self.__nombre = nombre   # atributo privado
        self.__edad = edad       # atributo privado
        self.__apellido = apellido  # atributo privado

    def saludar(self):         # método público
        print(f"Hola, soy {self.__nombre} {self.__apellido} y tengo {self.__edad} años")


#p = Persona("Ana", 25)
#print(p._Persona__nombre)   # Acceso permitido pero no recomendado
#p.saludar()       # Acceso permitido


class Ejemplo:
    def __init__(self, publica, protegido, privado):
        self.publica = publica               # atributo público
        self._protegido = protegido         # atributo protegido
        self.__privado = privado            # atributo privado
    
    def mostrar_atributos(self):
        print(f"Público: {self.publica}")
        print(f"Protegido: {self._protegido}")
        print(f"Privado: {self.__privado}")

clase_ejemplo = Ejemplo("valor público", "valor protegido", "valor privado")

print(clase_ejemplo.publica)                 # Acceso permitido
print(clase_ejemplo._protegido)              # Acceso permitido pero no recomendado
print(clase_ejemplo._Ejemplo__privado)       # Acceso no permitido
