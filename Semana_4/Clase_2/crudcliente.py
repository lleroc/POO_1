from cliente import cliente
class crud_clientes:
    def __init__(self):
        self._clientes:list[cliente] = []
        self._next_id:int = 1
    #-----crear un cliente
    def insertar(self, nombre: str, 
                 apellido: str, 
                 cedula: str, telefono: str, email: str)->cliente:
        #validadores nombre, apellido, cedula, telefono, email =>m texto de validacion
                    #self.validadores_texto(nombre, "nombre")
                    #self.validadores_texto(apellido, "apellido")
                    #self.validadores_texto(cedula, "cedula")
                    #self.validadores_texto(telefono, "telefono")
                    #self.validadores_texto(email, "email")
        #verificar si la cedula ya existe
        if self.cedula_repetida(cedula):
            raise ValueError(f"La cedula {cedula} ya existe")

        if self._next_id == 1:
            #cliente por defecto
            cliente_defecto = cliente()
            cliente_defecto.id = self._next_id
            cliente_defecto.nombre = "Juan"
            cliente_defecto.apellido = "Perez"
            cliente_defecto.cedula = "1234567890"
            cliente_defecto.telefono = "3001234567"
            cliente_defecto.email = "juan.perez@example.com"
            self._clientes.append(cliente_defecto)
            self._next_id += 1


            cliente_defecto = cliente()
            cliente_defecto.id = self._next_id
            cliente_defecto.nombre = "Isabel"
            cliente_defecto.apellido = "Arteaga"
            cliente_defecto.cedula = "0987654321"
            cliente_defecto.telefono = "342534534"
            cliente_defecto.email = "isabel.arteaga@example.com"
            self._clientes.append(cliente_defecto)
            self._next_id += 1




        nuevo_cliente = cliente()
        nuevo_cliente.id = self._next_id
        nuevo_cliente.nombre = nombre
        nuevo_cliente.apellido = apellido
        nuevo_cliente.cedula = cedula
        nuevo_cliente.telefono = telefono
        nuevo_cliente.email = email
        self._clientes.append(nuevo_cliente)
        self._next_id += 1
        return nuevo_cliente
    #-----todos los clientes.   select * from clientes
    def todos(self)-> list[cliente]:
        return list(self._clientes)
    #----obtener un solo cliente por id. where id=?
    def uno_x_id(self, id:int)->cliente|None:
       return next ((c for c in self._clientes if c.id == id), None)
    
    """
        for c in self._clientes:
            if c.id == id:
                return c
            else:
                return None
    """

    #----obtener un solo cliente por cedula, buscar
    def uno_x_cedula(self, cedula:str)->cliente|None:
       return next ((c for c in self._clientes if c.cedula == cedula), None)

    #----obtener un solo cliente por apellido.  buscar
    def uno_x_apellido(self, apellido:str)->cliente|None:
       return next ((c for c in self._clientes if c.apellido == apellido), None)
    
    def actualizar(self, id:int, nombre: str, 
                 apellido: str, 
                 cedula: str, telefono: str, email: str)->cliente:
        cliente_actualizar = self.uno_x_id(id)
        if cliente_actualizar is None:
            raise ValueError(f"No existe un cliente con id {id}")
        if cedula != '':
            cliente_actualizar.cedula = cedula
        if nombre != '':
            cliente_actualizar.nombre = nombre
        if apellido != '':
            cliente_actualizar.apellido = apellido
        if telefono != '':
            cliente_actualizar.telefono = telefono
        if email != '':
            cliente_actualizar.email = email    
        return cliente_actualizar
    
    def eliminar(self, id:int)->bool:
        for i, c in enumerate(self._clientes):
            if c.id == id:
                del self._clientes[i]
                return True
        return False
    
    def cedula_repetida(self, cedula:str)->bool:
        cedula = cedula.strip()
        return any(c.cedula == cedula for c in self._clientes) 
    
    def validadores_texto(valor:str, campo:str):
        if valor is None or not str(valor).strip():
            raise ValueError(f"El valor no puede estar vacio")
        


