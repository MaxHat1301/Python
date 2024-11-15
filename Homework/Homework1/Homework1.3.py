import random

number = random.randint(1, 10)
attempt = 3

print("Я загадав число від 1 до 10. У вас є 3 спроби його вгадати.")

for i in range(attempt):
    guess = int(input("Введіть ваше число: "))

    if guess == number:
        print("Вітаю! Ви вгадали число!")
        break
    elif guess < number:
        print("Більше!")
    else:
        print("Менше!")
