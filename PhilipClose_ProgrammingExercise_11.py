# Write a program that deals a poker hand of 5 cards. The program should let the player
# choose which cards they want to swap out. Then swap out those cards.

# Import random to be able to use randomizers.
import random

# The Card object is used to create cards that can be put in the players hand.
class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']

    # Initialize properties.
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # This allows the cards to be displayed.
    def display(self):
        return f'{Card.ranks[self.rank]} of {Card.suits[self.suit]}'

# The Deck object is used to create a deck that makes up the player's hand.
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]
        random.shuffle(self.cards)

    # Deal cards.
    def deal(self, num):
            return [self.cards.pop() for _ in range(num)]

# The main function is where the main program takes place. This is responsible for
# calling on functions in the card and deck objects and obtaining data to display.
def main():
    deck = Deck()

    # Give the player 5 cards.
    hand = deck.deal(5)

    #SHOW YOUR HAND!!!
    print("You're cards:")
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card.display()}")

    #Ask user if they want to replace any cards.
    print("\nEnter card numbers to replace (ex: 1 7), or leave blank to keep them.")
    print("Enter the list number, not the card number.")
    swapping = input("\nEnter here: ")
    if swapping.strip():
        try:

            #Convert list to indices and replace cards.
            indices = sorted(set(int(x) - 1 for x in swapping.split() if 0 < int(x) <= 5))
            for i in indices:
                hand[i] = deck.deal(1)[0]
        except ValueError:
            print("Invalid input. No cards were replaced.")

        #SHOW YOUR HAND!!!
        print("\nYour final hand:")
        for card in hand:
            print(card.display())

# Call main function.
main()