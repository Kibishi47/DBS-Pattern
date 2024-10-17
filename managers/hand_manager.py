from typing import TypeVar, Type
from entities.deck.hand import Hand

T = TypeVar('T', bound='HandManager')

class HandManager:
    _instances = {}

    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.hand = Hand()

    @classmethod
    def get_instance(cls: Type[T], key) -> T:
        if key not in cls._instances:
            cls._instances[key] = cls(key)
        return cls._instances[key]

    def add_card(self, card):
        if card is not None:
            self.hand.add_card(card)

    def remove_card(self, card):
        self.hand.remove_card(card)

    def get_hand(self):
        return self.hand