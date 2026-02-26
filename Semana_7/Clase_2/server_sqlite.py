import socket
import threading
import json
import sqlite3
from dataclasses import dataclass
DB_PATH = "escuela.db"
#---------modelo------------
@dataclass
class Alumno:
    id: int | None
    nombre:str
    apellido:str
    edad: int

#--------DAO (SQLite)-------

class SqlLiteConnectionFactory:
    def __init__(self, db_path:str):
        self.db_path = db_path
    
    def create(self):
        return sqlite3.connect(self.db_path,check_same_thread=False)

class AlumnoDAO:
    def __init__(self, factory: SqlLiteConnectionFactory):
        self.factory = factory
        self.__init__db()

    def __init__db(self):
        try:
            con = self.factory.create()
            con.execute("""
                CREATE TABLE IF NOT EXISTS alumnos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                edad INTEGER NOT NULL)
             """)
            con.commit()
        except Exception as e:
            raise f"Error al crear la tabla alumno: {e}"

        finally:
            con.close()
    
    def todos(self):
        con = self.factory.create()
        con.row_factory = sqlite3.Row
        filas = con.execute("select * from alumnos").fetchall()
        con.close
        return dict(filas) if filas else None
    
    def uno(self, alumno_id: int):
        con = self.factory.create()
        con.row_factory = sqlite3.Row
        filas = con.execute("select * from alumnos where id =?",(alumno_id,)).fetchone()
        con.close
        return dict(filas) if filas else None 

    def insertar(self, alumno:Alumno):
        con = self.factory.create()
        cur = con.execute(
            "insert into alumnos(nombre, apellido, edad) values(?,?,?)",
            (alumno.nombre, alumno.apellido, alumno.edad)
        )
        con.commit()
        afectacion = cur.rowcount
        return afectacion
    
    def actualizar(self,alumno_id:int, alumno:Alumno):
        con = self.factory.create()
        if alumno_id != alumno.id:
            return "No se logro actualizar al alumno"
        cur = con.execute(
            "update alumnos set nombre=?, apellido=?, edad=? where id=?" ,
            (alumno.nombre, alumno.apellido, alumno.edad, alumno_id)
        )
        con.commit()
        afectacion = cur.rowcount
        return afectacion

    def eliminar(self,alumno_id:int):
        con = self.factory.create()
        cur = con.execute("delete from alumnos where id=?" ,(alumno_id))
        con.commit()
        afectacion = cur.rowcount
        return afectacion
    

class JsonSocketProtocol:
    @staticmethod
    def send(sock: socket.socket, obj:dict):
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        sock.sendall(len(data).to_bytes(4,"big")+data)
    
    @staticmethod
    def recv(sock: socket.socket)-> dict |None:
        header = JsonSocketProtocol._revcall(sock, 4)
        if not header:
            return None
        length = int.from_bytes(header,"big")
        payload = JsonSocketProtocol._revcall(sock, length)
        if not payload:
            return None
        return json.loads(payload.decode("utf-8"))
    @staticmethod
    def _revcall(sock:socket.socket, n:int)->bytes:
        data=b""
        while len(data) < n:
            fila =sock.recv(n - len(data))
            if not fila:
                return b""
            data += fila
        return data

class AlumnoService:
    def __init__(self,dao:AlumnoDAO):
        self.dao = dao
    
    def accion(sefl, req:dict)-> dict:
        try:
            peticion = req.get("action")
            if peticion == "TODOS":
                return {"ok": True, "data":sefl.dao.todos()}
            
            if peticion == "UNO":
                alumno_id = int(req["id"])
                fila = sefl.dao.uno(alumno_id)
                if not fila:
                    return {"ok":True,"error":"El estudiante no existe"}
                return {"ok":True,"data":fila}
            
            if peticion == "INSERTAR":
                p = req.get("payload",{})
                alumno = Alumno(
                    id=None,
                    nombre=str(p.get("nombre","")).strip(),
                    apellido = str(p.get("apellido","")).strip(),
                    edad= int(p.get("edad","")),
                )
                if not alumno.nombre or not alumno.apellido:
                    return {"ok":False,"error":"Los campos son requeridos"}
                neevo_id = sefl.dao.insertar(alumno)
                return {"ok":True,"data":{"id":neevo_id}}

            if peticion == "ACTUALIZAR":
                alumno_id = int(req.get["id"])
                p = req.get("payload",{})
                alumno = Alumno(
                    id=alumno_id,
                    nombre=str(p.get("nombre","")).strip(),
                    apellido = str(p.get("apellido","")).strip(),
                    edad= int(p.get("edad","")),
                )
                if not alumno.nombre or not alumno.apellido:
                    return {"ok":False,"error":"Los campos son requeridos"}
                neevo_id = sefl.dao.actualizar(alumno_id,alumno)
                return {"ok":True,"data":{"id":neevo_id}}
            if peticion == "ELIMINAR":
                 alumno_id = int(req.get["id"])
                 fila_afectada = sefl.dao.eliminar(alumno_id)
                 if fila_afectada == 0:
                     return {"ok":False,"error":"No se logro eliminar al alumno"}
                 return {"ok":True,"data":{"id":neevo_id}} 
            return  {"ok":False,"error":"Opcion no encontrada"}
        except Exception as e:
            return {"ok":False,"error":str(e)}


class TCPServer:
    def __init__(self, host:str,port:int, servicio:AlumnoService):
        self.host = host
        self.port = port
        self.servicio = servicio
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    
    def start(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(20)

        print(f"Servidor de Sql Lite ejecutandose {self.port}")

        while True:
            cliente, addr = self.sock.accept()
            threading.Thread(target=self._handle_alumno, agrs=(cliente, addr),deamon=True).start()
    
    def _handle_alumno(self, alumno: socket.socket, addr):
        while True:
            req = JsonSocketProtocol.recv(alumno)
            if req is None:
                break
            res= self.servicio.accion(req)
            JsonSocketProtocol.send(alumno,res)
        
        alumno.close()


            

        