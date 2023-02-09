# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f'{self.x}, {self.y}, {self.width}, {self.height}'
#     def area(self):
#         return self.width*self.height
# r_1 = Rectangle(5, 10, 50, 100)
# print(r_1)
# print(r_1.area())

class Klient:
    def __init__(self, name="One", surname="One", city="None", balance=0):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'
    def get_info(self):
        return f'{self.name} {self.surname}. {self.city}.'
ivan = Klient('Иван','Петров','Москва',50)
vladimir = Klient('Владимир','Зайцев','Кострома',50)
olesya = Klient('Олеся','Янина','Новосибирск',50)
klient_list = [ivan, vladimir, olesya]
for i in klient_list:
    print(i.get_info())

