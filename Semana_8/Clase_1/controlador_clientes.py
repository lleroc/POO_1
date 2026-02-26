from modelo_clientes import ModeloClientes

from vista_cliente import VistaClientes

class ControladorClientes:

    def __init__(self, ventana_dashboard):
        self.modelo_cliente =ModeloClientes()
        self.vista_cliente = VistaClientes(ventana_dashboard,self)
        self.refrescar()

    def limpiar_cajas(self):
        self.vista_cliente.limpiar_cajas()
    
    def refrescar(self):
        try:
            filas = self.modelo_cliente.todos()
            self.vista_cliente.cargar_en_tabla(filas)
        except Exception as e:
            self.vista_cliente.error("Error",f"No se pudo lista la informaicon. \n Detalle: {e}")
    
    def insertar(self):
        nombre, email, telefono = self.vista_cliente.obtener_datos_formulario()
        if not nombre or not email or not telefono:
            self.vista_cliente.error("Error",f"Complete todos los campos del formuario")
        
        try:
            self.modelo_cliente.insertar(nombre, email, telefono)
            self.vista_cliente.alerta("Clientes","Cliente creado con exito")
            self.vista_cliente.limpiar_cajas()
            self.refrescar()
        except Exception as e:
            self.vista_cliente.error("Error",f"No se pudo insertar el cliente")
    
    def actualizar(self):
        if not self.vista_cliente.cliente_id_seleccionado:
            self.vista_cliente.error("Error",f"Seleccione un cliente")
            return 
        nombre, email, telefono = self.vista_cliente.obtener_datos_formulario()
        if not nombre or not email or not telefono:
            self.vista_cliente.error("Error",f"Complete todos los campos del formuario")
        
        try:
            self.modelo_cliente.actualizar(self.vista_cliente.cliente_id_seleccionado, nombre, email, telefono)
            self.vista_cliente.alerta("Clientes","Cliente actualziado con exito")
            self.vista_cliente.limpiar_cajas()
            self.refrescar()
        except Exception as e:
            self.vista_cliente.error("Error",f"No se pudo insertar el cliente")
    
    def eliminar(self):
        if not self.vista_cliente.cliente_id_seleccionado:
            self.vista_cliente.error("Error",f"Seleccione un cliente")
            return 
        
        try:
            self.modelo_cliente.eliminar(self.vista_cliente.cliente_id_seleccionado)
            self.vista_cliente.alerta("Clientes","Cliente se elimino con exito")
            self.vista_cliente.limpiar_cajas()
            self.refrescar()
        except Exception as e:
            self.vista_cliente.error("Error",f"No se pudo insertar el cliente")
    

        



