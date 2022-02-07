from random import shuffle


class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{a} of {b}".format(a=self.value, b=self.suit)


class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {a} cards".format(a=self.count())

    def _deal(self, num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)
