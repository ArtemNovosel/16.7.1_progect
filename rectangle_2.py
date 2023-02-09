from rectangle import Rectangle, Square, Circle
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# print((rect_1.get_area()))
# print(rect_2.get_area())
square_1 = Square(5)
square_2 = Square(10)
# print(square_1.get_area())
# print(square_2.get_area())
circle_1 = Circle(10)
circle_2 = Circle(3)
# print(circle_1.get_aria_cirkle())
# print(circle_2.get_aria_cirkle())
figures = [rect_1,rect_2,square_1,square_2, circle_2, circle_1]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area(), 'квадрат')
    elif isinstance(figure, Rectangle):
        print(figure.get_area(), 'прямоугольник')
    else:
        print(figure.get_aria_cirkle(),'круг')
