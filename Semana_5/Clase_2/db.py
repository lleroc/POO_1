import mysql.connector
from mysql.connector import Error
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from config.config import DB_CONFIG

def obtener_conexion():
    try:
        con = mysql.connector.connect(**DB_CONFIG)
        return con
    except Error as e:
        return RuntimeError("Error al conectarse a la base de datos")

