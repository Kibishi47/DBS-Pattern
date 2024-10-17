class TransformationState:
    def __init__(self, race):
        self.race = race
        self.name = "name"
        self.sup_life = 0
        self.sup_stamina = 0
        self.sup_energy = 0
        self.sup_shield = 0
        self.sup_speed = 0
        self.sup_force = 0

        self.inf_life = 0
        self.inf_stamina = 0
        self.inf_energy = 0
        self.inf_shield = 0
        self.inf_speed = 0
        self.inf_force = 0
        

    def get_name(self):
        return self.name
    
    def get_life(self):
        actual_life = self.race.stats.get_life() + self.sup_life
        max_life = self.race.original_stats.get_life() + self.sup_life
        if (actual_life - self.inf_life > max_life):
            self.inf_life += actual_life - max_life
        return actual_life - self.inf_life

    def get_stamina(self):
        actual_stamina = self.race.stats.get_stamina() + self.sup_stamina
        max_stamina = self.race.original_stats.get_stamina() + self.sup_stamina
        if (actual_stamina - self.inf_stamina > max_stamina):
            self.inf_stamina += actual_stamina - max_stamina
        return actual_stamina - self.inf_stamina

    def get_energy(self):
        actual_energy = self.race.stats.get_energy() + self.sup_energy
        max_energy = self.race.original_stats.get_energy() + self.sup_energy
        if (actual_energy - self.inf_energy > max_energy):
            self.inf_energy += actual_energy - max_energy
        return actual_energy - self.inf_energy

    def get_shield(self):
        actual_shield = self.race.stats.get_shield() + self.sup_shield
        max_shield = self.race.original_stats.get_shield() + self.sup_shield
        if (actual_shield - self.inf_shield > max_shield):
            self.inf_shield += actual_shield - max_shield
        return actual_shield - self.inf_shield

    def get_speed(self):
        actual_speed = self.race.stats.get_speed() + self.sup_speed
        max_speed = self.race.original_stats.get_speed() + self.sup_speed
        if (actual_speed - self.inf_speed > max_speed):
            self.inf_speed += actual_speed - max_speed
        return actual_speed - self.inf_speed

    def get_force(self):
        actual_force = self.race.stats.get_force() + self.sup_force
        max_force = self.race.original_stats.get_force() + self.sup_force
        if (actual_force - self.inf_force > max_force):
            self.inf_force += actual_force - max_force
        return actual_force - self.inf_force
    
    def base_form(self):
        self.race.set_transformation(BaseForm(self.race))
    
    def super_saiyan(self):
        self.race.set_transformation(SuperSaiyan(self.race))
    
    def super_saiyan_2(self):
        self.race.set_transformation(SuperSaiyan2(self.race))
    
    def super_saiyan_3(self):
        self.race.set_transformation(SuperSaiyan3(self.race))
    
    def super_saiyan_god(self):
        self.race.set_transformation(SuperSaiyanGod(self.race))
    
    def super_saiyan_blue(self):
        self.race.set_transformation(SuperSaiyanBlue(self.race))
    
    def ultra_instinct(self):
        self.race.set_transformation(UltraInstinct(self.race))
    
    def great_ape(self):
        self.race.set_transformation(GreatApe(self.race))
    
    def super_namekian(self):
        self.race.set_transformation(SuperNamekian(self.race))
    
class BaseForm(TransformationState):
    def __init__(self, race):
        super().__init__(race)
        self.name = "Base Forme"
        self.sup_life = 0
        self.sup_stamina = 0
        self.sup_energy = 0
        self.sup_shield = 0
        self.sup_speed = 0
        self.sup_force = 0

    def get_name(self):
        return self.race.name
    
    def base_form(self):
        pass

class SuperSaiyan(TransformationState):
    def __init__(self, race):
        super().__init__(race)
        self.name = "Super Saiyan"
        self.sup_life = 50
        self.sup_stamina = 30
        self.sup_energy = 20
        self.sup_shield = 0
        self.sup_speed = 10
        self.sup_force = 50

    def super_saiyan(self):
        pass

class SuperSaiyan2(TransformationState):
    def __init__(self, race):
        super().__init__(race)
        self.name = "Super Saiyan 2"
        self.sup_life = 60
        self.sup_stamina = 40
        self.sup_energy = 30
        self.sup_shield = 10
        self.sup_speed = 15
        self.sup_force = 60

    def super_saiyan_2(self):
        pass

class SuperSaiyan3(TransformationState):
    def __init__(self, race):
        super().__init__(race)
        self.name = "Super Saiyan 3"
        self.sup_life = 70
        self.sup_stamina = 50
        self.sup_energy = 40
        self.sup_shield = 20
        self.sup_speed = 20
        self.sup_force = 70
    
    def super_saiyan_3(self):
        pass

class SuperSaiyanGod(TransformationState):
    def __init__(self, race):
        super().__init__(race)
        self.name = "Super Saiyan God"
        self.sup_life = 80
        self.sup_stamina = 60
        self.sup_energy = 50
        self.sup_shield = 30
        self.sup_speed = 25
        self.sup_force = 80
    
    def super_saiyan_god(self):
        pass

class SuperSaiyanBlue(TransformationState):
    def __init__(self, race):
        super().__init__(race)
        self.name = "Super Saiyan Blue"
        self.sup_life = 90
        self.sup_stamina = 70
        self.sup_energy = 60
        self.sup_shield = 40
        self.sup_speed = 30
        self.sup_force = 90
    
    def super_saiyan_blue(self):
        pass

class UltraInstinct(TransformationState):
    def __init__(self, race):
        super().__init__(race)
        self.name = "Ultra Instinct"
        self.sup_life = 100
        self.sup_stamina = 80
        self.sup_energy = 70
        self.sup_shield = 50
        self.sup_speed = 40
        self.sup_force = 100
    
    def ultra_instinct(self):
        pass

class GreatApe(TransformationState):
    def __init__(self, race):
        super().__init__(race)
        self.name = "Great Ape"
        self.sup_life = 150
        self.sup_stamina = 100
        self.sup_energy = 80
        self.sup_shield = 60
        self.sup_speed = 20
        self.sup_force = 150
    
    def great_ape(self):
        pass

class SuperNamekian(TransformationState):
    def __init__(self, race):
        super().__init__(race)
        self.name = "Super Namekian"
        self.sup_life = 100
        self.sup_stamina = 70
        self.sup_energy = 60
        self.sup_shield = 50
        self.sup_speed = 30
        self.sup_force = 110

    def super_namekian(self):
        pass