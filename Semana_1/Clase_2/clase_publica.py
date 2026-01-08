#calse_publica

class Persona:
    def __init__(self, nombre, edad, apellido):
        self.nombre = nombre   # atributo público
        self.edad = edad       # atributo público
        self.apellido = apellido  # atributo privado

    def saludar(self):         # método público
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")


p = Persona("Ana", 25)
print(p.nombre)   # Acceso permitido
p.saludar()       # Acceso permitido


