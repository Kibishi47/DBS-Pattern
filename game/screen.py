import os
import readchar
from managers.observer import Observer

class Screen:
    def __init__(self):
        self.title = ""
        self.selections = []
        self.message = ""
        self.battle_info = ""
        self.current_selection = 0
        self.in_battle = False
        Observer.get_instance().attach(self)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def set_title(self, title):
        self.title = title

    def set_selections(self, selections):
        self.selections = selections

    def set_message(self, message):
        self.message = message

    def update(self, message):
        if message == "clear":
            self.battle_info = ""
            return
        last_messages = self.battle_info.split("\n")
        messages = last_messages + [message]
        while len(messages) > 3:
            messages.pop()
        self.battle_info = "\n".join(messages)

    def render(self):
        self.clear()
        print(f"=== {self.title} ===\n")
        if self.message:
            print(f"{self.message}\n")
        for i, selection in enumerate(self.selections):
            if i == self.current_selection:
                print(f"> {selection}")
            else:
                print(f"  {selection}")
        if self.in_battle:
            print("\n=== Logs du combat ===")
            print(f"{self.battle_info}")
        print("\nUtilisez les flèches pour naviguer, Entrée pour sélectionner, Q pour quitter")

    def get_input(self):
        key = readchar.readkey()
        if key == readchar.key.UP:
            return 'KEY_UP'
        elif key == readchar.key.DOWN:
            return 'KEY_DOWN'
        elif key == readchar.key.LEFT:
            return 'KEY_LEFT'
        elif key == readchar.key.RIGHT:
            return 'KEY_RIGHT'
        elif key == readchar.key.ENTER:
            return 'KEY_ENTER'
        elif key.lower() == 'q':
            return 'q'
        else:
            return key