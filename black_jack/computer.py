from player import Player
from random import randint


class Computer(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "Computer controlled Player of Black Jack"

    def should_deal(self):
        num = randint(1, 10)
        if self._score < 11:
            return True
        elif self._score < 13:
            return num >= 3
        elif self._score < 16:
            return num >= 5
        elif self._score < 18:
            return num >= 7
        else:
            return num == 10
