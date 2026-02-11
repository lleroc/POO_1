from mysql.connector import Error

class usuario_model:
    def __init__(self, db):
        self.db = db


    def login_con_erorr(self,  usuario:str, contrasenia:str):
        cadena = f"SELECT * FROM `usuarios` WHERE `usuario`='{usuario}' and `contrasenia`='{contrasenia}'"
        try:
            conn = self.db.obtener_conexion()
            abrir_con = conn.cursor(dictionary = True)
            abrir_con.execute(cadena)
            ok = abrir_con.fetchone()
            conn.close()
            abrir_con.close()
            return ok
        except Error as e:
            return e



    

    

