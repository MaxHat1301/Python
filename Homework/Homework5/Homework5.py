class Character:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__energy = 50
        self.__weapon = None

    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
            print(f"{self.name} атакует.")
        else:
            print("Недостаточно энергии")

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            print(f"Персонаж погиб.")
            self.__health = 0
        else:
            print(f"{self.name} получил {damage} урона. Здоровье: {self.__health}")

    def equip_weapon(self, weapon):
        self.__weapon = weapon
        print(f"{self.name} взял {weapon}.")

    def get_status(self):
        return f"Здоровье: {self.__health}, Энергия: {self.__energy}, Оружие: {self.__weapon or 'нет'}"

h = Character("Герой")
