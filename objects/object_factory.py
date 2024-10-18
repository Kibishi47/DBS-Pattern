from objects.object import PowerPole, SenzuBean, KintoUn, DragonBall

class ObjectFactory:
    objects = {
        'PowerPole': PowerPole,
        'SenzuBean': SenzuBean,
        'KintoUn': KintoUn,
        'DragonBall': DragonBall,
    }

    id = 0

    @classmethod
    def create_object(cls, object_type):
        cls.id += 1
        return cls.objects.get(object_type, None)(cls.id)