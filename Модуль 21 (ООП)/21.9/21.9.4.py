class Customers:
    def __init__(self, first_name,second_name,city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance
        self.city=city

    def __str__(self):
        return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''

    def get_guest(self):
        return f'{self.first_name} {self.second_name},г. {self.city}'


customer_1 = Customers('Иван','Петров','Москва',50)
customer_2 = Customers('Владимир','Зайцев','Кострома',50)
customer_3 = Customers('Олеся','Янина','Новосибирск',50)

guest_list=[costomer_1,costomer_2,costomer_3]


for guest in guest_list:
    print(guest.get_guest())