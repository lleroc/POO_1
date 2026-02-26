import tkinter as tk
from tkinter import messagebox
from controlador_clientes import ControladorClientes


def abrir_dashboard(ventana_principal, usuario: str):
    ventana_principal.withdraw()

    ventana_dashboard = tk.Toplevel(ventana_principal)
    ventana_dashboard.title("Cuadro de Mando Integral")
    ventana_dashboard.geometry("800x600")
    ventana_dashboard.resizable(False, False)

    etiqueta_contenido = tk.Label(ventana_dashboard, text=f"Bievenido {usuario}",
                                  font=("Arial",18))
    etiqueta_contenido.pack(expand=True, fill="both")

    #funciones cerrar sesion, ir inicio, acerce de, salir app, al cerrar
    def cerrar_sesion():
        ventana_dashboard.destroy()
        ventana_principal.deiconify()

    def ir_inicio():
        etiqueta_contenido.config(text="Inicio")
    
    def acerca_de():
        #messagebox.showinfo("Titulo","Texto")
        messagebox.showinfo("Dashborad","Acerca de mi app en python")
    
    def salir_app():
        ventana_principal.destroy()
    
    def al_cerrar():
        ventana_principal.destroy()

    def abrir_ventana_clientes():
        ControladorClientes(ventana_dashboard)

    #menu
    barra_menu = tk.Menu(ventana_dashboard)

    menu_archivo = tk.Menu(barra_menu,tearoff=0)
    menu_archivo.add_command(label="Inicio", command=ir_inicio)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Cerrar Sesion", command=cerrar_sesion)
    menu_archivo.add_command(label="Salir",command=salir_app)

    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)


    menu_cliente = tk.Menu(barra_menu, tearoff=0)
    menu_cliente.add_command(label="Gestion de Clientes", command=abrir_ventana_clientes)
    barra_menu.add_cascade(label="Clientes", menu=menu_cliente)



    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    menu_ayuda.add_command(label="Acerca de", command=acerca_de)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda) 


    ventana_dashboard.config(menu=barra_menu)
    ventana_dashboard.protocol("WN_DELETE_WINDOW", al_cerrar)

