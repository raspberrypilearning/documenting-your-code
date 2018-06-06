import random

class Card:
    """
    The Card class represents a single playing card and is initialised by passing a suit and number.

    A card is initialised using::

        ace_of_spades = Card("spades", "A")
    
    """
    def __init__(self, suit, number):

        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """
        Returns or sets the suit (hearts, clubs, diamonds, spades) of the Card

        :returns: the card suit as a `string`
        """
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """ 
        Returns or sets the number ("2"-"10", "J", "Q", "K", "A") of the Card 

        :returns: the card number as a `string`
        """
        return self._number

    @number.setter
    def number(self, number):
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:
    """
    The Deck class represents a deck of playing cards in an order.
    """
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):
        """
        Populates (resets) the deck of cards with all 52 cards in the order 
        2-10, J, Q, K, A, hearts, clubs, diamonds, spades.
        """
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        """
        Shuffles the deck into a random order of playing cards.
        """
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """
        Deals (and removes) a number of cards from the deck.

        :returns: `list of Card objects`
        """
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"
        
deck = Deck()
print(deck)
