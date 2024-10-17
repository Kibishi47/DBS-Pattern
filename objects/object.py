class Object:
    def __init__(self):
        self.name = "name"
        self.speed = 0

        self.energy_cost = 0
        self.stamina_cost = 0
        self.life_cost = 0
        self.shield_cost = 0
        self.force_cost = 0
        self.speed_cost = 0

        self.energy_damage = 0
        self.stamina_damage = 0
        self.life_damage = 0
        self.shield_damage = 0
        self.force_damage = 0
        self.speed_damage = 0

        self.race_specifications = []

    def use(self, user, target):
        print(f"L'objet {self.name} est utilisé")

class PowerPole(Object):
    def __init__(self):
        super().__init__()
        self.name = "Power Pole"
        self.speed = 70  # Relativement rapide à utiliser
        self.energy_cost = 0
        self.stamina_cost = 10
        self.life_cost = 0
        self.shield_cost = 0
        self.force_cost = 0
        self.speed_cost = 0

        self.energy_damage = 0
        self.stamina_damage = 0
        self.life_damage = 40  # Inflige des dégâts physiques
        self.shield_damage = 20  # Peut percer légèrement les boucliers
        self.force_damage = 0
        self.speed_damage = 0

        self.race_specifications = ["Saiyan", "Android"]

class SenzuBean(Object):
    def __init__(self):
        super().__init__()
        self.name = "Senzu Bean"
        self.speed = 100  # Utilisable instantanément
        self.energy_cost = -100  # Restaure entièrement l'énergie
        self.stamina_cost = -100  # Restaure entièrement la stamina
        self.life_cost = -100  # Restaure complètement la vie
        self.shield_cost = 0
        self.force_cost = 0
        self.speed_cost = 0

        self.energy_damage = 0
        self.stamina_damage = 0
        self.life_damage = 0
        self.shield_damage = 0
        self.force_damage = 0
        self.speed_damage = 0

        self.race_specifications = []  # Accessible à toutes les races

class KintoUn(Object):
    def __init__(self):
        super().__init__()
        self.name = "Kinto-un"
        self.speed = 150  # Très rapide
        self.energy_cost = 5  # Nécessite un peu d'énergie pour être utilisé
        self.stamina_cost = 0
        self.life_cost = 0
        self.shield_cost = 0
        self.force_cost = 0
        self.speed_cost = 0

        self.energy_damage = 0
        self.stamina_damage = 0
        self.life_damage = 0
        self.shield_damage = 0
        self.force_damage = 0
        self.speed_damage = -50  # Augmente la vitesse d'esquive

        self.race_specifications = ["Saiyan", "Namekian"]

class DragonBall(Object):
    def __init__(self):
        super().__init__()
        self.name = "Dragon Ball"
        self.speed = 0  # Ne confère pas de bonus direct en combat
        self.energy_cost = 0
        self.stamina_cost = 0
        self.life_cost = 0
        self.shield_cost = 0
        self.force_cost = 0
        self.speed_cost = 0

        self.energy_damage = 0
        self.stamina_damage = 0
        self.life_damage = 0
        self.shield_damage = 0
        self.force_damage = 0
        self.speed_damage = 0

        self.race_specifications = []  # Peut être utilisé par toutes les races, mais utilisé pour une quête