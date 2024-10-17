class Hand:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def add_card(self, card):
        self.cards.append(card)
        return True
    
    def remove_card(self, card):
        self.cards.remove(card)