from typing import List, Optional, Tuple
from config.conexion import Conexion
from dataclasses import dataclass

@dataclass
class Producto:
    id: int
    nombre: str
    precio : float
    stock:int


class producto_model:
    def __init__(self, db:Conexion):
        self.db = db
    
    def todos(self)-> list[Producto]:
        conn = None
        try:
            conn = self.db.conectar()
            cadena = "SELECT * FROM `producto`"
            cur = conn.cursor()
            cur.execute(cadena)
            filas = cur.fetchall()
            return filas
        except Exception as e:
            raise RuntimeError(f"Error al listar los productos")
        finally:
            try:
                if conn:
                    conn.close()
            except Exception:
                pass
    def insertar(self, nombre, precio, stock) -> int:
        conn = None
        try:
            cadena = "INSERT INTO `producto`( `nombre`, `precio`, `stock`) VALUES (%s,%s,%s))"
            conn = self.db.conectar()
            cur = conn.cursor()
            cur.execute(cadena, (nombre, precio, stock))
            conn.commit()
            return cur.lastrowid
        except Exception as e:
            try:
                if conn:
                    conn.rollback()
            except Exception as e:
                pass    
            raise RuntimeError(f"Error al listar los productos")
        finally:
            try:
                if conn:
                    conn.close()
            except Exception:
                pass
    def actualizar(self, id, nombre, precio, stock) -> None:
        conn = None
        try:
            cadena = "UPDATE `producto` SET `nombre`=%s,`precio`=%s,`stock`=%s' WHERE `id`=%s)"
            conn = self.db.conectar()
            cur = conn.cursor()
            cur.execute(cadena, (nombre, precio, stock,id))
            conn.commit()
        except Exception as e:
            try:
                if conn:
                    conn.rollback()
            except Exception as e:
                pass    
            raise RuntimeError(f"Error al listar los productos")
        finally:
            try:
                if conn:
                    conn.close()
            except Exception:
                pass

    def eliminar(self, id) -> None:
        conn = None
        try:
            cadena = "DELETE FROM `producto` WHERE `id`=%s"
            conn = self.db.conectar()
            cur = conn.cursor()
            cur.execute(cadena, (id,))
            conn.commit()
        except Exception as e:
            try:
                if conn:
                    conn.rollback()
            except Exception as e:
                pass    
            raise RuntimeError(f"Error al listar los productos")
        finally:
            try:
                if conn:
                    conn.close()
            except Exception:
                pass
    def uno(self, id)-> Producto:
        conn = None
        try:
            cadena = "SELECT * FROM `producto` WHERE `id`=%s"
            conn = self.db.conectar()
            cur = conn.cursor()
            cur.execute(cadena, (id,))
            fila = cur.fetchone()
            return fila
        except Exception as e:
            raise RuntimeError(f"Error al listar los productos")
        finally:
            try:
                if conn:
                    conn.close()
            except Exception:
                pass
