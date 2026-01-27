import tkinter 
from tkinter import messagebox

num1 = None
op = None

def click_boton(valor):
    pantalla.insert(tkinter.END, valor)

def operacion(simbolo):
    global num1, op
    num1 = float(pantalla.get())
    op = simbolo
    pantalla.delete(0, tkinter.END)

def limpiar():
    pantalla.delete(0, tkinter.END)

def igual():
    global num1, op
    num2 = float(pantalla.get())
    pantalla.delete(0, tkinter.END)
    if op == "+":
        resultado = num1 + num2
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    elif op == "/":
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir por cero")
            return
        resultado = num1 / num2

    pantalla.insert(tkinter.END, str(resultado))

root = tkinter.Tk()
root.title("Calculadora Simple")
root.geometry("330x250")
pantalla = tkinter.Entry(root, width=18,font=("Arial",18), justify="center")
pantalla.grid(row=0,column=0,columnspan=4, padx=5, pady=5)

numeros = [
    ('7',1,0), ('8',1,1), ('9',1,2),  
    ('4',2,0), ('5',2,1), ('6',2,2),   
    ('1',3,0), ('2',3,1), ('3',3,2),  
    ('0',4,0)                        
]

for numero, fila, colmna in numeros:
    tkinter.Button(root,text=numero,width=5,height=2, command=lambda x= numero: click_boton(x)).grid(row=fila,column=colmna, padx=2, pady=2)
#crear los botones de las operaciones
tkinter.Button(root, text='+', width=3, height=2, command=lambda:operacion("+")).grid(row=1, column=3, padx=2, pady=2)
tkinter.Button(root, text='-', width=3, height=2, command=lambda:operacion("-")).grid(row=2, column=3, padx=2, pady=2)
tkinter.Button(root, text='*', width=3, height=2, command=lambda:operacion("*")).grid(row=3, column=3, padx=2, pady=2)
tkinter.Button(root, text='/', width=3, height=2, command=lambda:operacion("/")).grid(row=4, column=3, padx=2, pady=2)
#igual y limpiar
tkinter.Button(root, text='=', width=3, height=2, command=igual).grid(row=4, column=1, padx=2, pady=2)
tkinter.Button(root, text='C', width=3, height=2, command=limpiar).grid(row=4, column=2, padx=2, pady=2)

root.mainloop()