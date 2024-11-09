class Product:
    def __init__(self, my_name, my_price, my_number):
        self.name = my_name
        self.price = my_price 
        self.number = my_number

    def actualizar_precio(self, new_price):
        if new_price < 0:
            return False
        self.price = new_price
        return True 

    def actualizar_stock(self, new_stock):
        if new_stock < 0:
            return False
        self.price = new_stock
        return True 
    

