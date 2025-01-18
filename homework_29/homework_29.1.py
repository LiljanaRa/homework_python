class Rectangle:
    def __init__(self, width, heihgt):
        self.width = width
        self.height = heihgt

    def calculate_area(self):
        return f"Площадь прямоугольника равна: {self.width * self.height:.2f}"

rectangles = [
Rectangle(5.6, 6.9),
Rectangle(8.1, 5.6),
Rectangle(3.2, 1.4),
Rectangle(7.9, 13.1),
Rectangle(1.7, 2.3),
Rectangle(6.3, 3.8),
Rectangle(2.5, 9.5),
Rectangle(4.8, 8.0),
Rectangle(9.4, 4.2),
Rectangle(15.0, 7.7),
]

for rectangle in rectangles:
    print(rectangle.calculate_area())
