from db import obtener_conexion
import mysql.connector
from mysql.connector import Error

class PaisModel:
    @staticmethod
    def todos():
        con = obtener_conexion()
        try:
            paises = con.cursor()
            paises.execute("SELECT * FROM `paises`")
            return paises.fetchall() # id nombre
        except Error as e:
            raise RuntimeError("Error al obtener los paises")
        finally:
            paises.close()
            con.close()
    @staticmethod
    def uno(pais_id:int):
        con = obtener_conexion()
        try:
            paises = con.cursor()
            paises.execute("SELECT * FROM `paises` where id=%s",(pais_id))
            return paises.fetchall() # id nombre  o None
        except Error as e:
            raise RuntimeError("Error al obtener los paises")
        finally:
            paises.close()
            con.close()
    @staticmethod
    def insertar(nombre:str)-> int:
        con = obtener_conexion()
        try:
            cadena = con.cursor()
            cadena.execute("INSERT INTO `paises`(`nombre`) VALUES (%s)",(nombre))
            return cadena.lastrowid
        except Error as e:
            raise RuntimeError("Ocurrio un error al guardar el pais")
        finally:
            cadena.close()
            con.close()
    @staticmethod
    def actualizar(pais_id:int, nombre:str)-> bool:
        con = obtener_conexion()
        try:
            cadena = con.cursor()
            cadena.execute("UPDATE `paises` SET `nombre`=%s WHERE `id`=%s",(nombre, pais_id))
            return cadena.rowcount > 0
        except Error as e:
            raise RuntimeError("No se pudo actualizar el pais")
        finally:
            cadena.close()
            con.close()
    @staticmethod
    def eliminar(pais_id:int)-> bool:
        con = obtener_conexion()
        try:
            cadena = con.cursor()
            cadena.execute("DELETE FROM `paises` WHERE `id`=%s",( pais_id))
            return cadena.rowcount > 0
        except Error as e:
            raise RuntimeError("No se pudo eliminar el pais")
        finally:
            cadena.close()
            con.close()
    

