class Doctor:
    def __init__(self, name):
        self.name = name

class Pacient:
    def __init__(self, name):
        self.name = name

    def introduce_doctor(self, doctor1):
        print(f"My doctor is - {doctor1.name}")

doctor1 = Doctor("Mr. Ivanov")
pacient1 = Pacient("Petya")
pacient1.introduce_doctor(doctor1)