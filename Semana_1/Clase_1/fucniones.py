def suma(a, b):  #el tipo de datos de a y b no está definido (numeros)
    return a + b

def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division por cero"

print("Bienvenido a la calculadora")
n1 = float(input("Ingrese el primer numero: ")) #por defecto input toma todo como string
n2 = float(input("Ingrese el segundo numero: "))
while True:
    print("Si desea salir ingrese 'salir'")
    operacion = input("Ingrese la operacion (+, -, *, /): ")
    if operacion == "+":
        print("El valor de la suma es: " + str(suma(n1, n2)))
    elif operacion == "-":
        print("El valor de la resta es: " + str(resta(n1, n2)))
    elif operacion == "*":
        print("El valor de la multiplicacion es: " + str(multiplicacion(n1, n2)))
    elif operacion == "/":
        print("El valor de la division es: " + str(division(n1, n2)))
    elif operacion.lower() == "salir":
        print("Saliendo de la calculadora")
        break
    else:
        print("Operacion no valida")    
