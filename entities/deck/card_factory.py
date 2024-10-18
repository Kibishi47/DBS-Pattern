from entities.deck.card import Card, AttackCard, ObjectCard, TransformationCard

class CardFactory:
    cards = {
        "Attack": AttackCard,
        "Object": ObjectCard,
        "TransformationState": TransformationCard
    }

    id = 0

    @classmethod
    def create_card(cls, type_class) -> Card:
        cls.id += 1
        class_name = type_class.__class__.__bases__[0].__name__
        return cls.cards.get(class_name, None)(cls.id, type_class)