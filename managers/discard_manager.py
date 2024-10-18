from typing import TypeVar, Type
from entities.deck.discard import Discard

T = TypeVar('T', bound='DiscardManager')

class DiscardManager:
    _instances = {}

    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.discard = Discard()

    @classmethod
    def get_instance(cls: Type[T], key) -> T:
        if key not in cls._instances:
            cls._instances[key] = cls(key)
        return cls._instances[key]

    def add_card(self, card):
        if card is not None:
            self.discard.add_card(card)

    def remove_card(self, card):
        self.discard.remove_card(card)

    def get_discard(self):
        return self.discard