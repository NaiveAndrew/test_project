class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance
        self.city=city

    def __str__(self):
        return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''

customer_1 = Customers('Иван', 'Петров', 'Москва', 50)
print(customer_1)
