import sys
from game.menu import Menu
from game.screen import Screen

class DBSPattern:
    def __init__(self):
        self.screen = Screen()
        self.current_state = Menu(self)
        self.run = True

    def run_game(self):
        while self.run:
            self.current_state.render(self.screen)
            key = self.screen.get_input()
            if key == 'q':
                self.run = False
            else:
                self.current_state.handle_input(key)

    def change_state(self, new_state):
        self.screen.in_battle = False
        self.current_state = new_state

if __name__ == "__main__":
    game = DBSPattern()
    game.run_game()