from Estudiantes import Estudiante

class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = [] #ARREGLO DE TIPO ESTUDIANTE

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        return "Se agragó el estudiante al curso."
    
    def mostrar_estudiantes(self):
        print(f"Estudiantes en el curso {self.nombre_curso}:")
        for estudiante in self.estudiantes:
            estudiante.obtener_informacion()

    

    