from random import shuffle


class Deck:
    def __init__(self):
        self._cards = ["A", *range(2, 11), "J", "Q", "K"] * 4

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, collection: list):
        self._cards = collection

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        return f"Deck with {len(self)} cards"

    def shuffle(self):
        shuffle(self._cards)

    def deal(self, amount: int = 1):
        stack = []
        for num in range(0, amount):
            stack.append(self._cards.pop())
        return stack
