import tkinter as tk
from tkinter import ttk, messagebox

class VistaClientes(tk.Toplevel):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador

        self.title("Clientes - CRUD (MVC)")
        self.geometry("800x600")
        self.resizable(False, False)

        # Mantener "formato dashboard": un contenido centrado, con secciones claras
        self.etiqueta_titulo = tk.Label(self, text="Gestión de Clientes", font=("Arial", 18))
        self.etiqueta_titulo.pack(pady=10)

        self.marco_formulario = tk.Frame(self)
        self.marco_formulario.pack(fill="x", padx=20)

        # Campos
        tk.Label(self.marco_formulario, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Label(self.marco_formulario, text="Email:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Label(self.marco_formulario, text="Teléfono:").grid(row=2, column=0, sticky="w", pady=5)

        self.entrada_nombre = tk.Entry(self.marco_formulario, width=40)
        self.entrada_email = tk.Entry(self.marco_formulario, width=40)
        self.entrada_telefono = tk.Entry(self.marco_formulario, width=40)

        self.entrada_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.entrada_email.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.entrada_telefono.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Botones
        self.marco_botones = tk.Frame(self)
        self.marco_botones.pack(fill="x", padx=20, pady=10)

        self.boton_nuevo = tk.Button(self.marco_botones, text="Nuevo", command=self.controlador.limpiar_cajas)
        self.boton_guardar = tk.Button(self.marco_botones, text="Guardar", command=self.controlador.insertar)
        self.boton_actualizar = tk.Button(self.marco_botones, text="Actualizar", command=self.controlador.actualizar)
        self.boton_eliminar = tk.Button(self.marco_botones, text="Eliminar", command=self.controlador.eliminar)
        self.boton_refrescar = tk.Button(self.marco_botones, text="Refrescar", command=self.controlador.refrescar)

        self.boton_nuevo.pack(side="left", padx=5)
        self.boton_guardar.pack(side="left", padx=5)
        self.boton_actualizar.pack(side="left", padx=5)
        self.boton_eliminar.pack(side="left", padx=5)
        self.boton_refrescar.pack(side="left", padx=5)

        # Tabla
        self.marco_tabla = tk.Frame(self)
        self.marco_tabla.pack(expand=True, fill="both", padx=20, pady=10)

        columnas = ("id", "nombre", "email", "telefono")
        self.tabla = ttk.Treeview(self.marco_tabla, columns=columnas, show="headings", height=18)

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("email", text="Email")
        self.tabla.heading("telefono", text="Teléfono")

        self.tabla.column("id", width=60, anchor="center")
        self.tabla.column("nombre", width=220)
        self.tabla.column("email", width=260)
        self.tabla.column("telefono", width=160)

        self.tabla.pack(side="left", expand=True, fill="both")

        scrollbar = ttk.Scrollbar(self.marco_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.tabla.bind("<<TreeviewSelect>>", self._al_seleccionar_fila)

        # Estado interno
        self.cliente_id_seleccionado = None

    def _al_seleccionar_fila(self, _evento):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        item = self.tabla.item(seleccion[0])
        valores = item["values"]
        self.cliente_id_seleccionado = valores[0]

        self.entrada_nombre.delete(0, tk.END)
        self.entrada_nombre.insert(0, valores[1])

        self.entrada_email.delete(0, tk.END)
        self.entrada_email.insert(0, valores[2] if valores[2] else "")

        self.entrada_telefono.delete(0, tk.END)
        self.entrada_telefono.insert(0, valores[3] if valores[3] else "")

    # Helpers que el controlador usa
    def limpiar_formulario(self):
        self.cliente_id_seleccionado = None
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_email.delete(0, tk.END)
        self.entrada_telefono.delete(0, tk.END)
        self.tabla.selection_remove(self.tabla.selection())

    def obtener_datos_formulario(self):
        return (
            self.entrada_nombre.get().strip(),
            self.entrada_email.get().strip(),
            self.entrada_telefono.get().strip(),
        )

    def cargar_en_tabla(self, filas):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for fila in filas:
            self.tabla.insert("", tk.END, values=(fila["id"], fila["nombre"], fila["email"], fila["telefono"]))

    def alertar(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def confirmar(self, titulo, mensaje):
        return messagebox.askyesno(titulo, mensaje)

    def error(self, titulo, mensaje):
        messagebox.showerror(titulo, mensaje)