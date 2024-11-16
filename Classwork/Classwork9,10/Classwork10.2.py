class PlayerInventory:
    def __init__(self, items):
        self.__items = items

    def add_item(self, item):
        self.__items += 1
        print("Предмет добавлен")

    def remove_item(self, item):
        if item > 0:
            self.__items -= 1
        else:
            print("же 0 предметов")

    def show_inventory(self):
        return self.__items

I = PlayerInventory(12)
I.add_item(1)
print(I.show_inventory())