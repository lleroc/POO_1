class ProveedorController:
    def __init__(self, model):
        self.model = model

    def listar(self):
        return self.model.listar()

    def crear(self, data: dict):
        self._validar(data)
        self.model.crear(
            data["nombre"],
            data["ruc"],
            data.get("telefono", ""),
            data.get("email", ""),
            data.get("direccion", "")
        )

    def actualizar(self, proveedor_id: int, data: dict):
        self._validar(data)
        self.model.actualizar(
            proveedor_id,
            data["nombre"],
            data["ruc"],
            data.get("telefono", ""),
            data.get("email", ""),
            data.get("direccion", "")
        )

    def eliminar(self, proveedor_id: int):
        self.model.eliminar(proveedor_id)

    def _validar(self, data: dict):
        nombre = (data.get("nombre") or "").strip()
        ruc = (data.get("ruc") or "").strip()

        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if not ruc:
            raise ValueError("El RUC es obligatorio.")
        if len(ruc) < 8:
            raise ValueError("El RUC parece inválido (muy corto).")