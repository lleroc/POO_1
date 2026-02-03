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


if __name__ == "__main__":
    app = AlumnoView()
    app.mainloop()