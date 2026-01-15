#Una institución educativa desea manejar la información de sus programas académicos.
#Crea una clase Alumnos con:
    #Atributo: cantidad_alumnos
    #Método info() que muestre la cantidad de alumnos.

#Crea una clase Curso con:
    #Atributo: nombre_curso
    #Método info() que muestre el nombre del curso

#Crea una clase Programa que herede de Alumnos y Curso y:
#Sobrescriba el método info() para mostrar toda la información del programa.
#Permita mostrar solo la información básica o información detallada.
#Crea dos objetos de la clase Programa y muestra su información.

from programas import programas
print("Bienvenido al sistema de gestión de programas académicos")
while True:
    print("Menu Principal")
    print("1. Crear Programa Académico")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre_curso = input("Ingrese el nombre del curso: ")
        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
        duracion = int(input("Ingrese la duración del programa (en meses): "))
        programa = programas(cantidad_alumnos, nombre_curso, duracion)
        
        detalle = input("¿Desea ver la información detallada? (s/n): ").lower() == 's'
        print(programa.info(detalle))
        
    elif opcion == "2":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")