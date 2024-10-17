class Stats:
    def __init__(self):
        self.life = 0
        self.stamina = 0
        self.energy = 0
        self.shield = 0
        self.speed = 0
        self.force = 0

    def get_life(self):
        return self.life

    def get_stamina(self):
        return self.stamina

    def get_energy(self):
        return self.energy

    def get_shield(self):
        return self.shield

    def get_speed(self):
        return self.speed

    def get_force(self):
        return self.force
    
class SaiyanStats(Stats):
    def __init__(self):
        self.life = 200           # Bonne résistance physique
        self.stamina = 90         # Endurance élevée mais pas infinie
        self.energy = 50          # Énergie moyenne, mais augmente avec les transformations
        self.shield = 10          # Défense modérée
        self.speed = 120          # Très rapides en combat
        self.force = 80           # Force physique brute élevée

class NamekianStats(Stats):
    def __init__(self):
        self.life = 300           # Très résistants grâce à la régénération
        self.stamina = 85         # Endurance correcte
        self.energy = 100          # Grande maîtrise de l'énergie spirituelle
        self.shield = 15          # Bonne défense
        self.speed = 100          # Agiles, mais moins rapides que les Saiyans
        self.force = 65           # Moins forts physiquement que les Saiyans, mais compensés par leur énergie

class AndroidStats(Stats):
    def __init__(self):
        self.life = 400           # Très résistants
        self.stamina = float('inf')  # Endurance infinie (ne se fatiguent jamais)
        self.energy = 60          # Bonne énergie mais moins puissante que celle des Namekians
        self.shield = 20          # Excellente défense grâce à leur corps artificiel
        self.speed = 90           # Moins rapides que les Saiyans et Namekians
        self.force = 70           # Force physique correcte, mais pas aussi élevée que les Saiyans