from races.race import Race, Saiyan, Namekian, Android

class RaceFactory:
    races = {
        "Saiyan": Saiyan(),
        "Namekian": Namekian(),
        "Android": Android(),
    }
    @classmethod
    def create_race(cls, race_type) -> Race:
        return cls.races.get(race_type, None)