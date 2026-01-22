# tkinter

import tkinter as tk
from tkinter import ttk, messagebox

app = tk.Tk()
app.title("estion de Publicaciones")
app.geometry("900x600")


titulo = tk.StringVar()
autor = tk.StringVar()
anio = tk.IntVar()

frm = tk.LabelFrame(app, text="Gestion de Publicaciones", padx=20, pady=20)
frm.pack(fill="both", padx=10, pady=10, expand=True)

tk.Label(frm, text="Titulo:").grid(row=0, column=0, sticky="e")
tk.Entry(frm, textvariable=titulo, width=70,bg="#ffffff", fg="#000000").grid(row=0, column=1, sticky="w")

tk.Label(frm, text="Autor:").grid(row=1, column=0, sticky="e")
tk.Entry(frm, textvariable=autor, width=70,bg="#ffffff", fg="#000000").grid(row=1, column=1, sticky="w")

tk.Label(frm, text="Año:").grid(row=2, column=0, sticky="e")
tk.Entry(frm, textvariable=anio, width=70,bg="#ffffff",fg="#000000").grid(row=2, column=1, sticky="w")


mensaje = messagebox.showinfo("Info", "Publicacion agregada exitosamente")
tk.Button(frm, text="Aceptar", command=mensaje).grid(row=4, column=0, columnspan=2)


tk.Button(frm, 
          text="Agregar Publicacion", 
          bg="#4CAF50", 
          fg="white", 
          width=20).grid(row=3, 
                         column=0, 
                         columnspan=2, 
                         pady=10)

#combo box.   ---- select
#lista desplegable
#lista
#checkbox



app.mainloop()