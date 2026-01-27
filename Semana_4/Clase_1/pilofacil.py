class Perro:
    def hacer_sonido(self):
        return "Guau"
class Gato:
    def hacer_sonido(self):
        return "Miau"
class Vaca:
    def hacer_sonido(self):
        return "Muu"

def emitir_sonido(animal):
    print(animal.hacer_sonido())

perro = Perro()
gato = Gato()
vaca = Vaca()

emitir_sonido(perro)  # Output: Guau
emitir_sonido(gato)   # Output: Miau
emitir_sonido(vaca)   # Output: Muu