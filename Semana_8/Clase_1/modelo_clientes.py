from conexion import obtener_connexion

class ModeloClientes:
    def todos(self):
        conexion = obtener_connexion()
        cmd = conexion.cursor(dictionary=True)
        cmd.execute("select * from clientes")
        filas = cmd.fetchall()
        cmd.close()
        conexion.close()
        return filas
    
    def insertar(self, nombre, email, telefono):
        try:
            conexion = obtener_connexion()
            cmd = conexion.cursor(dictionary=True)
            cmd.execute("insert into clientes(nombre, email, telefono) values(%s,%s,%s)",
                        (nombre, email, telefono))
            cmd.close()
            conexion.close()
            return "ok"
        except Exception as e:
            return e
    
    def actualizar(self,cliente_id, nombre, email, telefono):
        try:
            conexion = obtener_connexion()
            cmd = conexion.cursor(dictionary=True)
            cmd.execute("update clientes set nombre=%s, email=%s, telefono=%s where cliente_id=%s",
                        (nombre, email, telefono, cliente_id))
            cmd.close()
            conexion.close()
            return "ok"
        except Exception as e:
            return e
    
    def eliminar(self, cliente_id):
        try:
            conexion = obtener_connexion()
            cmd = conexion.cursor(dictionary=True)
            cmd.execute("delete from cleintes where cliente_id=%s",
                        (cliente_id))
            cmd.close()
            conexion.close()
            return "ok"
        except Exception as e:
            return e