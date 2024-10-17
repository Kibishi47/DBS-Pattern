
class LogManager:
    _instance = None
    
    def __init__(self):
        self.battle_logs = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def log(self, info: str):
        self.battle_logs.append(info)
