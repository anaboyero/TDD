import unittest
import client 
import platform
import company 

class Project_Company_Test(unittest.TestCase):
        
    """ 
    Prueba 1: Crear un cliente con horas de netflix, horas de amazon y horas de hotstar
    Escribe la prueba: Crea una prueba que verifique que un cliente se puede crear correctamente
    """ 
    
    def test_creates_client(self):
        my_client = client.Client(10, 20, 5)
        self.assertEqual(my_client.horas_netflix, 10)
        self.assertEqual(my_client.horas_amazon, 20)
        self.assertEqual(my_client.horas_hotstar, 5)

    """ 
    Prueba 2: Crear una plataforma con atributo de name, price_per_unit and unit_in_hours
    Escribe la prueba: Crea una prueba que verifique que un cliente se puede crear correctamente
    """ 

    def test_creates_platform(self):
        my_platform = platform.Platform('netflix', 10, 10)
        self.assertEqual(my_platform.name, 'netflix')
        self.assertEqual(my_platform.price_per_unit, 10)
        self.assertEqual(my_platform.unit_in_hours, 10)

         
    """
    Prueba 3: Crear la compañía con los siguientes atributos: tres plataformas y varios clientes.
    Escribe la prueba: Crea una prueba que verifique que un cliente se puede crear correctamente
    """ 

    def test_creates_company(self):
        my_company = company.Company()
        my_platform = platform.Platform('hotstar', 1, 5)
        my_company.add_platform(my_platform)
        my_client = client.Client(10, 20, 5)
        my_company.add_client(my_client)
        self.assertEqual(my_company.platforms, [my_platform])
        self.assertEqual(my_company.clients, [my_client])

    def set_up(self):
        """ 
        Creates an instance of a company with platforms 
        """
        my_company = company.Company()
        my_platform1 = platform.Platform('netflix', 10, 10)
        my_platform2 = platform.Platform('amazon', 2, 5)
        my_platform3 = platform.Platform('hotstar', 1, 5)
        my_company.add_platform(my_platform1)
        my_company.add_platform(my_platform2)
        my_company.add_platform(my_platform3)

        return my_company


    # def test_calculate_plan_single_client(self):
        """ It calculates the total amount of a plan whene there is just one client """  
     #   my_company = self.set_up()            
     #   total_amount_answer = my_company.calculate_amount()
     #   self.assertEqual(total_amount_answer, 34) """ 

    
    def test_calculate_plan_concrete_client(self):
        """ 
        It calculates the total amount of a plan for a specific client 
        """
        my_company = self.set_up()    
        my_client1 = client.Client(20, 10, 50)
        my_company.add_client(my_client1)       
        total_amount_answer = my_company.calculate_amount(my_client1)
        self.assertEqual(total_amount_answer, 34)
    
    def test_calculate_plan_concrete_client_with_zero_hours(self):
        """ 
        It calculates the total amount of a plan for a specific client with 0 hours for a platform
        """
        my_company = self.set_up() 
        my_client2 = client.Client(10, 0, 100)
        my_company.add_client(my_client2)          
        total_amount_answer = my_company.calculate_amount(my_company.clients[0])
        self.assertEqual(total_amount_answer, 30)

    def test_calculate_plan_concrete_client_with_zero_hours(self):
        """ 
        It calculates the total amount of a plan for a specific client with not enough hourss to get a unit
        """
        my_company = self.set_up()
        my_client3 = client.Client(10, 2, 0)
        my_company.add_client(my_client3)           
        total_amount_answer = my_company.calculate_amount(my_company.clients[0])
        self.assertEqual(total_amount_answer, 10)
















""" 
        my_company = company.Company()
        my_platform1 = platform.Platform('Netflix', 10, 10)
        my_platform2 = platform.Platform('AmazonPrime', 2, 5)
        my_platform3 = platform.Platform('Hotstar', 1, 5)
        my_company.add_platform(my_platform1)
        my_company.add_platform(my_platform2)
        my_company.add_platform(my_platform3)
        my_client1 = client.Client(10, 20, 5)
        my_client2 = client.Client(30, 10, 15)
        my_company.add_client(my_client1)
        my_company.add_client(my_client2)

        self.assertEqual(my_company.platforms, [my_platform1, my_platform2, my_platform3])
        self.assertEqual(my_company.clients, [my_client1, my_client2])

"""    


""" 
Step 1: Write the basic design and responsibilities of each class

client: it represents a client, with atributes like hours_in_netflix, hours_in_amazon, hours_in_hotstar.
platform: it represents a platform, with atributes like name, price_per_unit and unit_in_hours
company: it represents a platform, with atributes like name, price_per_unit and unit_in_hours 

Step 2: Configurate the test enviroment

Step 3: TDD cycle for each class and funcionality

Para cada clase y funcionalidad, repetimos los pasos de Red (falla), Green (pasa), y Refactor (refactorización). Aquí te muestro cómo sería el flujo:
""" 

