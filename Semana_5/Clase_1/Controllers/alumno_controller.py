from ..Models.alumno_model import Alumno

class AlumnoController:
    def __init__(self):
        self.lista_alumnos:list[Alumno] = []
    
    def crear(self, alumno:Alumno)->str:
        try:
            self.lista_alumnos.append(alumno)
            return "Se guardo con exito"
        except Exception as ex:
            return ex
    
    def editar(self, cedula:str, alumno_parametro:Alumno)->str:
        try: 
            alumno_editar:Alumno = None
            for al in self.lista_alumnos:
                if al.__cedula == cedula:
                    alumno_editar = al
                    break
            if alumno_parametro.__cedula:
                alumno_editar.__cedula = alumno_parametro.__cedula

            if alumno_parametro.__nombre:
                alumno_editar.__nombre = alumno_parametro.__nombre

            if alumno_parametro.__apellido:
                alumno_editar.__apellido = alumno_parametro.__apellido

            if alumno_parametro.__nivel:
                alumno_editar.__nivel = alumno_parametro.__nivel

            if alumno_parametro.__paralelo:
                alumno_editar.__paralelo = alumno_parametro.__paralelo

            if alumno_parametro.__edad:
                alumno_editar.__edad = alumno_parametro.__edad
        except Exception as ex:
            return f"Ocurrio un error al guardar. {ex}"
    
    def todos(self):
        return self.lista_alumnos

    def uno_apellido(self, apellido:str)-> Alumno:
        for alu in self.lista_alumnos:
            if alu.__apellido == apellido:
                return alu
        return None

    def uno_cedula(self, cedula:str)-> Alumno:
        return next((alu for alu in self.lista_alumnos if alu.__cedula == cedula), None)

    def eliminar(self, cedula:str)-> str:
        alumno:Alumno = self.uno_cedula(cedula)
        if alumno is None:
            return "No se Encontro al alumno"
        self.lista_alumnos.remove(alumno)
        return "Se elimno con exito"

        
            
                
        
        
