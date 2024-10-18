from transformations.transformation import BaseForm, SuperSaiyan, SuperSaiyan2, SuperSaiyan3, SuperSaiyanGod, SuperSaiyanBlue, UltraInstinct, GreatApe, SuperNamekian

class TransformationFactory:
    attacks = {
        'Base Forme': BaseForm,
        'Super Saiyan': SuperSaiyan,
        'Super Saiyan 2': SuperSaiyan2,
        'Super Saiyan 3': SuperSaiyan3,
        'Super Saiyan God': SuperSaiyanGod,
        'Super Saiyan Blue': SuperSaiyanBlue,
        'Ultra Instinct': UltraInstinct,
        'Great Ape': GreatApe,
        'Super Namekian': SuperNamekian,
    }

    id = 0

    @classmethod
    def create_transformation(cls, transformation_type: str):
        cls.id += 1
        return cls.attacks.get(transformation_type, None)(cls.id)