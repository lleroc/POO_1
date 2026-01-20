#gestion de estudiantes

#Estudiantes.  1
#curso.  varios

from Cursos import Curso
from Estudiantes import Estudiante
def main():
    curso_python = Curso("Python Básico")
    curso_poo = Curso("Python Orientado a Objetos")
    curso_angular = Curso("Angular para Principiantes")

    while True:   
        print("Gestión de Estudiantes en Cursos")
        print("Menu de opciones:")
        print("1. Crear un Estudiante")
        print("2. Agregar Estudiante a un Curso")
        print("3. Mostrar Estudiantes en un Curso")
        print("4. Salir")
        opcion = int(input("Seleccione una opción (1-4): "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            calificacion = float(input("Ingrese la calificación del estudiante: "))
            estudiante = Estudiante(nombre, apellido, calificacion)
            print("Estudiante creado exitosamente.")
            print("*"*50)
        elif opcion == 2:
            print("Seleccione el curso para agregar el estudiante:")
            print("1. Python Básico")
            print("2. Python Orientado a Objetos")
            print("3. Angular para Principiantes")
            curso_opcion = int(input("Ingrese el número del curso (1-3): "))
            if curso_opcion == 1:
                mensaje = curso_python.agregar_estudiante(estudiante)
            elif curso_opcion == 2:
                mensaje = curso_poo.agregar_estudiante(estudiante)
            elif curso_opcion == 3:
                mensaje = curso_angular.agregar_estudiante(estudiante)
            else:
                mensaje = "Opción de curso inválida."
            print(mensaje)
            print("*"*50)

        elif opcion == 3:
            print("Seleccione el curso para mostrar los estudiantes:")
            print("1. Python Básico")
            print("2. Python Orientado a Objetos")
            print("3. Angular para Principiantes")
            curso_opcion = int(input("Ingrese el número del curso (1-3): "))
            if curso_opcion == 1:
                curso_python.mostrar_estudiantes()
            elif curso_opcion == 2:
                curso_poo.mostrar_estudiantes()
            elif curso_opcion == 3:
                curso_angular.mostrar_estudiantes()
            else:
                print("Opción de curso inválida.")
            print("*"*50)

        elif opcion == 4:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 4.")


if __name__ == "__main__":
    main()   









