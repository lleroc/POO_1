import tkinter as tk
from tkinter import ttk

from views.pais_view import PaisView
from controllers.pais_controller import PaisController

def main():
    root = tk.Tk()
    root.title("CRUD País - Tkinter + MySQL (MVC)")
    root.geometry("600x500")

    # Theme (opcional)
    try:
        ttk.Style().theme_use("clam")
    except:
        pass

    view = PaisView(root)
    view.pack(fill="both", expand=True)

    controller = PaisController(view)
    view.set_controller(controller)

    controller.cargar_lista()

    root.mainloop()

if __name__ == "__main__":
    main()
