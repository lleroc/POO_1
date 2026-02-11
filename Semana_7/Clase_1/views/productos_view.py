import tkinter as tk
from tkinter import ttk, messagebox

class producto_view(tk.Tk):
    def __init__(self, controller):
        try:
            super().__init__()
            self.controller = controller
            self.title("CRUD Productos (MVC + Tkinter + MySQL)")
            self.geometry("720x420")
            self.resizable(False, False)

            self.selected_id = None

            self._build_ui()
            self._load_data()
        except Exception as e:
            try:
                messagebox.showerror("Error", f"Error inicializando vista: {e}")
            except Exception:
                pass
            raise
    
    def _build_ui(self):
        try:
            frm = ttk.LabelFrame(self, text="Producto")
            frm.place(x=10, y=10, width=700, height=120)

            ttk.Label(frm, text="Nombre:").place(x=10, y=10)
            self.ent_nombre = ttk.Entry(frm, width=40)
            self.ent_nombre.place(x=80, y=10)

            ttk.Label(frm, text="Precio:").place(x=10, y=45)
            self.ent_precio = ttk.Entry(frm, width=20)
            self.ent_precio.place(x=80, y=45)

            ttk.Label(frm, text="Stock:").place(x=320, y=45)
            self.ent_stock = ttk.Entry(frm, width=20)
            self.ent_stock.place(x=370, y=45)

            btn_crear = ttk.Button(frm, text="Crear", command=self.on_crear)
            btn_crear.place(x=520, y=10, width=150)

            btn_actualizar = ttk.Button(frm, text="Actualizar", command=self.on_actualizar)
            btn_actualizar.place(x=520, y=45, width=150)

            btn_limpiar = ttk.Button(frm, text="Limpiar", command=self.limpiar_form)
            btn_limpiar.place(x=520, y=80, width=150)

            cols = ("id", "nombre", "precio", "stock")
            self.tree = ttk.Treeview(self, columns=cols, show="headings", height=12)
            self.tree.place(x=10, y=140, width=700, height=230)

            self.tree.heading("id", text="ID")
            self.tree.heading("nombre", text="Nombre")
            self.tree.heading("precio", text="Precio")
            self.tree.heading("stock", text="Stock")

            self.tree.column("id", width=60, anchor="center")
            self.tree.column("nombre", width=360, anchor="w")
            self.tree.column("precio", width=120, anchor="e")
            self.tree.column("stock", width=120, anchor="center")

            self.tree.bind("<<TreeviewSelect>>", self.on_select)

            sb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
            self.tree.configure(yscroll=sb.set)
            sb.place(x=690, y=140, height=230)

            btn_eliminar = ttk.Button(self, text="Eliminar seleccionado", command=self.on_eliminar)
            btn_eliminar.place(x=10, y=380, width=200)

            btn_refrescar = ttk.Button(self, text="Refrescar", command=self._load_data)
            btn_refrescar.place(x=220, y=380, width=120)
        except Exception as e:
            raise RuntimeError(f"Error construyendo UI: {e}")
        
    def _load_data(self):
        try:
            try:
                for item in self.tree.get_children():
                    self.tree.delete(item)
            except Exception:
                pass

            rows = self.controller.todos()
            for r in rows:
                try:
                    self.tree.insert("", "end", values=r)
                except Exception:
                    pass
        except Exception as e:
            try:
                messagebox.showerror("Error", f"No se pudo listar: {e}")
            except Exception:
                pass

    def limpiar_form(self):
        try:
            self.selected_id = None
            self.ent_nombre.delete(0, tk.END)
            self.ent_precio.delete(0, tk.END)
            self.ent_stock.delete(0, tk.END)
            try:
                self.tree.selection_remove(self.tree.selection())
            except Exception:
                pass
        except Exception as e:
            try:
                messagebox.showerror("Error", f"Error limpiando formulario: {e}")
            except Exception:
                pass

    def on_select(self, _event):
        try:
            sel = self.tree.selection()
            if not sel:
                return
            values = self.tree.item(sel[0], "values")
            self.selected_id = int(values[0])

            self.ent_nombre.delete(0, tk.END)
            self.ent_nombre.insert(0, values[1])

            self.ent_precio.delete(0, tk.END)
            self.ent_precio.insert(0, values[2])

            self.ent_stock.delete(0, tk.END)
            self.ent_stock.insert(0, values[3])
        except Exception as e:
            try:
                messagebox.showerror("Error", f"Error seleccionando fila: {e}")
            except Exception:
                pass

    def on_crear(self):
        try:
            err = self.controller.insertar(
                self.ent_nombre.get(),
                self.ent_precio.get(),
                self.ent_stock.get(),
            )
            if err:
                messagebox.showwarning("Validación", err)
                return
            self._load_data()
            self.limpiar_form()
            messagebox.showinfo("OK", "Producto creado.")
        except Exception as e:
            try:
                messagebox.showerror("Error", f"Error en crear: {e}")
            except Exception:
                pass

    def on_actualizar(self):
        try:
            err = self.controller.actualizar(
                self.selected_id,
                self.ent_nombre.get(),
                self.ent_precio.get(),
                self.ent_stock.get(),
            )
            if err:
                messagebox.showwarning("Validación", err)
                return
            self._load_data()
            self.limpiar_form()
            messagebox.showinfo("OK", "Producto actualizado.")
        except Exception as e:
            try:
                messagebox.showerror("Error", f"Error en actualizar: {e}")
            except Exception:
                pass

    def on_eliminar(self):
        try:
            if not self.selected_id:
                messagebox.showwarning("Validación", "Selecciona un producto para eliminar.")
                return

            try:
                ok = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar el producto seleccionado?")
            except Exception:
                ok = False

            if not ok:
                return

            err = self.controller.eliminar(self.selected_id)
            if err:
                messagebox.showwarning("Validación", err)
                return

            self._load_data()
            self.limpiar_form()
            messagebox.showinfo("OK", "Producto eliminado.")
        except Exception as e:
            try:
                messagebox.showerror("Error", f"Error en eliminar: {e}")
            except Exception:
                pass
