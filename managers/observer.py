class Observer:
    _instance = None

    def __init__(self):
        self.observers = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)
