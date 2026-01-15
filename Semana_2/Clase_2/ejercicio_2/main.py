#Una empresa de transporte necesita calcular el costo de envíos.
#Crea una clase base Envio con:
    #Atributos: peso (kg)
    #Método calcular_costo() que calcule el costo básico del envío:
        #Costo = peso * 5

#Crea una clase derivada EnvioExpress que herede de Envio y:
    #Sobrescriba el método calcular_costo()

#Permita calcular el costo de dos formas:
    #Sin parámetros: agrega un recargo fijo de 20.
    #Con parámetro distancia: agrega un recargo adicional de distancia * 2.
#Muestra el costo de un envío normal y dos cálculos distintos de un envío expres


from archivo_envio import clase_envio
from archivo_EnvioExpress import EnvioExpress
while True:
    print("Sistema de Encomiendas\n")
    print("Menu Principal")
    print("1. Envio Normal")
    print("2. Envio Express (sin distancia)")
    print("3. Envio Express (con distancia)")
    opcion = int(input("Seleccione una opción (1-3): "))
    peso = float(input("Ingrese el peso del paquete (kg): "))
    if opcion == 1:
        envio = clase_envio(peso) #solicito a la clase padre
        costo = envio.calcular_costo()
        print(f"Costo del Envio Normal: ${costo}\n")
    elif opcion == 2:
        envio_express = EnvioExpress(peso) #solicito a la clase hija
        costo = envio_express.calcular_costo()
        print(f"Costo del Envio Express (sin distancia): ${costo}\n")
    elif opcion == 3:
        distancia = float(input("Ingrese la distancia del envío (km): "))
        envio_express = EnvioExpress(peso) #solicito a la clase hija
        try:
            costo = envio_express.calcular_costo(distancia)
            print(f"Costo del Envio Express (con distancia): ${costo}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.\n")

