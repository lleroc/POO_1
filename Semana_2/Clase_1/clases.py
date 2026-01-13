class Animal:
    def hacer_sonido(self):
        print("Sonido genérico de animal")

class Perro(Animal):
    def hacer_sonido(self):  #override
        super().hacer_sonido()
        print("Guau Guau")

#a = Animal()
p = Perro()

p.hacer_sonido()  # Salida: Guau Guau