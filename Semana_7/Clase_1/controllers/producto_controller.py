from models.producto_model import producto_model

class producto_controller:
    def __init__(self, model:producto_model):
        try:
            self.model = model
        except Exception as e:
            raise RuntimeError(f"Ocurrio un error al inicializar el controllador: {e}")
    
    def todos(self):
        try:
            return self.model.todos()
        except Exception as e:
            raise RuntimeError(f" Ocurrio un error en el todos del controlador: {e}")
    
    def insertar(self, nombre, precio, stock):
        try:
            return self.model.insertar(nombre,precio,stock)
        except Exception as e:
            raise RuntimeError(f" Ocurrio un error en el insertar del controlador: {e}")
    
    def actualziar(self,id, nombre, precio, stock):
        try:
            return self.model.actualizar(id,nombre,precio,stock)
        except Exception as e:
            raise RuntimeError(f" Ocurrio un error en el insertar del controlador: {e}")
    
    def elimianr(self,id):
        try:
            return self.model.eliminar(id)
        except Exception as e:
            raise RuntimeError(f" Ocurrio un error en el insertar del controlador: {e}")
             