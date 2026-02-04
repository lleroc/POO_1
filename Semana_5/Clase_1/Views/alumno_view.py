import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional


import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from Controllers.alumno_controller import AlumnoController
from Models.alumno_model import Alumno

class AlumnoView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Alumnos")
        self.geometry("900x600")

        self.alumno_controller = AlumnoController()

        self._build_UI()
    
    def _build_UI(self):
        frm = ttk.LabelFrame(self, text="Datos del Alumno")
        frm.pack(fill="x", padx=10,pady=10)

        #variable que voy a usar en el formulario (vista)
        self.var_cedula = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_apellido = tk.StringVar()
        self.var_nivel = tk.IntVar()
        self.var_paralelo = tk.StringVar()
        self.var_edad = tk.IntVar()

        #grid
        labels = [
            ("Cedula", self.var_cedula),
            ("Nombre", self.var_nombre),
            ("Apellido", self.var_apellido),
            ("Nivel", self.var_nivel),
            ("Paralelo", self.var_paralelo),
            ("Edad", self.var_edad),
        ]
        for i, (txt, var) in enumerate(labels):
            r = i // 3
            c = (i % 3) * 2
            ttk.Label(frm, text=txt).grid(row=r, column=c, padx=8, pady=6, sticky="w")
            ttk.Entry(frm, textvariable=var, width=25).grid(row=r, column=c + 1, padx=8, pady=6, sticky="w")

        # Botones
        btns = ttk.Frame(self)
        btns.pack(fill="x", padx=10, pady=5)

        ttk.Button(btns, text="Crear", command=self.crear).pack(side="left", padx=5)
        ttk.Button(btns, text="Editar (por cédula)", command=self.editar).pack(side="left", padx=5)
        ttk.Button(btns, text="Eliminar (por cédula)", command=self.eliminar).pack(side="left", padx=5)

        ttk.Separator(btns, orient="vertical").pack(side="left", fill="y", padx=10)

        ttk.Button(btns, text="Buscar por Cédula", command=self.buscar_cedula).pack(side="left", padx=5)
        ttk.Button(btns, text="Buscar por Apellido", command=self.buscar_apellido).pack(side="left", padx=5)
        ttk.Button(btns, text="Listar Todos", command=self.listar_todos).pack(side="left", padx=5)
        ttk.Button(btns, text="Limpiar", command=self.limpiar_form).pack(side="left", padx=5)

        # Tabla (Treeview)
        table_frame = ttk.Frame(self)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        cols = ("cedula", "nombre", "apellido", "nivel", "paralelo", "edad")
        self.tree = ttk.Treeview(table_frame, columns=cols, show="headings", height=12)

        for col, title, w in [
            ("cedula", "Cédula", 140),
            ("nombre", "Nombre", 160),
            ("apellido", "Apellido", 160),
            ("nivel", "Nivel", 80),
            ("paralelo", "Paralelo", 100),
            ("edad", "Edad", 70),
        ]:
            self.tree.heading(col, text=title)
            self.tree.column(col, width=w, anchor="w")

        yscroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=yscroll.set)

        self.tree.pack(side="left", fill="both", expand=True)
        yscroll.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.on_select_row)

        # Estado
        self.status = tk.StringVar(value="Listo.")
        ttk.Label(self, textvariable=self.status).pack(fill="x", padx=10, pady=(0, 10))
    def set_status(self, msg: str):
        self.status.set(msg)

    def limpiar_form(self):
        self.var_cedula.set("")
        self.var_nombre.set("")
        self.var_apellido.set("")
        self.var_nivel.set("")
        self.var_paralelo.set("")
        self.var_edad.set("")
        self.set_status("Formulario limpio.")

    def _parse_int_or_none(self, text: str) -> Optional[int]:
        text = text.strip()
        if text == "":
            return None
        try:
            return int(text)
        except ValueError:
            return None

    def _build_alumno_for_crear(self) -> Optional[Alumno]:
        cedula = self.var_cedula.get().strip()
        nombre = self.var_nombre.get().strip()
        apellido = self.var_apellido.get().strip()
        paralelo = self.var_paralelo.get().strip()

        nivel_txt = self.var_nivel.get()
        edad_txt = self.var_edad.get()

        if not all([cedula, nombre, apellido, paralelo, nivel_txt, edad_txt]):
            messagebox.showwarning("Validación", "Para CREAR debes llenar todos los campos.")
            return None

        try:
            nivel = int(nivel_txt)
            edad = int(edad_txt)
        except ValueError:
            messagebox.showwarning("Validación", "Nivel y edad deben ser números enteros.")
            return None

        return Alumno(nombre, apellido, nivel, paralelo, edad, cedula)

    def _build_alumno_for_editar(self) -> Alumno:
        """
        Para editar permitimos campos vacíos:
        - si el campo está vacío => se manda '' o None y el controller no lo actualiza
        """
        cedula_nueva = self.var_cedula.get().strip()
        nombre = self.var_nombre.get().strip()
        apellido = self.var_apellido.get().strip()
        paralelo = self.var_paralelo.get().strip()

        nivel = self._parse_int_or_none(self.var_nivel.get())
        edad = self._parse_int_or_none(self.var_edad.get())

        # OJO: tu controller usa "if alumno_parametro.cedula:" para actualizar
        # así que si cedula_nueva está vacía, no la cambia.
        # Para ints, el controller usa "is not None" (en el que te pasé).
        return Alumno(
            nombre if nombre != "" else "",
            apellido if apellido != "" else "",
            nivel,                               # puede ser None
            paralelo if paralelo != "" else "",
            edad,                                # puede ser None
            cedula_nueva if cedula_nueva != "" else ""
        )

    def _refresh_tree(self, alumnos: list[Alumno]):
        # limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # cargar
        for alu in alumnos:
            # usamos properties: alu.cedula, alu.nombre, etc.
            self.tree.insert("", "end", values=(
                alu._Alumno__cedula,
                alu._Alumno__nombre,
                alu._Alumno__apellido,
                alu._Alumno__nivel,
                alu._Alumno__paralelo,
                alu._Alumno__edad
            ))

    # ---------- Eventos ----------
    def on_select_row(self, _event=None):
        sel = self.tree.selection()
        if not sel:
            return
        values = self.tree.item(sel[0], "values")
        # values: (cedula, nombre, apellido, nivel, paralelo, edad)
        self.var_cedula.set(values[0])
        self.var_nombre.set(values[1])
        self.var_apellido.set(values[2])
        self.var_nivel.set(values[3])
        self.var_paralelo.set(values[4])
        self.var_edad.set(values[5])
        self.set_status(f"Seleccionado: {values[1]} {values[2]}")

    # ---------- Acciones CRUD ----------
    def crear(self):
        alumno = self._build_alumno_for_crear()
        if alumno is None:
            return

        msg = self.alumno_controller.crear(alumno)
        self.set_status(msg)
        messagebox.showinfo("Crear", msg)
        self._refresh_tree(self.alumno_controller.todos())

    def editar(self):
        cedula_buscar = self.var_cedula.get().strip()
        if cedula_buscar == "":
            messagebox.showwarning("Validación", "Para EDITAR, escribe la cédula (la actual) en el campo Cédula.")
            return

        alumno_param = self._build_alumno_for_editar()
        msg = self.alumno_controller.editar(cedula_buscar, alumno_param)
        self.set_status(msg)
        messagebox.showinfo("Editar", msg)
        self._refresh_tree(self.alumno_controller.todos())

    def eliminar(self):
        cedula = self.var_cedula.get().strip()
        if cedula == "":
            messagebox.showwarning("Validación", "Para ELIMINAR, escribe la cédula.")
            return

        if not messagebox.askyesno("Confirmar", f"¿Seguro que quieres eliminar al alumno con cédula {cedula}?"):
            return

        msg = self.alumno_controller.eliminar(cedula)
        self.set_status(msg)
        messagebox.showinfo("Eliminar", msg)
        self._refresh_tree(self.alumno_controller.todos())

    def buscar_cedula(self):
        cedula = self.var_cedula.get().strip()
        if cedula == "":
            messagebox.showwarning("Validación", "Escribe una cédula para buscar.")
            return

        alu = self.alumno_controller.uno_cedula(cedula)
        if alu is None:
            self.set_status("No encontrado.")
            messagebox.showinfo("Buscar", "No existe un alumno con esa cédula.")
            self._refresh_tree([])
            return

        self.set_status(f"Encontrado: {alu._Alumno__nombre} {alu._Alumno__apellido}")
        self._refresh_tree([alu])

    def buscar_apellido(self):
        apellido = self.var_apellido.get().strip()
        if apellido == "":
            messagebox.showwarning("Validación", "Escribe un apellido para buscar.")
            return

        alu = self.alumno_controller.uno_apellido(apellido)
        if alu is None:
            self.set_status("No encontrado.")
            messagebox.showinfo("Buscar", "No existe un alumno con ese apellido.")
            self._refresh_tree([])
            return

        self.set_status(f"Encontrado: {alu._Alumno__nombre} {alu._Alumno__apellido}")
        self._refresh_tree([alu])

    def listar_todos(self):
        alumnos = self.alumno_controller.todos()
        self._refresh_tree(alumnos)
        self.set_status(f"Total alumnos: {len(alumnos)}")


if __name__ == "__main__":
    app = AlumnoView()
    app.mainloop()
