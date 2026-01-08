

class Persona:
    def __init__(self, nombre, edad, apellido = "Llerena"):
        self._nombre = nombre   # atributo protegido
        self._edad = edad       # atributo protegido
        self._apellido = apellido  # atributo protegido

    def saludar(self):         # método público
        print(f"Hola, soy {self._nombre} y tengo {self._edad} años")


p = Persona("Ana", 25)
p.saludar()       # Acceso permitido
print(p._nombre)   # Acceso permitido pero no recomendado


