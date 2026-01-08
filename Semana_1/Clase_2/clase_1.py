class Persona:
    def saludar(self):
        print("Hola, ¿cómo estás?")
    def despedirse(self):
        print("Adiós, ¡hasta luego!")
    def agradecer(self):
        print("Gracias por tu ayuda.")
    def felicitar(self):                      #funcion => se llama metodo
        print("¡Felicidades por tu logro!")

class operaciones_matematicas:
    def sumar(self, a, b):
        return a + b
    def restar(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero."


#atributos => caracteristicas
class Jordi_Villacis:
    def __init__(self,lentes,color_cabello,auriculares, color_piel, altura):
        pass

class bicicleta:
    def __init__(self,numero_ruedas, tipo, color, marca, velocidad_maxima):
        self.numero_ruedas = numero_ruedas
        self.tipo = tipo
        self.color = color
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima


class automovil:
    def __init__(self, placa:str, marca:str, anio:int = 2026):   #contructor
        self.placa = placa
        self.marca = marca
        self.anio = anio

    def acelerar(self, velocidad:int):
        print(f"El automóvil {self.marca} está acelerando a {velocidad} km/h.")
    
    def frenar(self):
        print(f"El automóvil {self.marca} está frenando.")

    def __str__(self):  #metodo especial para representar el objeto como cadena
        return f"Automóvil {self.marca} con placa {self.placa} del año {self.anio}"
    
    # destructor
    def __del__(self):
        print(f"El automóvil {self.marca} con placa {self.placa} ha sido eliminado.")

#string => str

#llamar a la clase
#mi_auto = automovil("ABC123", "Toyota", 2022)

#mi_auto.acelerar(100)


class xxx:
    def __init__(self):
        pass

    def metodo1(): #no solicita parametros y tampoco retorna nada
        print("Este es el metodo 1")

    def metodo2(self, parametro1): #solicita un parametro y no retorna nada
        print(f"Este es el metodo 2 con el parametro: {parametro1}")

    def metodo3(self)->str: #no solicita parametros pero retorna un valor
        return "Este es el metodo 3 que retorna un valor"
    
    def metodo4(self, parametro1)->int: #solicita un parametro y retorna un valor
        return len(parametro1)

Objeto = xxx()

#Objeto.metodo1()
#Objeto.metodo2("Hola")
#Objeto.metodo3()

valor_devuelto = Objeto.metodo4("Hola")
print(f"El metodo4 retorno el valor: {valor_devuelto}")
# 0 1 2 3 
# H O L A