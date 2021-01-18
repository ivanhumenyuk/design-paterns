from abc import abstractmethod, ABC


# Product class and instances
class Building(ABC):
    @abstractmethod
    def type_of_building(self):
        pass


class House(Building):
    def type_of_building(self):
        return str(self.__class__.__name__)


class Hangar(Building):
    def type_of_building(self):
        return str(self.__class__.__name__)


# Factory class
class BuildingFactory(ABC):
    @abstractmethod
    def build(self):
        pass


class AgroFactory(BuildingFactory):
    def build(self):
        return f'Our company offers to build {Hangar().type_of_building()}s'


class CivilFactory(BuildingFactory):
    def build(self):
        return f'We are {self.__class__.__name__} and we offer to build {House().type_of_building()}s'


def build_agro():
    return CivilFactory().build()


def build_civil():
    return AgroFactory().build()


button1 = build_agro()
button2= build_civil()

if __name__ == "__main__":
    print(button1)
    print(button2)
