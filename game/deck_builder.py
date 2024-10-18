from attacks.attack_factory import AttackFactory
from entities.deck.card_factory import CardFactory
from entities.deck.deck_builder import DeckBuilder
from managers.deck_manager import DeckManager
from objects.object_factory import ObjectFactory

class GameDeckBuilder:
    def __init__(self, game):
        self.game = game
        self.deck_builder = DeckBuilder()
        self.categories = ["Attack", "Object"]
        self.current_category_index = 0
        self.current_card_index = 0
        self.available_cards = self.get_available_cards()
        self.state = "selecting_card"
        self.current_selection = 0
        self.menu_selection = 0

    def get_available_cards(self):
        if self.categories[self.current_category_index] == "Attack":
            return [CardFactory.create_card(AttackFactory.create_attack(attack_name)) for attack_name in AttackFactory.attacks.keys()]
        else:
            return [CardFactory.create_card(ObjectFactory.create_object(object_name)) for object_name in ObjectFactory.objects.keys()]

    def render(self, screen):
        if self.state == "selecting_card":
            self.render_card_selection(screen)
        elif self.state == "selecting_quantity":
            self.render_quantity_selection(screen)

    def render_card_selection(self, screen):
        screen.set_title("Construction du Deck")
        
        categories_display = " | ".join(
            f"[{cat}]" if i == self.current_category_index else cat
            for i, cat in enumerate(self.categories)
        )
        
        current_card = self.available_cards[self.current_card_index]
        
        screen.set_message(f"Catégories: {categories_display}\n"
                           f"Carte: {current_card.get_name()} ({self.deck_builder.get_card_number(current_card)}/{current_card.unique_quantity})\n"
                           f"Cartes dans le deck: {self.deck_builder.get_card_number()}/{DeckManager.max_card_amount}\n\n"
                           f"Instructions:\n"
                           f"- Utilisez les flèches GAUCHE/DROITE pour changer de catégorie\n"
                           f"- Utilisez les flèches HAUT/BAS pour naviguer entre les cartes et les options\n"
                           f"- Appuyez sur ENTRÉE pour sélectionner une carte, ajuster sa quantité ou valider le deck\n"
                           f"- Sélectionnez 'Valider le deck' quand vous avez {DeckManager.max_card_amount} cartes")
        
        selections = ["Sélectionner cette carte"]
        if self.deck_builder.get_card_number() == DeckManager.max_card_amount:
            selections.append("Valider le deck")
        
        screen.set_selections(selections)
        screen.current_selection = self.menu_selection
        screen.render()

    def render_quantity_selection(self, screen):
        current_card = self.available_cards[self.current_card_index]
        
        screen.set_title(f"Sélection de la quantité - {current_card.get_name()}")
        screen.set_message(f"Quantité actuelle: {self.deck_builder.get_card_number(current_card)}\n"
                           f"Cartes dans le deck: {self.deck_builder.get_card_number()}/{DeckManager.max_card_amount}\n\n"
                           f"Instructions:\n"
                           f"- Utilisez la flèche HAUT pour augmenter la quantité\n"
                           f"- Utilisez la flèche BAS pour diminuer la quantité\n"
                           f"- Appuyez sur ENTRÉE pour confirmer et revenir à la sélection des cartes")
        screen.set_selections(["Confirmer la quantité"])
        screen.current_selection = 0
        screen.render()

    def handle_input(self, key):
        if self.state == "selecting_card":
            self.handle_card_selection_input(key)
        elif self.state == "selecting_quantity":
            self.handle_quantity_selection_input(key)

    def handle_card_selection_input(self, key):
        if key == 'KEY_LEFT':
            self.current_category_index = (self.current_category_index - 1) % len(self.categories)
            self.available_cards = self.get_available_cards()
            self.current_card_index = 0
            self.menu_selection = 0
        elif key == 'KEY_RIGHT':
            self.current_category_index = (self.current_category_index + 1) % len(self.categories)
            self.available_cards = self.get_available_cards()
            self.current_card_index = 0
            self.menu_selection = 0
        elif key == 'KEY_UP':
            if self.menu_selection > 0:
                self.menu_selection -= 1
            else:
                self.current_card_index = (self.current_card_index - 1) % len(self.available_cards)
        elif key == 'KEY_DOWN':
            if self.menu_selection < len(self.get_current_selections()) - 1:
                self.menu_selection += 1
            else:
                self.current_card_index = (self.current_card_index + 1) % len(self.available_cards)
                self.menu_selection = 0
        elif key == 'KEY_ENTER':
            if self.menu_selection == 0:  # Sélectionner cette carte
                self.state = "selecting_quantity"
            elif self.menu_selection == 1 and self.deck_builder.get_card_number() == DeckManager.max_card_amount:  # Valider le deck
                self.validate_deck()
        elif key in ['1', '2']:
            self.menu_selection = int(key) - 1
            if key == '1':
                self.state = "selecting_quantity"
            elif key == '2' and self.deck_builder.get_card_number() == DeckManager.max_card_amount:
                self.validate_deck()

    # def handle_quantity_selection_input(self, key):
    #     current_card = self.available_cards[self.current_card_index]
    #     if key == 'KEY_UP':
    #         if self.deck_builder.get_card_number(current_card) < current_card.unique_quantity and self.deck_builder.get_card_number() < DeckManager.max_card_amount:
    #             self.deck_builder.add_card(current_card)
    #         elif self.deck_builder.get_card_number() == DeckManager.max_card_amount:
    #             # Si le deck est plein, on retire une autre carte pour ajouter celle-ci
    #             for card in self.deck_builder.deck.cards:
    #                 if card.get_name() != current_card.get_name():
    #                     self.deck_builder.removeCard(card)
    #                     self.deck_builder.add_card(current_card)
    #                     break
    #     elif key == 'KEY_DOWN':
    #         if self.deck_builder.get_card_number(current_card) > 0:
    #             self.deck_builder.removeCard(current_card)
    #     elif key == 'KEY_ENTER' or key == '1':
    #         self.state = "selecting_card"
    #         self.menu_selection = 0

    def validate_deck(self):
        if self.deck_builder.get_card_number() == DeckManager.max_card_amount:
            from game.game import Game
            DeckManager.get_instance("player").set_deck(self.deck_builder.build())
            self.game.change_state(Game(self.game))
        else:
            print(f"Le deck doit contenir exactement {DeckManager.max_card_amount} cartes pour être validé.")

    def get_current_selections(self):
        selections = ["Sélectionner cette carte"]
        if self.deck_builder.get_card_number() == DeckManager.max_card_amount:
            selections.append("Valider le deck")
        return selections

    def handle_quantity_selection_input(self, key):
        current_card = self.available_cards[self.current_card_index]
        if key == 'KEY_UP':
            if self.can_add_card(current_card):
                self.deck_builder.add_card(current_card)
        elif key == 'KEY_DOWN':
            if self.deck_builder.get_card_number(current_card) > 0:
                self.deck_builder.removeCard(current_card)
        elif key == 'KEY_ENTER' or key == '1':
            self.state = "selecting_card"
            self.menu_selection = 0

    def can_add_card(self, card):
        return (self.deck_builder.get_card_number() < DeckManager.max_card_amount and 
                self.deck_builder.get_card_number(card) < card.unique_quantity)