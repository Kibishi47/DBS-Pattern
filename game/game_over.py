# Nouveau fichier: game/game_over_screen.py
class GameOverScreen:
    def __init__(self, game, result):
        self.game = game
        self.result = result
        self.current_selection = 0

    def render(self, screen):
        screen.in_battle = False
        screen.set_title("Fin de la partie")
        
        message = f"{self.result} !"
        if self.result == "Victoire":
            message += "\nFélicitations, vous avez vaincu tous les ennemis !"
        else:
            message += "\nVos guerriers ont été vaincus. Vous aurez une meilleure chance la prochaine fois !"
        
        screen.set_message(message)
        
        selections = ["Retour au menu principal", "Quitter le jeu"]
        screen.set_selections(selections)
        screen.current_selection = self.current_selection
        screen.render()

    def handle_input(self, key):
        if key == 'KEY_UP':
            self.current_selection = (self.current_selection - 1) % 2
        elif key == 'KEY_DOWN':
            self.current_selection = (self.current_selection + 1) % 2
        elif key == 'KEY_ENTER':
            if self.current_selection == 0:
                from game.menu import Menu
                self.game.change_state(Menu(self.game))
            else:
                self.game.quit_game()