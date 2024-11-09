import unittest
import carrito as c 
import producto as p
import usuario as u 

class TestCaseTienda (unittest.TestCase):

    def test_create_product(self):
        """ Checks if it creats a product correctly"""
        mi_producto = p.Product("apple", 1, 20)
        self.assertEqual(mi_producto.name, "apple")
        self.assertEqual(mi_producto.price, 1)
        self.assertEqual(mi_producto.number, 20)

    def test_actualizar_precio(self):
        """ Checks if it modifies a product price correctly"""
        mi_producto = p.Product("apple", 1, 20)
        self.assertTrue(mi_producto.actualizar_precio(2))
        self.assertFalse(mi_producto.actualizar_precio(-2))
        self.assertEqual(mi_producto.price, 2)

    def test_actualizarstock(self):
        #Checks if it modifies a stock product correctly
        mi_producto = p.Product("apple", 1, 20)
        self.assertTrue(mi_producto.actualizar_stock(15))
        self.assertFalse(mi_producto.actualizar_stock(-15))
        self.assertEqual(mi_producto.price, 15)


    def test_creates_carrito(self):
        # Checks if it creats a shopping cart correctly"
        mi_carrito = c.CarritoDeCompra()
        self.assertEqual(mi_carrito.contenido, [])

    
    def test_add_product(self):
        # Checks if adds a product to the shopping cart correctly
        manzanas = p.Product("apple", 1, 20)
        bananas = p.Product("banana", 3, 50)
        mi_carrito = c.CarritoDeCompra()
        self.assertTrue(mi_carrito.add_product(manzanas, 3))
        self.assertFalse(mi_carrito.add_product(bananas, 300))
        self.assertEqual(mi_carrito.contenido, [[manzanas, 3]])
        self.assertTrue(mi_carrito.add_product(bananas, 50))
        self.assertEqual(mi_carrito.contenido,  [[manzanas, 3], [bananas, 50]])  

  
    def test_remove_product(self):
        manzanas = p.Product("apple", 1, 20)
        bananas = p.Product("banana", 3, 50)
        mi_carrito = c.CarritoDeCompra()
        mi_carrito.add_product(manzanas, 3)
        self.assertEqual(len(mi_carrito.contenido), 1)
        #self.assertEqual(mi_carrito.contenido, [manzanas, 3])
        self.assertTrue(mi_carrito.remove_product(manzanas))
        self.assertEqual(len(mi_carrito.contenido), 0)
        self.assertFalse(mi_carrito.remove_product(bananas))

    
    def test_calcular_total(self):
        manzanas = p.Product("apple", 1, 20)
        bananas = p.Product("banana", 3, 50)
        mi_carrito = c.CarritoDeCompra()
        mi_carrito.add_product(manzanas, 10)
        mi_carrito.add_product(bananas, 50)
        self.assertEqual(mi_carrito.calcular_total(), 160)
        mi_carrito.remove_product(bananas)
        self.assertEqual(mi_carrito.calcular_total(), 10) 
        mi_carrito.remove_product(manzanas)
        self.assertEqual(mi_carrito.calcular_total(), 0) 
    
    def test_create_user(self):
        mi_usuario = u.Usuario("Marta")
        self.assertEqual(mi_usuario.id, "Marta")

    def test_crear_carrito(self):
        mi_usuario = u.Usuario("Marta")
        self.assertTrue(mi_usuario.crear_carrito())
        self.assertIsInstance(mi_usuario.carrito, c.CarritoDeCompra)
        self.assertEqual(mi_usuario.id, "Marta")
        
    
    def test_agregar_al_carrito(self):
        mi_usuario = u.Usuario("Marta")
        mi_usuario.crear_carrito()
        manzanas = p.Product("apple", 1, 20)
        bananas = p.Product("banana", 3, 50)
        self.assertTrue(mi_usuario.agregar_al_carrito(manzanas, 10))
        self.assertFalse(mi_usuario.agregar_al_carrito(bananas, 60))
        self.assertEqual(len(mi_usuario.carrito.contenido), 1)


    def test_calcular_total_carrito(self):
        mi_usuario = u.Usuario("Marta")
        mi_usuario.crear_carrito()
        manzanas = p.Product("apple", 1, 20)
        bananas = p.Product("banana", 3, 50)
        mi_usuario.agregar_al_carrito(manzanas, 10)
        mi_usuario.agregar_al_carrito(bananas, 50)
        self.assertEqual(mi_usuario.calcular_total_carrito(), 160)







        






        







