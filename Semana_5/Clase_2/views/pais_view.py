import tkinter as tk    
from tkinter import ttk

class PaisView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master,padding=12)

        self.master = master

        self.id_var = tk.IntVar()
        self.nombre_var = tk.StringVar()

        #form
        form = ttk.LabelFrame(self, "Gestion de Paises", padding=10)
        form.grid(row=0,column=0, sticky="ew")

        ttk.Label(form, text="ID de Pais").grid(row=0, column=0, sticky="w")
        self.id_entrada = ttk.Entry(form, textvariable=self.id_var, width=12, state="readonly")
        self.id_entrada.grid(row=0, column=1, sticky="w", padx=(8, 0))

        ttk.Label(form, text="Nombre de Pais").grid(row=1, column=0, sticky="w")
        self.id_entrada = ttk.Entry(form, textvariable=self.id_var, width=40)
        self.id_entrada.grid(row=1, column=1, sticky="w", padx=(8, 0), pady=(8, 0))

        botones = ttk.Frame(form)
        botones.grid(row=2, column=0,columnspan=2, sticky="w",pady=(12,0))

        self.btn_guardar = ttk.Button(botones, text="Guardar")
        self.btn_actualizar = ttk.Button(botones, text="Actualizar")
        self.btn_eliminar = ttk.Button(botones, text="Eliminar")
        self.btn_limpiar = ttk.Button(botones, text="Limpiar Cajas")

        self.btn_guardar.grid(row=0, column=0,padx=(0,6))
        self.btn_actualizar.grid(row=0,column=1,padx=(0,6))
        self.btn_eliminar.grid(row=0,column=2,padx=(0,6))
        self.btn_limpiar.grid(row=0, column=3)

         # List (Treeview)
        lista_frame = ttk.LabelFrame(self, text="Listado", padding=10)
        lista_frame.grid(row=1, column=0, sticky="nsew", pady=(12, 0))

        self.tree = ttk.Treeview(lista_frame, columns=("id", "nombre"), show="headings", height=12)
        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.column("id", width=80, anchor="center")
        self.tree.column("nombre", width=360, anchor="w")

        yscroll = ttk.Scrollbar(lista_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=yscroll.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")

        lista_frame.grid_columnconfigure(0, weight=1)
        lista_frame.grid_rowconfigure(0, weight=1)

        # Layout weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Bind select
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        # Controller will be attached later
        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller
        self.btn_guardar.configure(command=self.controller.guardar)
        self.btn_actualizar.configure(command=self.controller.actualizar)
        self.btn_eliminar.configure(command=self.controller.eliminar)
        self.btn_limpiar.configure(command=self.limpiar_form)

    def render_lista(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for (pid, nombre) in rows:
            self.tree.insert("", "end", values=(pid, nombre))

    def limpiar_form(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.tree.selection_remove(self.tree.selection())
        self.nombre_entry.focus_set()

    def _on_select(self, _event):
        sel = self.tree.selection()
        if not sel:
            return
        values = self.tree.item(sel[0], "values")
        self.id_var.set(str(values[0]))
        self.nombre_var.set(str(values[1]))




