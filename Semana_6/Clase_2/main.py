from config.config import DB_CONFIG
from database.connection import DatabaseConnection
from models.proveedor_model import ProveedorModel
from controllers.proveedor_controller import ProveedorController
from views.proveedor_view import ProveedoresView

def main():
    db = DatabaseConnection(DB_CONFIG)
    model = ProveedorModel(db)
    controller = ProveedorController(model)
    app = ProveedoresView(controller)
    app.mainloop()

if __name__ == "__main__":
    main()