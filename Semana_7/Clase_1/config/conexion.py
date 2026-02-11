import mysql.connector
from mysql.connector import Error
from config.config import obtener_db_config

class Conexion:
    def __init__(self):
        try:
            self.config = obtener_db_config()
        except Exception as e:
            raise RuntimeError(f"Error inializando la base de datos: {e}")
    
    def conectar(self):
        try:
            conn = mysql.connector.connect(**self.config)
        except Error as errorMySql:
            raise RuntimeError(f"Error al conectar con la base de datos: {errorMySql}")
        except Exception as e:
            raise RuntimeError(f"Ocurrio in error inesperado con mysql: {e}")
        