import random


class Enemy:
    def __init__(self):
        self.player_instance = "enemy"
        self.set_warriors()
        self.set_deck()
        

    def set_warriors(self):
        from managers.team_manager import TeamManager
        from entities.warrior.warrior import Warrior
        from races.race import Race
        for i in range(TeamManager.max_warrior):
            warrior = Warrior(f"Enemy {i+1}", random.choice(Race.races))
            TeamManager.get_instance(self.player_instance).set_warrior(warrior)

    def set_deck(self):
        from attacks.attack_factory import AttackFactory
        from objects.object_factory import ObjectFactory
        from entities.deck.card_factory import CardFactory
        from entities.deck.deck_builder import DeckBuilder
        from managers.deck_manager import DeckManager
        attack_cards = [CardFactory.create_card(AttackFactory.create_attack(attack_name)) for attack_name in AttackFactory.attacks.keys()]
        object_cards = [CardFactory.create_card(ObjectFactory.create_object(object_name)) for object_name in ObjectFactory.objects.keys()]
        cards = attack_cards + object_cards
        deck_builder = DeckBuilder()
        while(deck_builder.get_card_number() < DeckManager.max_card_amount):
            card = random.choice(cards)
            if deck_builder.get_card_number(card) < card.unique_quantity:
                deck_builder.add_card(card)
        DeckManager.get_instance(self.player_instance).set_deck(deck_builder.build())

    def choose_card(self):
        from managers.team_manager import TeamManager
        from managers.hand_manager import HandManager
        warrior = TeamManager.get_instance(self.player_instance).get_active_warrior()
        hand = HandManager.get_instance(self.player_instance).get_hand()
        valid_cards = list(filter(lambda card: card.get_energy_cost() <= warrior.get_energy(), hand.cards))
        if len(valid_cards) == 0:
            return None
        return random.choice(valid_cards)