class Menu:
    def __init__(self, game):
        self.game = game
        self.current_selection = 0
        self.options = ["Jouer", "Quitter"]

    def render(self, screen):
        screen.set_title("Menu Principal")
        screen.set_message("Bienvenue dans DBS-Pattern!")
        screen.set_selections(self.options)
        screen.current_selection = self.current_selection
        screen.render()

    def handle_input(self, key):
        if key == 'KEY_UP':
            self.current_selection = (self.current_selection - 1) % len(self.options)
        elif key == 'KEY_DOWN':
            self.current_selection = (self.current_selection + 1) % len(self.options)
        elif key == 'KEY_ENTER':
            if self.current_selection == 0:  # Jouer
                from game.team_creation import TeamCreation
                self.game.change_state(TeamCreation(self.game))
            elif self.current_selection == 1:  # Quitter
                self.game.run = False
        elif key in ['1', '2']:
            index = int(key) - 1
            if 0 <= index < len(self.options):
                self.current_selection = index
                self.handle_input('KEY_ENTER')