import tkinter as tk
from tkinter import messagebox
from dashborad import abrir_dashboard

def on_login():
    usuario = txt_user.get().strip()
    pwd =txt_contrasenia.get()
    if not usuario or not pwd:
        messagebox.showwarning("Inicio de Sesion","El usuario y la contraseña son requeridos")
        return
    
    #codigo para llamar al controlador
    if usuario == "luis" and pwd == "123":
        messagebox.showinfo("Bienvenido al Sistema","Bienvenido Usuario")
        abrir_dashboard(root, usuario)

        txt_user.delete(0,"end")   
        txt_contrasenia.delete(0,"end") 

    else:
        messagebox.showerror("Inicio de Sesion","El usuario y la contraseña son equivocados")

def toogle_password():
    if txt_contrasenia.cget("show") == "":
        txt_contrasenia.config(show="*")
        btn_mostrar_contrasenia.config(text="Mostrar")
    else:
        txt_contrasenia.config(show="")
        btn_mostrar_contrasenia.config(text="Ocultar")

#ventana principal
root = tk.Tk()
root.title("Inicio de Session")
root.geometry("420x370")
root.resizable(False,False)

BG= "#F7EFD8"
TEXT = "#273142"
ACCENT = "#C8C8A9"
MUTED = "#556270"
CARD="#E4A691"

root.configure(bg=BG)
#contenedor tipo card
card = tk.Frame(root, bg=CARD, bd=0,highlightthickness=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=360,height=360)

title = tk.Label(card,text="Bienvenido", font=("Arial",18,"bold"), bg=CARD,fg=TEXT)
title.pack(pady=(18,4))

subtitle = tk.Label(card,text="Inicie sesion para continuar",font=("Arial",10),bg=CARD,fg=MUTED)
subtitle.pack(pady=(0,16))

#ertiqueta usuario 
lbl_user = tk.Label(card,text="Usuario",font=("Arial",12,"bold"), bg=CARD, fg=TEXT)
lbl_user.pack(anchor="w", padx=28)
#caja de texto usuario
txt_user = tk.Entry(card,font=("Arial",11), bd=0, bg=CARD ,relief="flat")
txt_user.pack(fill="x", padx=28, pady=(6,12), ipady=7)

#contraseña
lbl_contrasenia=tk.Label(card,text="Contraseña",font=("Arial",12,"bold"),
                         bg=CARD,fg=TEXT)
lbl_contrasenia.pack(fill="x",padx=28)

contra_fila = tk.Frame(card, bg=CARD)
contra_fila.pack(fill="x", padx=28, pady=(6,12))

txt_contrasenia=tk.Entry(contra_fila,font=("Arial",12,"bold"), 
                         bg=CARD,fg=TEXT,show="*", relief="flat")
txt_contrasenia.pack(side="left",fill="x",expand=True, ipady=7)

btn_mostrar_contrasenia=tk.Button(contra_fila, text="Mostrar",
                                  command=toogle_password,
                                  font=("Arial",9), bg=CARD, fg=MUTED,
                                  activebackground=ACCENT, activeforeground=TEXT,
                                  bd=0,cursor="hand2")
btn_mostrar_contrasenia.pack(side="left",padx=(10,0))

#boton login
btn_login = tk.Button(card, text="Ingresar",command=on_login, font=("Arial",12),
                      bg=ACCENT, fg="white", activebackground=ACCENT,
                        activeforeground="white", cursor="hand")

btn_login.pack(fill="x", padx=28, pady=(8,10), ipady=8)


root.bind("<Return>", lambda e: on_login())
txt_user.focus()
root.mainloop()