from entities.warrior.warrior import Warrior
from races.race import Race
from managers.team_manager import TeamManager

class TeamCreation:
    def __init__(self, game):
        self.game = game
        self.current_warrior = 0
        self.name_input = ""
        self.races = Race.races
        self.selected_race = 0
        self.is_entering_name = False
        self.current_selection = 0

    def render(self, screen):
        if self.is_entering_name:
            screen.set_title(f"Entrez le nom du Guerrier {self.current_warrior + 1}")
            screen.set_message(f"Nom actuel: {self.name_input}\n\nAppuyez sur Entrée pour confirmer le nom")
            screen.set_selections([])
        else:
            screen.set_title(f"Créer Guerrier {self.current_warrior + 1}/{TeamManager.max_warrior}")
            screen.set_message(f"Nom: {self.name_input}\nRace: {self.races[self.selected_race]}")
            screen.set_selections(["Entrer le nom", "Changer de race", "Confirmer le guerrier"])
        
        screen.current_selection = self.current_selection
        screen.render()

    def handle_input(self, key):
        if self.is_entering_name:
            if key == 'KEY_ENTER':
                self.is_entering_name = False
            elif key == '\x7f':  # Backspace
                self.name_input = self.name_input[:-1]
            elif len(key) == 1 and key.isprintable():
                self.name_input += key
        else:
            if key == 'KEY_UP':
                self.current_selection = (self.current_selection - 1) % 3
            elif key == 'KEY_DOWN':
                self.current_selection = (self.current_selection + 1) % 3
            elif key == 'KEY_ENTER':
                self.process_selection()
            elif key in ['1', '2', '3']:
                self.current_selection = int(key) - 1
                self.process_selection()

    def process_selection(self):
        if self.current_selection == 0:  # Entrer le nom
            self.is_entering_name = True
        elif self.current_selection == 1:  # Changer de race
            self.selected_race = (self.selected_race + 1) % len(self.races)
        elif self.current_selection == 2:  # Confirmer le guerrier
            if self.name_input:
                new_warrior = Warrior(self.name_input, self.races[self.selected_race])
                TeamManager.get_instance("player").set_warrior(new_warrior)
                self.current_warrior += 1
                self.name_input = ""
                self.selected_race = 0
                self.current_selection = 0
                if self.current_warrior == TeamManager.max_warrior:
                    from game.deck_builder import GameDeckBuilder
                    self.game.change_state(GameDeckBuilder(self.game))