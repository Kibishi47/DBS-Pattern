from typing import TypeVar, Type

T = TypeVar('T', bound='DeckManager')

class DeckManager:

    _instances = {}
    max_card_amount = 25

    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.deck = None
        self.original_deck = None

    @classmethod
    def get_instance(cls: Type[T], key) -> T:
        if key not in cls._instances:
            cls._instances[key] = cls(key)
        return cls._instances[key]

    def set_deck(self, deck):
        self.deck = deck
        self.original_deck = deck

    def reset_deck(self):
        self.deck = self.original_deck

    def reset(self):
        self.deck = None
        self.original_deck = None

    def add_card(self, card):
        self.deck.add_card(card)

    def draw(self):
        return self.deck.draw()
    
    def shuffle(self):
        self.deck.shuffle()

    def get_deck(self):
        return self.deck