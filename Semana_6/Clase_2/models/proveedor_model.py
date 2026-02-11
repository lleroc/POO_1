from mysql.connector import Error

class ProveedorModel:
    def __init__(self, db):
        self.db = db
        self._crear_tabla_si_no_existe()

    def _crear_tabla_si_no_existe(self):
        sql = """
        CREATE TABLE IF NOT EXISTS proveedores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(120) NOT NULL,
            ruc VARCHAR(20) NOT NULL UNIQUE,
            telefono VARCHAR(30),
            email VARCHAR(120),
            direccion VARCHAR(200),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB;
        """
        conn = self.db.obtener_conexion()
        try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        finally:
            conn.close()

    def listar(self):
        conn = self.db.obtener_conexion()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM proveedores ORDER BY id DESC;")
            return cur.fetchall()
        finally:
            conn.close()

    def crear(self, nombre, ruc, telefono, email, direccion):
        conn = self.db.obtener_conexion()
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO proveedores (nombre, ruc, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s);",
                (nombre, ruc, telefono, email, direccion),
            )
            conn.commit()
        except Error as e:
            # ejemplo típico: ruc duplicado
            raise RuntimeError(f"No se pudo crear proveedor: {e}")
        finally:
            conn.close()

    def actualizar(self, proveedor_id, nombre, ruc, telefono, email, direccion):
        conn = self.db.obtener_conexion()
        try:
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE proveedores
                SET nombre=%s, ruc=%s, telefono=%s, email=%s, direccion=%s
                WHERE id=%s;
                """,
                (nombre, ruc, telefono, email, direccion, proveedor_id),
            )
            conn.commit()
        except Error as e:
            raise RuntimeError(f"No se pudo actualizar proveedor: {e}")
        finally:
            conn.close()

    def eliminar(self, proveedor_id):
        conn = self.db.obtener_conexion()
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM proveedores WHERE id=%s;", (proveedor_id,))
            conn.commit()
        finally:
            conn.close()