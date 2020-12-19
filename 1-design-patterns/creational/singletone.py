# classic Singleton


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


singleton_1 = Singleton()
print(singleton_1)

singleton_2 = Singleton()
print(singleton_2)

singleton_3 = Singleton()
print(singleton_3)


# Meta Singleton

class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class New(metaclass=SingletonMeta):
    creation_counter = 0

    def __init__(self):
        self.creation_counter += 1


new_1 = New()
new_2 = New()

if id(new_1) == id(new_2):
    print(new_2)
    print(new_2)
