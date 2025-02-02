from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        ...


class Rectangle(Shape):

    def area(self):
        rect_area = rectangle.height * rectangle.width
        return f"Площадь прямоугольника равна: {rect_area}"

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return f"Периметр прямоугольника равен: {2 * (self.height + self.width)}"

    def get_figur_info(self):
        return f"########\n#      #\n########\nЭто прямоугольник со сторонами {self.height} и {self.width}"


class Circle(Shape):

    def area(self):
        circle_area = pi * (circle.radius ** 2)
        return f"Площадь круга равна: {circle_area:.2f}"

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return f"Периметр круга равен: {2 * pi * self.radius:.2f}"

    def get_figur_info(self):
        return f"  **\n*    *\n*    *\n  **\nЭто круг с радиусом:  {self.radius}"


rectangle = Rectangle(8, 5)
circle = Circle(5)

print(rectangle.get_figur_info(), rectangle.perimeter(), rectangle.area(), sep='\n')
print(circle.get_figur_info(), circle.perimeter(), circle.area(), sep='\n')