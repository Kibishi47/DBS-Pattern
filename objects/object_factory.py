from objects.object import PowerPole, SenzuBean, KintoUn, DragonBall

class ObjectFactory:
    objects = {
        'PowerPole': PowerPole(),
        'SenzuBean': SenzuBean(),
        'KintoUn': KintoUn(),
        'DragonBall': DragonBall(),
    }

    @classmethod
    def create_object(cls, object_type):
        return cls.objects.get(object_type, None)