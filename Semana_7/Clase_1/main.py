from config.conexion import Conexion
from models.producto_model import producto_model
from controllers.producto_controller import producto_controller
from views.productos_view import producto_view

def main():
    try:
        db = Conexion()
        model = producto_model(db)
        controller = producto_controller(model)
        vista = producto_view(controller)
        vista.mainloop()
    except Exception as e:
         # Si falla antes de que Tkinter pueda mostrar messagebox
        try:
            print(f"Error fatal en la aplicación: {e}")
        except Exception:
            pass

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        try:
            print(f"Error fatal ejecutando main: {e}")
        except Exception:
            pass