from attacks.attack import Regeneration, Afterimage, Kamehameha, Blast, FastPunch, LoadPunch, FastKick, LoadKick

class AttackFactory:
    attacks = {
        'Regeneration': Regeneration,
        'Afterimage': Afterimage,
        'Kamehameha': Kamehameha,
        'Blast': Blast,
        'FastPunch': FastPunch,
        'LoadPunch': LoadPunch,
        'FastKick': FastKick,
        'LoadKick': LoadKick,
    }

    id = 0

    @classmethod
    def create_attack(cls, attack_type: str):
        cls.id += 1
        return cls.attacks.get(attack_type, None)(cls.id)