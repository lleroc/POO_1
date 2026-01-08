while True:  #
    print("Este ciclo se ejecuta para siempre.")
    respuesta = input("¿Quieres salir del ciclo? (s/n): ") 
    #todos los valores ingresados por teclado son cadenas de texto

    if respuesta.upper() == 'S':
        break

    
print("Has salido del ciclo.")