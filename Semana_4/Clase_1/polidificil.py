from abc import ABC, abstractmethod
class Descuento(ABC):
    @abstractmethod
    def aplicar(self, subtotal:float) ->float:
        pass

class SinDescuento(Descuento):
    def aplicar(self, subtotal:float) ->float:
        return subtotal
    
class DescuentoPorcentaje(Descuento):
    def __init__(self, porcentaje:float):
        self.porcentaje = porcentaje

    def aplicar(self, subtotal:float) ->float:
        return subtotal * (1 - self.porcentaje / 100)
    
class DescuentoFijo(Descuento):
    def __init__(self, monto:float):
        self.monto = monto

    def aplicar(self, subtotal:float) ->float:
        return max(0, subtotal - self.monto)
    

class CarritoDeCompras:
    def __init__(self, descuento:Descuento):
        self.descuento = descuento
        self.items = []
    
    def agregar_item(self, nombre:str, precio:float):
        self.items.append((nombre, precio))

    def calcular_total(self) ->float:
        subtotal = sum(precio for nombre, precio in self.items)
        total_con_descuento = self.descuento.aplicar(subtotal)
        return total_con_descuento

#sin descuento
carrito1 = CarritoDeCompras(SinDescuento())
carrito1.agregar_item("Camisa", 50)
carrito1.agregar_item("Pantalones", 80)
print("Total sin descuento:", carrito1.calcular_total())

#con descuento por porcentaje
carrito2 = CarritoDeCompras(DescuentoPorcentaje(10))
carrito2.agregar_item("Camisa", 50) 
carrito2.agregar_item("Pantalones", 80)
print("Total con descuento por porcentaje:", carrito2.calcular_total())

#con descuento fijo
carrito3 = CarritoDeCompras(DescuentoFijo(20))
carrito3.agregar_item("Camisa", 50)
carrito3.agregar_item("Pantalones", 80)
print("Total con descuento fijo:", carrito3.calcular_total())