import carrito as c

class Usuario:
    def __init__(self, identificador):
        self.id = identificador
    
    def crear_carrito(self):
        self.carrito = c.CarritoDeCompra()
        return True
    
    def agregar_al_carrito(self, producto, cantidad):
        return self.carrito.add_product(producto, cantidad)

    def calcular_total_carrito(self):
        return self.carrito.calcular_total()