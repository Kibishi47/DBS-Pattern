from entities.warrior.stats import Stats

class GaugeDecorator(Stats):
    def __init__(self, stats: Stats, num):
        self._stats = stats
        self.num = num

    def get_life(self):
        return self._stats.get_life()

    def get_stamina(self):
        return self._stats.get_stamina()

    def get_energy(self):
        return self._stats.get_energy()

    def get_shield(self):
        return self._stats.get_shield()

    def get_speed(self):
        return self._stats.get_speed()

    def get_force(self):
        return self._stats.get_force()

class LifeLose(GaugeDecorator):
    def get_life(self):
        return self._stats.get_life() - self.num

class LifeGain(GaugeDecorator):
    def get_life(self):
        return self._stats.get_life() + self.num
    
class StaminaLose(GaugeDecorator):
    def get_stamina(self):
        return self._stats.get_stamina() - self.num

class StaminaGain(GaugeDecorator):
    def get_stamina(self):
        return self._stats.get_stamina() + self.num
    
class EnergyLose(GaugeDecorator):
    def get_energy(self):
        return self._stats.get_energy() - self.num

class EnergyGain(GaugeDecorator):
    def get_energy(self):
        return self._stats.get_energy() + self.num
    
class ShieldLose(GaugeDecorator):
    def get_shield(self):
        return self._stats.get_shield() - self.num

class ShieldGain(GaugeDecorator):
    def get_shield(self):
        return self._stats.get_shield() + self.num
    
class SpeedLose(GaugeDecorator):
    def get_speed(self):
        return self._stats.get_speed() - self.num

class SpeedGain(GaugeDecorator):
    def get_speed(self):
        return self._stats.get_speed() + self.num
    
class ForceLose(GaugeDecorator):
    def get_force(self):
        return self._stats.get_force() - self.num

class ForceGain(GaugeDecorator):
    def get_force(self):
        return self._stats.get_force() + self.num