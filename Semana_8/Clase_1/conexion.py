import mysql.connector

def obtener_connexion():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="clientes_python",
        autocommit=True
    )