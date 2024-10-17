from attacks.attack import Regeneration, Afterimage, Kamehameha, Blast, FastPunch, LoadPunch, FastKick, LoadKick

class AttackFactory:
    attacks = {
        'Regeneration': Regeneration(),
        'Afterimage': Afterimage(),
        'Kamehameha': Kamehameha(),
        'Blast': Blast(),
        'FastPunch': FastPunch(),
        'LoadPunch': LoadPunch(),
        'FastKick': FastKick(),
        'LoadKick': LoadKick(),
    }

    @classmethod
    def create_attack(cls, attack_type: str):
        return cls.attacks.get(attack_type, None)