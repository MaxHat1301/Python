class Bicycle:
    def __init__(self, brand="Trek", model="Marine", year=2022):
        self.brand = brand
        self.model = model
        self.year = year

    def get_age(self):
        return 2024 - self.year

Bike = Bicycle()
print(Bike.get_age())
