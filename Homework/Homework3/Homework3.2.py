class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Hero(Character):
    def attack(self, target):
        target.health -= 10
        print(f"{self.name} атакує {target.name} і завдає 10 шкоди!")


class Enemy(Character):
    def attack(self, target):
        target.health -= 5
        print(f"{self.name} атакує {target.name} і завдає 5 шкоди!")


# Приклад використання
h = Hero("Воїн", 100)
e = Enemy("Демон", 50)

h.attack(e)
e.attack(h)

print(f"{h.name} - Здоров'я: {h.health}")
print(f"{e.name} - Здоров'я: {e.health}")
