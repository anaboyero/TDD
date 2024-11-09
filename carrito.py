class CarritoDeCompra:
    def __init__(self):
        self.contenido = []
    
    def add_product(self, my_product, my_number):
        if my_number > my_product.number:
            return False 
        self.contenido.append([my_product, my_number])
        return True 
        # Mirar si ya estuviera en el carrito 


    def remove_product(self, my_product):
        for pareja in self.contenido:
            if my_product in pareja:
                self.contenido.remove(pareja)
                return True 
        return False

    
    def calcular_total(self):
        if len(self.contenido) < 1:
            return 0
        amount = 0
        for product, number in self.contenido:
            amount += number*product.price 
        return amount

