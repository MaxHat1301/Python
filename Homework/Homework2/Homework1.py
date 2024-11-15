class Rectangle:
    def init(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimetr(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(f"Площа: {rect.calculate_area()}")
print(f"Перметр: {rect.calculate_perimetr()}")