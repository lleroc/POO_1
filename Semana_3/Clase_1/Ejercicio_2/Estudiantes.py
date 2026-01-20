class Estudiante:
    def __init__(self, nombre, apellido, calificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.calificacion = calificacion
    
    def obtener_informacion(self):
        print(f"Nombre: {self.nombre} {self.apellido}, Calificación: {self.calificacion}")