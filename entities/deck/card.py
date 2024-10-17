from attacks.attack import Attack
from objects.object import Object
from gauge.gauge import EnergyGain, EnergyLose, LifeGain, LifeLose, StaminaGain, StaminaLose, ShieldGain, ShieldLose, ForceGain, ForceLose

class Card:
    def __init__(self):
        pass

    def use(self, user, target):
        pass

class AttackCard(Card):

    def __init__(self, type_class: Attack):
        self.unique_quantity = 4
        self.attack = type_class

    def get_name(self):
        return self.attack.name

    def get_complete_name(self):
        return f"{self.attack.name} Attack"
    
    def get_speed(self):
        return self.attack.speed
    
    def get_energy_cost(self):
        return self.attack.energy_cost
        
    def get_stamina_cost(self):
        return self.attack.stamina_cost
        
    def get_life_cost(self):
        return self.attack.life_cost
        
    def get_shield_cost(self):
        return self.attack.shield_cost
        
    def get_force_cost(self):
        return self.attack.force_cost
        
    def get_speed_cost(self):
        return self.attack.speed_cost

    def get_energy_damage(self):
        return self.attack.energy_damage

    def get_stamina_damage(self):
        return self.attack.stamina_damage
        
    def get_life_damage(self):
        return self.attack.life_damage
        
    def get_shield_damage(self):
        return self.attack.shield_damage
        
    def get_force_damage(self):
        return self.attack.force_damage
        
    def get_speed_damage(self):
        return self.attack.speed_damage
            

    def use(self, user, target):
        user.decor_stats(EnergyLose, self.attack.energy_cost)
        user.decor_stats(StaminaLose, self.attack.stamina_cost)
        user.decor_stats(LifeLose, self.attack.life_cost)
        user.decor_stats(ShieldLose, self.attack.shield_cost)
        user.decor_stats(ForceLose, self.attack.force_cost)
        user.decor_stats(ShieldLose, self.attack.speed_cost)

        target.decor_stats(EnergyLose, self.attack.energy_damage)
        target.decor_stats(StaminaLose, self.attack.stamina_damage)
        target.decor_stats(LifeLose, self.attack.life_damage)
        target.decor_stats(ShieldLose, self.attack.shield_damage)
        target.decor_stats(ForceLose, self.attack.force_damage)
        target.decor_stats(ShieldLose, self.attack.speed_damage)

class ObjectCard(Card):
    
    def __init__(self, type_class: Object):
        self.unique_quantity = 2
        self.object = type_class
        self.name = type_class.name

    def get_name(self):
        return self.object.name

    def get_complete_name(self):
        return f"{self.object.name} Object"
    
    def get_speed(self):
        return self.object.speed
    
    def get_energy_cost(self):
        return self.object.energy_cost
        
    def get_stamina_cost(self):
        return self.object.stamina_cost
        
    def get_life_cost(self):
        return self.object.life_cost
        
    def get_shield_cost(self):
        return self.object.shield_cost
        
    def get_force_cost(self):
        return self.object.force_cost
        
    def get_speed_cost(self):
        return self.object.speed_cost

    def get_energy_damage(self):
        return self.object.energy_damage

    def get_stamina_damage(self):
        return self.object.stamina_damage
        
    def get_life_damage(self):
        return self.object.life_damage
        
    def get_shield_damage(self):
        return self.object.shield_damage
        
    def get_force_damage(self):
        return self.object.force_damage
        
    def get_speed_damage(self):
        return self.object.speed_damage

    def use(self, user, target):
        user.decor_stats(EnergyLose, self.object.energy_cost)
        user.decor_stats(StaminaLose, self.object.stamina_cost)
        user.decor_stats(LifeLose, self.object.life_cost)
        user.decor_stats(ShieldLose, self.object.shield_cost)
        user.decor_stats(ForceLose, self.object.force_cost)
        user.decor_stats(ShieldLose, self.object.speed_cost)

        target.decor_stats(EnergyLose, self.object.energy_damage)
        target.decor_stats(StaminaLose, self.object.stamina_damage)
        target.decor_stats(LifeLose, self.object.life_damage)
        target.decor_stats(ShieldLose, self.object.shield_damage)
        target.decor_stats(ForceLose, self.object.force_damage)
        target.decor_stats(ShieldLose, self.object.speed_damage)
