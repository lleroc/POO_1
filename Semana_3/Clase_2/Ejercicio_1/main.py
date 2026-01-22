#Ejercicio 2: Biblioteca
#Diseña un sistema para una biblioteca con:

#Publicacion (clase base)
#Libro (hereda de Publicacion)
#Revista (hereda de Publicacion)
#LibroDigital (hereda de Libro)

#crud de un libro
#C. => create.  insert
#R. => read.    select
#U. => update.  update
#D. => delete.  delete

from Publicacion import Publicacion

objeto_publicacion = Publicacion()
print("--- Sistema de Gestión de Biblioteca ---")
while True:
    print("Menu General")
    print("1. Agregar Publicación")
    print("2. Listar Publicaciones")
    print("3. Editar Publicación")
    print("4. Eliminar Publicación")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    match opcion:   #switch
        case 1:
            titulo = input("Ingrese el título de la publicación: ")
            autor = input("Ingrese el autor de la publicación: ")
            anio = input("Ingrese el año de la publicación: ")
            pub = Publicacion(titulo, autor, anio)
            objeto_publicacion.agregar_publicacion(pub)
            print("Publicación agregada exitosamente.")
        case 2:
            objeto_publicacion.listar_publicaciones()
        case 3:
            objeto_publicacion.lista_horizontal()
            indice = int(input("Ingrese el índice de la publicación a editar: ")) - 1
            nuevo_titulo = input("Ingrese el nuevo título (deje en blanco para no cambiar): ")
            nuevo_autor = input("Ingrese el nuevo autor (deje en blanco para no cambiar): ")
            nuevo_anio = input("Ingrese el nuevo año de publicación (deje en blanco para no cambiar): ")
            objeto_publicacion.editar_publicacion(indice,nuevo_titulo, nuevo_autor, nuevo_anio)
        case 4:
            objeto_publicacion.lista_horizontal()
            indice = int(input("Ingrese el índice de la publicación a eliminar: ")) - 1
            objeto_publicacion.eliminar_publicacion(indice)
        case 5:
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción no válida. Por favor, intente de nuevo.")
            print("-"*50)