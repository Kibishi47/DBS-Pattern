class Discard:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def add_card(self, card):
        self.cards.append(card)
        return True
    
    def remove_card(self, card):
        cards_to_remove = list(filter(lambda c: card.id == c.id, self.cards))
        if len(cards_to_remove) > 0:
            self.cards.remove(cards_to_remove[0])