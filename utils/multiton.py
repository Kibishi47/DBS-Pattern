from typing import TypeVar, Type

T = TypeVar('T', bound='Multiton')

class Multiton:
    _instances = {}

    @classmethod
    def get_instance(cls: Type[T], key) -> T:
        if key not in cls._instances:
            cls._instances[key] = cls()
        return cls._instances[key]