import tkinter as tk
from tkinter import ttk, messagebox
from models.usuario_model import  usuario_model
from config.config import DB_CONFIG
from database.connection import database_connection
db = database_connection.obtener_conexion(DB_CONFIG)
modelo_usuario = usuario_model()

def abrir_app():
    #ventana principal (despues del login)
    app = tk.Toplevel(root)
    app.title("Dashboard")
    app.geometry("400x200")
    ttk.Label(app, text="Bienvenido", font=("Arial",14)).pack(pady=30)
    ttk.Button(app,text="Salir", command=app.destroy).pack()

def login():
    user = txt_user.get().strip()
    cotnrasenia = txt_contrasenia.get().strip()

    objeto_ususaurio = usuario_model.login_con_erorr(user, cotnrasenia)
    print(objeto_ususaurio)

    if objeto_ususaurio.usuario == user and objeto_ususaurio.contrasenia == cotnrasenia:
        messagebox.showinfo("Login", "Login exitoso")
        txt_contrasenia.delete(0,tk.END)
        txt_user.delete(0,tk.END)
        abrir_app()
    else:
        messagebox.showerror("Login","El usuario o a contraseña son incorrectos")
    
def salir():
    root.destroy()

#ventana login
root = tk.Tk()
root.title("Login usuarios")
        #    ancho x alto
root.geometry("470x200")
#root.resizable(False,False)

frm = ttk.Frame(root,padding=15)
frm.pack(fill="both", expand=True)

ttk.Label(frm,text="Usuario:").grid(row=0,column=0,sticky="w",pady=5)
txt_user = ttk.Entry(frm,width=25)
txt_user.grid(row=0,column=1,pady=5)
txt_user.focus()

ttk.Label(frm, text="Contraseña:").grid(row=1,column=0,sticky="w",pady=5)
txt_contrasenia = ttk.Entry(frm, width=25, show="*")
txt_contrasenia.grid(row=1,column=1, pady=5)

root.bind("<Return>", lambda e: login())

botones = ttk.Frame(frm)
botones.grid(row=2, column=0, pady=15)

ttk.Button(botones, text="Ingresar",command=login).grid(row=0, column=0, padx=5)
ttk.Button(botones,text="Salir",command=salir).grid(row=0, column=1,padx=5)
root.mainloop()



