from entities.deck.card import Card, AttackCard, ObjectCard

class CardFactory:
    cards = {
        "Attack": AttackCard,
        "Object": ObjectCard
    }

    @classmethod
    def create_card(cls, type_class) -> Card:
        class_name = type_class.__class__.__bases__[0].__name__
        return cls.cards.get(class_name, None)(type_class)