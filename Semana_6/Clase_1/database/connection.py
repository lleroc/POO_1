import mysql.connector

class database_connection:
    def __init__(self, config: dict):
        self.config = config

    def obtener_conexion(self):
        return mysql.connector.connect(**self.config)
