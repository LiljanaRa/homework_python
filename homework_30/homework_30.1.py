class Rectangle:
    def __init__(self, width = None, height = None):
        self.width = width if width else "N/A"
        self.height = height if height else "N/A"

    def calculate_area(self):
        return f"Площадь прямоугольника равна: {self.width * self.height:.2f}"

    def calculate_perimeter(self):
        return f"Периметр прямоугольника равен: {2 * (self.width + self.height):.2f}"

    def __str__(self):
        return f"Прямоугольнок выглядит так: {"#" * 5}"

    def __repr__(self):
        template = "Rectangle(Width: {}, Height: {})"
        return template.format(self.width, self.height)

rectangle = Rectangle(5.6, 8.1)

print(rectangle)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
print(repr(rectangle))
