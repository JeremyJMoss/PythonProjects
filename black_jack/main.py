from deck import Deck
from player import Player
from computer import Computer


def final_statements(statement):
    print(f"Your final cards: {player.hand}")
    print(f"Your score: {player.score}")
    print(f"Computer's cards: {computer.hand}")
    print(f"Computer's score: {computer.score}")
    print(statement)


deck = Deck()
player = Player()
computer = Computer()
deck.shuffle()
player.add_cards(deck.deal(2))
computer.add_cards(deck.deal(2))
should_continue = True
state = None
print("Let's Play Black Jack")
while should_continue:
    print(f"Your cards: {player.hand}")
    print(f"Computer's first card: {computer.hand[0]}")
    if player.is_blackjack() and computer.is_blackjack():
        state = "What a coincidence. You both got Black Jack. It's a very rare draw."
        break
    elif computer.is_blackjack():
        state = "You lose. Computer got Black Jack."
        break
    elif player.is_blackjack():
        state = "You win! You got Black Jack!"
        break
    elif computer.score > 21 and player.score > 21:
        state = "Both went over. It's a draw."
        break
    elif computer.score > 21:
        state = "Computer has gone over. You win!"
        break
    elif player.score > 21:
        state = "You went over. You lose"
        break
    while True:
        another_card = input("Would you like another card? (yes/no)\n")
        if another_card == "yes":
            player.add_cards(deck.deal())
            if computer.should_deal():
                computer.add_cards(deck.deal())
            break
        elif another_card == "no":
            should_continue = False
            break
if state is None:
    if player.score > computer.score:
        state = "Your score was the highest. You win!"
    elif player.score < computer.score:
        state = "Computer scored the most. You lose."
    else:
        state = "It's a draw."
final_statements(state)
