from entities.warrior.warrior import Warrior
from typing import TypeVar, Type

T = TypeVar('T', bound='TeamManager')

class TeamManager:
    _instances = {}

    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.active_warrior = None
        self.warriors = []

    @classmethod
    def get_instance(cls: Type[T], key) -> T:
        if key not in cls._instances:
            cls._instances[key] = cls(key)
        return cls._instances[key]

    def set_warrior(self, warrior):
        if warrior not in self.warriors:
            if len(self.warriors) == 0:
                self.active_warrior = warrior
            self.warriors.append(warrior)
        else:
            print(f"{warrior.get_name()} est déjà dans l'équipe.")
    
    def remove_warrior(self, warrior):
        if warrior in self.warriors:
            self.warriors.remove(warrior)
            print(f"{warrior.get_name()} a été retiré de l'équipe.")
            if self.active_warrior == warrior:
                if len(self.warriors) > 0:
                    self.active_warrior = self.warriors[0]
                else:
                    self.active_warrior = None
        else:
            print(f"{warrior.get_name()} n'est pas dans l'équipe.")

    def get_warriors(self):
        return self.warriors
    
    def set_active_warrior(self, warrior):
        if warrior in self.warriors:
            self.active_warrior = warrior
        else:
            print(f"{warrior.get_name()} n'est pas dans l'équipe.")

    def get_active_warrior(self) -> Warrior:
        return self.active_warrior
    
    def reset(self):
        self.warriors = []
        self.active_warrior = None