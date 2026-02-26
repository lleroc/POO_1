import tkinter as tk    
from tkinter import ttk, messagebox

class ProveedoresView(tk.Tk):
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.title = "CRUD PROVEEDORES"
        self.geometry("950x450")
        #self.resizable(False, False)

        self._buil_ui()
        self._cargar_lista()

    def _buil_ui(self):
        form = ttk.LabelFrame(self,text="Proveedor", padding=10)
        form.place(x=10, y=10, width=450, height=350)

        ttk.Label(form, text="Nombre: ").grid(row=0,column=0, pady=6)
        self.txt_nombre = ttk.Entry(form,width=40)
        self.txt_nombre.grid(row=0,column=1, pady=6)

        ttk.Label(form, text="RUC: ").grid(row=1,column=0, pady=6)
        self.txt_RUC = ttk.Entry(form,width=40)
        self.txt_RUC.grid(row=1,column=1, pady=6)

        ttk.Label(form, text="Telefono: ").grid(row=2,column=0, pady=6)
        self.txt_telefono = ttk.Entry(form,width=40)
        self.txt_telefono.grid(row=2,column=1, pady=6)

        ttk.Label(form, text="Email: ").grid(row=3,column=0, pady=6)
        self.txt_email = ttk.Entry(form,width=40)
        self.txt_email.grid(row=3,column=1, pady=6)

        ttk.Label(form, text="Direccion: ").grid(row=0,column=0, pady=6)
        self.txt_direccion = ttk.Entry(form,width=40)
        self.txt_direccion.grid(row=4,column=1, pady=6)

        btns = ttk.Frame(form)
        btns.grid(row=5, column=0,columnspan=2, pady=16)

        ttk.Button(btns, text='Crear',command=self._crear).grid(row=0, column=0,padx=6)
        ttk.Button(btns, text='Actualizar', command=self._actualizar).grid(row=0, column=1, padx=6)
        ttk.Button(btns, text='Elimianr', command=self._eliminar).grid(row=0, column=2, padx=6)
        ttk.Button(btns, text='Limpiar Cajas', command=self._limpiarcajas).grid(row=0, column=3, padx=6)

        #tabla
        tabla_frame = ttk.LabelFrame(self, text="Lista de Proveedores", padding=10)
        tabla_frame.place(x=470,y=10,width=470,height=400)

        columnas = ("id", "nombre", "ruc", "telefono", "email", "direccion")
        self.tabla = ttk.Treeview(tabla_frame,columns=columnas,show="headings", height=12)

        for columna, texto in [("id","ID"),("nombre","Nombre"),("ruc","RUC"),("telefono","Tel."),
                               ("email","Email"),('direccion',"Dir.")]:
            self.tabla.heading(columna,text=texto)
        
        self.tabla.column('id', width=30, anchor="center")
        self.tabla.column("nombre",width=140)
        self.tabla.column("ruc",width=95)
        self.tabla.column("telefono",width=75)
        self.tabla.column("email",width=125)
        self.tabla.column("direccion",width=160)

        self.tabla.pack(fill="both", expand=True)
        self.tabla.bind("<<TreeviewSelect>>", self._on_select)

        ttk.Button(self, text="Recargar Tabla", command=self._cargar_lista).grid(row=6, column=0, columnspan=2)

    def _data_form(self):
        return {
            "nombre":self.txt_nombre.get().strip(),
            "ruc":self.txt_RUC.get().strip(),
            "telefono":self.txt_telefono.get().strip(),
            "email":self.txt_email.get().strip(),
            "direccion":self.txt_direccion.get().strip(),
        }
    def _cargar_lista(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        
        lista_proveedores = self.controller.listar()
        for proveedor in lista_proveedores:
            self.tabla.insert('',"end", values=(proveedor["id"],proveedor["nombre"],proveedor["ruc"],
                                                proveedor["telefono"], proveedor["email"],
                                                proveedor['direccion']))
        
    def _get_selected_id(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            return None
        valores = self.tabla.item(seleccion[0],'values')
        return int(valores[0])
    
    def _on_select(self, _event:None):
        seleccion = self.tabla.selection()
        if not seleccion:
            return 
        vector = self.tabla.item(seleccion[0],"values")
        self.txt_nombre.insert(0,vector[1])
        self.txt_RUC.insert(0,vector[2])
        self.txt_telefono.insert(0,vector[3])
        self.txt_email.insert(0,vector[4])
        self.txt_direccion.insert(0,vector[5])
    
    def _crear(self):
        try:
            self.controller.crear(self._data_form())
            messagebox.showinfo("ok", "Proveedor creado")
            self._limpiarcajas()
            self._cargar_lista()
        except Exception as e:
            messagebox.showerror("Error",str(e))
    
    def _actualizar(self):
        try:
            id_proveedor = self._get_selected_id()
            if id_proveedor is None:
                messagebox.showwarning("Proveedores","Seleccione un proveedore de la tabla")
                return
            self.controller.actualizar(id_proveedor,self._data_form())
            messagebox.showinfo("ok", "Proveedor Actualizado")
            self._limpiarcajas()
            self._cargar_lista()
        except Exception as e:
            messagebox.showerror("Error",str(e))

    def _eliminar(self):
        try:
            id_proveedor = self._get_selected_id()
            if id_proveedor is None:
                messagebox.showwarning("Proveedores","Seleccione un proveedore de la tabla")
                return
            self.controller.eliminar(id_proveedor)
            messagebox.showinfo("ok", "Proveedor Eliminado")
            self._limpiarcajas()
            self._cargar_lista()
        except Exception as e:
            messagebox.showerror("Error",str(e))
    
    def _limpiarcajas(self):
        for cajas_texto in (self.txt_direccion, self.txt_email, self.txt_nombre, 
                            self.txt_RUC, self.txt_telefono):
            cajas_texto.delete(0, tk.END)



    










        





