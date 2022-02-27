class Player:
    def __init__(self):
        self._hand = []
        self._score = 0

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, collection: list):
        self._hand = collection

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score

    def hand_size(self):
        return len(self._hand)

    def add_cards(self, cards):
        for card in cards:
            self._hand.append(card)
        self.calculate_score()

    def calculate_score(self):
        score = 0
        count = 0
        for card in self._hand:
            if card != "A":
                if card == 'K' or card == 'Q' or card == 'J':
                    score += 10
                else:
                    score += card
            else:
                count += 1
        for ace in range(0, count):
            if count == 1:
                if self.score < 11:
                    score += 11
                else:
                    score += 1
            else:
                score += 1
                count -= 1

        self._score = score

    def is_blackjack(self):
        return self.score == 21 and self.hand_size() == 2




    def __repr__(self):
        return "Player of Black Jack"
