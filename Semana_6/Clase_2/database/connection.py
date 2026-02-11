# database/connection.py
import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, db_config: dict):
        self.db_config = db_config

    def obtener_conexion(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            return conn
        except Error as e:
            raise RuntimeError(f"Error de conexión a MySQL: {e}")
