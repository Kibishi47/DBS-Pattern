class Attack:
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

class Regeneration(Attack):
    def __init__(self):
        super().__init__()
        self.name = "Regeneration"
        self.speed = 50
        self.energy_cost = 0
        self.life_damage = 0
        self.stamina_damage = -30  # Récupère de la stamina
        self.shield_damage = 0
        self.race_specifications = ["Namekian"]  # Spécifique aux Namekians

class Afterimage(Attack):
    def __init__(self):
        super().__init__()
        self.name = "Afterimage"
        self.speed = 150  # Très rapide
        self.energy_cost = 10
        self.life_damage = 0
        self.stamina_damage = 0
        self.shield_damage = 0
        self.race_specifications = ["Saiyan"]

class Kamehameha(Attack):
    def __init__(self):
        super().__init__()
        self.name = "Kamehameha"
        self.speed = 100
        self.energy_cost = 40  # Très énergivore
        self.life_damage = 80  # Gros dégâts physiques
        self.stamina_damage = 30
        self.shield_damage = 50  # Peut percer les boucliers
        self.race_specifications = ["Saiyan"]

class Blast(Attack):
    def __init__(self):
        super().__init__()
        self.name = "Blast"
        self.speed = 120  # Relativement rapide
        self.energy_cost = 15
        self.life_damage = 40  # Dégâts modérés
        self.stamina_damage = 20
        self.shield_damage = 30
        self.race_specifications = ["Saiyan", "Android"]

class FastPunch(Attack):
    def __init__(self):
        super().__init__()
        self.name = "Fast Punch"
        self.speed = 140  # Très rapide
        self.energy_cost = 5
        self.life_damage = 20  # Dégâts légers
        self.stamina_damage = 10
        self.shield_damage = 5
        self.race_specifications = ["Saiyan", "Android"]

class LoadPunch(Attack):
    def __init__(self):
        super().__init__()
        self.name = "Load Punch"
        self.speed = 60  # Lent
        self.energy_cost = 20
        self.life_damage = 70  # Gros dégâts
        self.stamina_damage = 30
        self.shield_damage = 40
        self.race_specifications = ["Saiyan", "Android"]

class FastKick(Attack):
    def __init__(self):
        super().__init__()
        self.name = "Fast Kick"
        self.speed = 130  # Rapide
        self.energy_cost = 5
        self.life_damage = 25
        self.stamina_damage = 10
        self.shield_damage = 5
        self.race_specifications = ["Saiyan", "Android"]

class LoadKick(Attack):
    def __init__(self):
        super().__init__()
        self.name = "Load Kick"
        self.speed = 50  # Plus lent que Fast Kick
        self.energy_cost = 25
        self.life_damage = 80
        self.stamina_damage = 40
        self.shield_damage = 50
        self.race_specifications = ["Saiyan", "Android"]