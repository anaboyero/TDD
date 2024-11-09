class Company:
    def __init__(self):
        self.platforms = []
        self.clients = []
    
    def add_platform(self, one_platform):
        self.platforms.append(one_platform)
    
    def add_client(self, one_client):
        self.clients.append(one_client)

    """ def calculate_amount(self):
        for cli in self.clients:
            amount = 0
            for platf in self.platforms:
                if platf.name == "netflix":
                    amount += (cli.horas_netflix/platf.unit_in_hours)*platf.price_per_unit
                elif platf.name == "amazon":
                    amount += (cli.horas_amazon/platf.unit_in_hours)*platf.price_per_unit
                else:
                    amount += (cli.horas_hotstar/platf.unit_in_hours)*platf.price_per_unit
            return amount """ 
                    
    def calculate_amount(self, cliente):
        amount = 0
        for platf in self.platforms:
            if platf.name == "netflix":
                if cliente.horas_netflix < platf.unit_in_hours:
                    pass
                else: 
                    amount += (cliente.horas_netflix//platf.unit_in_hours)*platf.price_per_unit

            elif platf.name == "amazon":
                if cliente.horas_amazon < platf.unit_in_hours:
                    pass
                else: 
                    amount += (cliente.horas_amazon//platf.unit_in_hours)*platf.price_per_unit

            else:
                if cliente.horas_hotstar < platf.unit_in_hours:
                        pass
                else: 
                    amount += (cliente.horas_hotstar//platf.unit_in_hours)*platf.price_per_unit
                 
        return amount
