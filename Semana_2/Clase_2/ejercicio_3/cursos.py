class cursos:
    def __init__(self, nombre_curso:str):
        self.nombre_curso = nombre_curso

    def info(self)->str:
        print(f"Nombre del curso: {self.nombre_curso}")