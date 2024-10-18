from transformations.transformation import BaseForm, SuperSaiyan, SuperSaiyan2, SuperSaiyan3, SuperSaiyanGod, SuperSaiyanBlue, SuperNamekian
from entities.warrior.stats import Stats, SaiyanStats, NamekianStats, AndroidStats
from managers.observer import Observer

class Race:
    
    races = [
        "Saiyan",
        "Namekian",
        "Android"
    ]

    def __init__(self):
        self.name = "name"
        self.original_stats = Stats()
        self.stats = Stats()
        self.transformation = BaseForm(self)
        self.player_name = ""

    def decor_stats(self, decorator, amount):
        self.stats = decorator(self.stats, amount)

    def get_name(self):
        return self.transformation.get_name()

    def get_life(self):
        return self.transformation.get_life()

    def get_stamina(self):
        return self.transformation.get_stamina()

    def get_energy(self):
        return self.transformation.get_energy()

    def get_shield(self):
        return self.transformation.get_shield()

    def get_speed(self):
        return self.transformation.get_speed()

    def get_force(self):
        return self.transformation.get_force()
    
    def set_transformation(self, transformation):
        self.transformation = transformation
        
    def get_transformations(self):
        return {
            "Ultra Instinct": "ultra_instinct"
        }

    def base_form(self):
        self.transformation.base_form()

    def ultra_instinct(self):
        self.transformation.ultra_instinct()

class Saiyan(Race):
    def __init__(self):
        super().__init__()
        self.name = "Saiyan"
        self.original_stats = SaiyanStats()
        self.stats = SaiyanStats()

    def get_transformations(self):
        return {
            "Super Saiyan": "super_saiyan",
            "Super Saiyan 2": "super_saiyan_2",
            "Super Saiyan 3": "super_saiyan_3",
            "Super Saiyan God": "super_saiyan_god",
            "Super Saiyan Blue": "super_saiyan_blue",
            "Great Ape": "great_ape",
            "Ultra Instinct": "ultra_instinct"
        }

    # Méthodes de transformation
    def super_saiyan(self):
        self.transformation.super_saiyan()

    def super_saiyan_2(self):
        self.transformation.super_saiyan_2()
    
    def super_saiyan_3(self):
        self.transformation.super_saiyan_3()
    
    def super_saiyan_god(self):
        self.transformation.super_saiyan_god()
    
    def super_saiyan_blue(self):
        self.transformation.super_saiyan_blue()
    
    def great_ape(self):
        self.transformation.great_ape()

class Namekian(Race):
    def __init__(self):
        super().__init__()
        self.name = "Namekian"
        self.original_stats = NamekianStats()
        self.stats = NamekianStats()

    def get_transformations(self):
        return {
            "Super Namekian": "super_namekian",
            "Ultra Instinct": "ultra_instinct"
        }

    # Méthode de transformation
    def super_namekian(self):
        self.transformation.super_namekian()

class Android(Race):
    def __init__(self):
        super().__init__()
        self.name = "Android"
        self.original_stats = AndroidStats()
        self.stats = AndroidStats()