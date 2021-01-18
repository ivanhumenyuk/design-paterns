from abc import ABC, abstractmethod


# Abstraction class
class SubwaySurfer:
    def __init__(self, device):
        self.device = device

    def auto_save(self):
        return f'App is {self.device.save_and_unpack()}\n\n'\
               f'Subway Surfer is {self.device.install()}'


# Extended abstraction
class SubwaySurferLimited(SubwaySurfer):
    def start(self):
        return f'SubSurf App is {self.device.start()}'


# Implementation
class Device(ABC):
    @abstractmethod
    def save_and_unpack(self):
        pass

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def start(self):
        pass


class Iphone11X(Device):
    def name(self):
        return self.__class__.__name__

    def __repr__(self):
        return

    def save_and_unpack(self):
        return f'unpacking... and saving... in {self.name()}'

    def install(self):
        return f'installing... in {self.name()}'

    def start(self):
        return f'starting in {self.name()}'


class XiaomiMi10T(Device):
    def name(self):
        return self.__class__.__name__

    def save_and_unpack(self):
        return f'unpacking... and saving... in {self.name()}'

    def install(self):
        return f'installing... in {self.name()}'

    def start(self):
        return f'starting in {self.name()}'


if __name__ == '__main__':
    app1 = SubwaySurfer(XiaomiMi10T())
    app2 = SubwaySurferLimited(Iphone11X())

    print(app1.auto_save())
    print('\n\n')
    print(app2.auto_save())
    print(app2.start())
