from entities.deck.deck import Deck
from entities.deck.card_factory import CardFactory

class DeckBuilder:
    def __init__(self):
        self.deck = Deck()

    def add_card(self, card):
        return self.deck.add_card(card)
    
    def removeCard(self, card):
        self.deck.remove_card(card)

    def get_card_number(self, card = None):
        return self.deck.get_card_number(card)

    def build(self):
        return self.deck