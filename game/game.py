from managers.team_manager import TeamManager
from managers.deck_manager import DeckManager
from managers.hand_manager import HandManager
from managers.battle_manager import BattleManager
from game.enemy import Enemy

class Game:
    def __init__(self, game):
        self.game = game
        self.battle_manager = BattleManager.get_instance()
        self.team_manager = TeamManager.get_instance("player")
        self.deck_manager = DeckManager.get_instance("player")
        self.hand_manager = HandManager.get_instance("player")
        self.enemy = Enemy()
        self.turn = 0
        self.current_selection = 0
        self.battle_manager.init_game()

    def render(self, screen):
        active_warrior = self.team_manager.get_active_warrior()
        enemy_warrior = TeamManager.get_instance("enemy").get_active_warrior()
        
        screen.set_title(f"Combat - Tour {self.turn + 1}")
        
        hand_cards = self.hand_manager.get_hand().cards
        card_info = "\n".join([f"{i+1}. {card.get_complete_name()} (Coût: {card.get_energy_cost()} énergie)" for i, card in enumerate(hand_cards)])
        
        screen.set_message(f"Joueur: {active_warrior.get_name()} - Vie: {active_warrior.get_life()} - Énergie: {active_warrior.get_energy()}\n"
                           f"Ennemi: {enemy_warrior.get_name()} - Vie: {enemy_warrior.get_life()} - Énergie: {enemy_warrior.get_energy()}\n\n"
                           f"Cartes en main:\n{card_info}")
        
        selections = [f"Utiliser {card.get_complete_name()}" for card in hand_cards]
        selections.append("Passer le tour")
        
        screen.set_selections(selections)
        screen.current_selection = self.current_selection
        screen.render()

    def handle_input(self, key):
        num_options = len(self.hand_manager.get_hand().cards) + 1
        if key == 'KEY_UP':
            self.current_selection = (self.current_selection - 1) % num_options
        elif key == 'KEY_DOWN':
            self.current_selection = (self.current_selection + 1) % num_options
        elif key == 'KEY_ENTER':
            self.play_turn(self.current_selection)
        elif key.isdigit():
            index = int(key) - 1
            if 0 <= index < num_options:
                self.play_turn(index)

    def play_turn(self, player_card_index):
        hand_cards = self.hand_manager.get_hand().cards
        is_pass_turn = player_card_index == len(hand_cards)
        player_card = None if is_pass_turn else hand_cards[player_card_index]
        enemy_card = self.enemy.choose_card()

        cards_by_player_instance = []
        if player_card:
            if self.team_manager.get_active_warrior().get_energy() >= player_card.get_energy_cost():
                cards_by_player_instance.append((player_card, "player"))
            else:
                print("Pas assez d'énergie pour jouer cette carte.")
                return
            
        if enemy_card:
            cards_by_player_instance.append((enemy_card, "enemy"))

        self.battle_manager.select_cards(cards_by_player_instance)
        
        self.turn += 1
        self.battle_manager.new_turn()
        self.check_game_state()

    def check_game_state(self):
        player_warrior = self.team_manager.get_active_warrior()
        enemy_warrior = TeamManager.get_instance("enemy").get_active_warrior()

        if player_warrior.get_life() <= 0:
            self.team_manager.remove_warrior(player_warrior)
            if not self.team_manager.get_warriors():
                self.game_over("Défaite")
            else:
                self.team_manager.set_active_warrior(self.team_manager.get_warriors()[0])

        if enemy_warrior.get_life() <= 0:
            enemy_team = TeamManager.get_instance("enemy")
            enemy_team.remove_warrior(enemy_warrior)
            if not enemy_team.get_warriors():
                self.game_over("Victoire")
            else:
                enemy_team.set_active_warrior(enemy_team.get_warriors()[0])

    def game_over(self, result):
        from game.menu import Menu
        print(f"Fin de la partie : {result}")
        self.game.change_state(Menu(self.game))