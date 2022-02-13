from deck import Card, Deck
import unittest


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """should return string in format '{value} of {suit}'"""
        self.assertEqual(repr(self.card), 'A of Hearts')


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """deck should be a list with 52 instances of Card"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck), 52)

    def test_count(self):
        """count method should return amount of Card instances in deck"""
        self.assertEqual(self.deck.count(), len(self.deck))

    def test_repr(self):
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_deal(self):
        self.assertEqual(len(self.deck._deal(5)), 5)
        self.deck._deal(47)
        self.assertEqual(self.deck._deal(1))


if __name__ == '__main__':
    unittest.main()
