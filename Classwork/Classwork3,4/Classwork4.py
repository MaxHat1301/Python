class Car:
    def __init__(self, amount=4):  # параметр по умолчанию
        self.amount = amount

    def printer(self):  # метод!!
        print(self.amount)


wheels = Car()
karcas = Car(amount=1)
wheels.printer()
karcas.printer()