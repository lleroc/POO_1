class Alumno:
    def __init__(self, nombre:str, apellido:str, nivel:int, paralelo:str, edad:int, cedula:str):
        self.__nombre = nombre 
        self.__apellido = apellido 
        self.__nivel = nivel 
        self.__paralelo = paralelo
        self.__edad = edad
        self.__cedula = cedula
    
    def __str__(self):
        return {
            "Nombre" : self.__nombre,
            "Apellido":self.__apellido,
            "Nivel":self.__nivel,
            "Paralelo":self.__paralelo,
            "Edad":self.__edad,
            "Cedula":self.__cedula
        }
        

