class Rectangle:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a*self.b
class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, b = a)
        # self.a = a
        # self.b = a
class Circle:
    def __init__(self, a):
        self.a = a
    def get_aria_cirkle(self):
        return self.a**2*3.14