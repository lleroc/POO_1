from alumnos import alumnos as clase_alumnos
from cursos import cursos as clase_cursos

class programas(clase_alumnos, clase_cursos):
    def __init__(self, cantidad_alumnos:int, nombre_curso:str, duracion :int):
        clase_alumnos.__init__(self, cantidad_alumnos)
        clase_cursos.__init__(self, nombre_curso)
        self.duracion = duracion

    def info(self, detalle:bool=False)->str:
        if not detalle:
            print(f"{self.nombre_curso}")
        
        return (f"Programa: {self.nombre_curso},\n" 
        f"Cantidad de alumnos: {self.cantidad_alumnos}, \n"
        f"Duración: {self.duracion} meses")