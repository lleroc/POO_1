import tkinter as tk

from tkinter import ttk, messagebox
from crudcliente import crud_clientes

crud_clientes = crud_clientes()

def carga_clientes_en_tabla():
    for item in tree.get_children():
        tree.delete(item)
    
    for cliente in crud_clientes.todos():
        tree.insert("","end",values=(cliente.id, cliente.nombre, cliente.apellido, cliente.cedula, cliente.telefono, cliente.email))

def limpiar_campos():
    var_id.set("")
    var_nombre.set("")
    var_apellido.set("")
    var_cedula.set("")
    var_telefono.set("")
    var_email.set("")
    txt_dir.delete("1.0", tk.END)

def insertar():
    nombre=var_nombre.get()
    apellido=var_apellido.get()
    cedula=var_cedula.get()
    telefono=var_telefono.get()
    email=var_email.get()
    try:
        crud_clientes.insertar(nombre, apellido, cedula, telefono, email)
        carga_clientes_en_tabla()
        limpiar_campos()
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))   
    
def carga_informacion_cajas():
    cliente_seleccionado = tree.selection()
    if not cliente_seleccionado:
        return
    valores = tree.item(cliente_seleccionado[0],"values")
    var_id.set(valores[0])
    var_nombre.set(valores[1])
    var_apellido.set(valores[2])
    var_cedula.set(valores[3])
    var_telefono.set(valores[4])
    var_email.set(valores[5])
    
def actualizar():
    id = var_id.get()
    if not id:
        messagebox.showerror("Error", "Seleccione un cliente para actualizar")
        return
    try:
        crud_clientes.actualizar(
            int(id),
            var_nombre.get(),
            var_apellido.get(),
            var_cedula.get(),
            var_telefono.get(),
            var_email.get()
        )
        carga_clientes_en_tabla()
        limpiar_campos()
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))    

def eliminar():
    id = var_id.get()
    if not id:
        messagebox.showerror("Error", "Seleccione un cliente para eliminar")
        return
    confirmado = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este cliente?")
    if confirmado:
        eliminado = crud_clientes.eliminar(int(id))
        if eliminado:
            carga_clientes_en_tabla()
            limpiar_campos()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el cliente")

root = tk.Tk()
root.title("CRUD Clientes (Solo Interfaz)")
root.geometry("900x500")


# ---------- Contenedor principal ----------
main = tk.Frame(root, padx=10, pady=10)
main.pack(fill="both", expand=True)

# ---------- Frame Formulario ----------
frm_form = tk.LabelFrame(main, text="Datos del cliente", padx=10, pady=10)
frm_form.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

# Variables (solo para interfaz)
var_id = tk.StringVar()
var_nombre = tk.StringVar()
var_apellido = tk.StringVar()
var_cedula = tk.StringVar()
var_telefono = tk.StringVar()
var_email = tk.StringVar()
var_direccion = tk.StringVar()

# Campos
tk.Label(frm_form, text="ID:").grid(row=0, column=0, sticky="w", pady=4)
ent_id = tk.Entry(frm_form, textvariable=var_id, state="disabled", width=30)
ent_id.grid(row=0, column=1, pady=4, sticky="w")

tk.Label(frm_form, text="Nombre:").grid(row=1, column=0, sticky="w", pady=4)
tk.Entry(frm_form, textvariable=var_nombre, width=30).grid(row=1, column=1, pady=4, sticky="w")

tk.Label(frm_form, text="Apellido:").grid(row=2, column=0, sticky="w", pady=4)
tk.Entry(frm_form, textvariable=var_apellido, width=30).grid(row=2, column=1, pady=4, sticky="w")

tk.Label(frm_form, text="Cédula / DNI:").grid(row=3, column=0, sticky="w", pady=4)
tk.Entry(frm_form, textvariable=var_cedula, width=30).grid(row=3, column=1, pady=4, sticky="w")

tk.Label(frm_form, text="Teléfono:").grid(row=4, column=0, sticky="w", pady=4)
tk.Entry(frm_form, textvariable=var_telefono, width=30).grid(row=4, column=1, pady=4, sticky="w")

tk.Label(frm_form, text="Email:").grid(row=5, column=0, sticky="w", pady=4)
tk.Entry(frm_form, textvariable=var_email, width=30).grid(row=5, column=1, pady=4, sticky="w")

tk.Label(frm_form, text="Dirección:").grid(row=6, column=0, sticky="nw", pady=4)
txt_dir = tk.Text(frm_form, width=30, height=4)
txt_dir.grid(row=6, column=1, pady=4, sticky="w")

# ---------- Frame Botones ----------
frm_btn = tk.LabelFrame(main, text="Acciones", padx=10, pady=10)
frm_btn.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=(10, 0))

# Botones (sin comandos / sin lógica)
btn_nuevo = tk.Button(frm_btn, text="Nuevo", width=12)
btn_guardar = tk.Button(frm_btn, text="Guardar", width=12)
btn_actualizar = tk.Button(frm_btn, text="Actualizar", width=12)
btn_eliminar = tk.Button(frm_btn, text="Eliminar", width=12)
btn_limpiar = tk.Button(frm_btn, text="Limpiar", width=12)

btn_nuevo.grid(row=0, column=0, padx=5, pady=5)
btn_guardar.grid(row=0, column=1, padx=5, pady=5)
btn_actualizar.grid(row=0, column=2, padx=5, pady=5)
btn_eliminar.grid(row=0, column=3, padx=5, pady=5)
btn_limpiar.grid(row=0, column=4, padx=5, pady=5)

btn_limpiar.config(command=limpiar_campos)
btn_guardar.config(command=insertar)
btn_nuevo.config(command=limpiar_campos)
btn_actualizar.config(command=actualizar)
btn_eliminar.config(command=eliminar) 

# ---------- Frame Tabla ----------
frm_tabla = tk.LabelFrame(main, text="Listado de clientes", padx=10, pady=10)
frm_tabla.grid(row=0, column=1, rowspan=2, sticky="nsew")

# Barra de búsqueda (solo interfaz)
frm_buscar = tk.Frame(frm_tabla)
frm_buscar.pack(fill="x", pady=(0, 8))

tk.Label(frm_buscar, text="Buscar:").pack(side="left")
ent_buscar = tk.Entry(frm_buscar, width=30)
ent_buscar.pack(side="left", padx=6)
btn_buscar = tk.Button(frm_buscar, text="Buscar", width=10)
btn_buscar.pack(side="left")

# Tabla (Treeview)
cols = ("id", "nombre", "apellido", "cedula", "telefono", "email")
tree = ttk.Treeview(frm_tabla, columns=cols, show="headings", height=16)

tree.heading("id", text="ID")
tree.heading("nombre", text="Nombre")
tree.heading("apellido", text="Apellido")
tree.heading("cedula", text="Cédula/DNI")
tree.heading("telefono", text="Teléfono")
tree.heading("email", text="Email")

tree.column("id", width=60, anchor="center")
tree.column("nombre", width=130)
tree.column("apellido", width=130)
tree.column("cedula", width=110)
tree.column("telefono", width=110)
tree.column("email", width=170)

tree.bind("<<TreeviewSelect>>", lambda e: carga_informacion_cajas())

# Scrollbars
scroll_y = ttk.Scrollbar(frm_tabla, orient="vertical", command=tree.yview)
scroll_x = ttk.Scrollbar(frm_tabla, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

tree.pack(fill="both", expand=True)
scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")

# ---------- Layout responsive básico ----------
main.grid_columnconfigure(0, weight=0)
main.grid_columnconfigure(1, weight=1)
main.grid_rowconfigure(0, weight=1)


carga_clientes_en_tabla()

root.mainloop()
