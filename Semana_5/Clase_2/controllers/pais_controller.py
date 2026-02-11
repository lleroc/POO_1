from tkinter import Tk, messagebox
from models.pais_model import PaisModel

class PaisController:
    def __init__(self, vista):
        self.vista = vista
     
    def cargar_lista(self):
        try:
            paises = PaisModel.todos()
            self.vista.render_lista(paises)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def guardar(self):
        nombre = self.vista.nombre_var.get().strip()
        if not nombre:
            messagebox.showerror("Validacion:","El nombre es requerido")
            return
        if len(nombre) > 120:
            messagebox.showerror("Validacion:", "El nombre del pais excedio el limite de caracteres permitidos")
            return
        try:
            PaisModel.insertar(nombre)
            self.vista.limpiar_form()
            self.cargar_lista()
        except Exception as e:
            messagebox.showerror("Validacion:", "Ocurrio un error al guardar" )
    
    def uno(self, pais_id:int):
        try:
            pais = PaisModel.uno(pais_id)
            if not pais:
                messagebox.showerror("No se encontro al pais")
                return
            id, nombre = pais
            self.vista.nombre_var.set(str(nombre))
            self.vista.id_var.set(str(id))
        except Exception as e:
            messagebox.showerror("Ocurrio un error")
    
    def actualizar(self):
        id =  self.vista.id_var.get()
        nombre = self.vista.nombre_var.get().strip()
        try:
            ok = PaisModel.actualizar(id, nombre)
            if not ok:
                messagebox.showerror("Ocurrio un error al actualziar")
            self.vista.limpiar_form()
            self.cargar_lista()
        except Exception as e:
            messagebox.showerror("Ocurrio un error al actualziar")
        
    def eliminar(self):
        id = self.vista.id_var.get()
        try:
            ok = PaisModel.eliminar(id)
            if not ok:
                messagebox.showerror("Ocurrio un error al elimianr")
            self.vista.limpiar_form()
            self.cargar_lista()
        except Exception as e:
            messagebox.showerror("Ocurrio un error al actualziar")



