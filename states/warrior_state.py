class WarriorState:
    def attack(self, target, damage):
        pass

class NormalState(WarriorState):
    def attack(self, target, damage):
        target.health -= damage
        print(f"Attaque réussie, {target.name} perd {damage} points de vie.")

class InjuredState(WarriorState):
    def attack(self, target, damage):
        reduced_damage = damage * 0.75
        target.health -= reduced_damage
        print(f"Attaque réduite, {target.name} perd {reduced_damage} points de vie.")

class StunState(WarriorState):
    def attack(self, target, damage):
        print(f"{target.name} est étourdi et ne peut pas attaquer.")