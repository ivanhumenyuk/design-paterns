from abc import abstractmethod, ABC
from copy import deepcopy


# Prototype
class Smartphone(ABC):
    @abstractmethod
    def clone(self):
        pass


class Iphone10(Smartphone):
    def __init__(self, color, screen_size, memory):
        self.color = color
        self.screen_size = screen_size
        self.memory = memory

    def clone(self):
        return Iphone10(self.color,
                        self.screen_size,
                        self.memory)

    def __str__(self):
        return f'This is {self.__class__.__name__} model'


class XiaomiMi10T(Smartphone):
    def __init__(self, color, memory, glass_type):
        self.color = color
        self.memory = memory
        self.glass_type = glass_type

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f'This is {self.__class__.__name__} model'


if __name__ == '__main__':
    smartphone1 = Iphone10('white', 5, 256)
    smartphone2 = smartphone1.clone()

    print(smartphone1)
    print(smartphone2)

    smartphone3 = XiaomiMi10T('rosy', '64', 'Gorilla glass 8')
    smartphone4 = smartphone3.clone()

    print(smartphone3)
    print(smartphone4)
