from abc import ABC, abstractmethod

class GameCharacter:
    @abstractmethod
    def atack(selfself):
       pass

class Warrior(GameCharacter):
    def atack(self):
        return "Удар"

class Mage(GameCharacter):
    def atack(self):
        return "Выстрел"

W = Warrior()
M = Mage()
print(W.atack())
print(M.atack())