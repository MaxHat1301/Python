import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='logs.log',
    filemode='w',
    format="%(levelname)s:%(asctime)s - %(message)s")

logging.info(f'Program started')
class NameSurname:
    def __init__(self, name, surname):
        if(type(name) != str):
            raise TypeError(f"Name is not a string ")
        if(type(surname) != str):
            raise TypeError(f"Surname is not a string '{type(surname) }'")
        self.name = name
        self.surname = surname

class Student:
    student_amount = 0
    def __init__ (self,name, surname , age, height=160):
        self.ns = NameSurname(name, surname)
        self.age = age
        self.height = height
        Student.student_amount += 1
        logging.info(f'Student created: {self.ns.name} {self.ns.surname}')
        logging.info(f'Student info: age = {self.age} height = {self.height}')

    def printStudent(self):
        print(f'Name: {self.ns.name}')
        print(f'Surname: {self.ns.surname}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')

    def Birthday(self):
        self.age += 1
        print(f'Happy Birthday to {self.ns.name}. Now you {self.age}!')

logging.debug(f'Program in progress...')

try:
    first_student = Student("Maxim", "Khatianov", 13)
    second_student = Student("Oleg", True, 12)

except Exception as error:
    print("Next code")
    logging.error(error)

logging.info(f'Program finished')
