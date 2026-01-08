#calculadora con funciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

print("Bienvenidos a super Calculadora en Python")
while True:
    print("Menu de Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = (input("Seleccione una opción (1/2/3/4): "))
    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        res = sumar(num1, num2)
        print(f"La suma es: {res}")
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        res = restar(num1, num2)
        print(f"La resta es: {res}")
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        res = multiplicar(num1, num2)
        print(f"La multiplicación es: {res}")
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        res = dividir(num1, num2)
        print(f"La división es: {res}")
    elif opcion == "5":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opción no válida")