from entities.deck.deck import Deck
from entities.deck.card_factory import CardFactory
from managers.deck_manager import DeckManager
    
class DeckBuilder:
    def __init__(self):
        self.deck = Deck()

    def add_card(self, card):
        if self.get_card_number() < DeckManager.max_card_amount and self.get_card_number(card) < card.unique_quantity:
            self.deck.add_card(card)

    def removeCard(self, card):
        self.deck.remove_card(card)

    def get_card_number(self, card=None):
        return self.deck.get_card_number(card)

    def build(self):
        return self.deck