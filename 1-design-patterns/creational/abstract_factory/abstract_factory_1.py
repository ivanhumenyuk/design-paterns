from abc import abstractmethod, ABC


# Product class
class SmartPhone(ABC):
    @abstractmethod
    def incoming_call(self):
        pass

    @abstractmethod
    def outgoing_call(self):
        pass


class Laptop(ABC):
    @abstractmethod
    def run_prompt(self):
        pass


class Factory(ABC):
    @abstractmethod
    def produce_smartphone(self):
        pass

    @abstractmethod
    def produce_laptop(self):
        pass


# Smartphone instances
class Iphone12(SmartPhone):
    def name(self):
        return self.__class__.__name__

    def incoming_call(self):
        print(f'Making incoming call from {self.name()}')

    def outgoing_call(self):
        print(f'Making outgoing call from {self.name()}')


class GalaxyNote20(SmartPhone):
    def name(self):
        return self.__class__.__name__

    def incoming_call(self):
        print(f'Making incoming call from {self.name()}')

    def outgoing_call(self):
        print(f'Making incoming call from {self.name()}')


# Laptops
class MacBookAir(Laptop):
    def run_prompt(self):
        pass


class FlexA(Laptop):
    def run_prompt(self):
        pass


# Factories
class AppleFactory(Factory):
    def produce_smartphone(self):
        return Iphone12()

    def produce_laptop(self):
        return MacBookAir()


class SamsungFactory(Factory):
    def produce_smartphone(self):
        return GalaxyNote20()

    def produce_laptop(self):
        return FlexA()


if __name__ == '__main__':
    factory = AppleFactory()
    smartphone = factory.produce_smartphone()

    smartphone.incoming_call()
