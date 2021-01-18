from abc import ABC, abstractmethod


# invoker class
class Pilot():
    def __init__(self, button):
        self.button = button

    def press(self):
        return f'Pilot {self.button.press()}\'s turbine'


# receiver class
class Turbine:
    def __init__(self):
        self.status = 'off'

    def set_off(self):
        self.status = 'off'
        return self.status

    def set_on(self):
        self.status = 'on'
        return self.status


# command abs class
class BoardButton(ABC):
    def __init__(self, turbine: Turbine):
        self.turbine = turbine

    @abstractmethod
    def press(self):
        pass


# command class
class TurbineOnButton(BoardButton):
    def press(self):
        return self.turbine.set_on()


# command class
class TurbineOffButton(BoardButton):
    def press(self):
        return self.turbine.set_off()


if __name__ == '__main__':
    turbine = Turbine()
    print(f'Turbine is {turbine.status} now')

    on_command = TurbineOnButton(turbine)
    off_command = TurbineOffButton(turbine)
    pilot = Pilot(on_command)

    print('\n')
    print(pilot.press())
    print(f'Turbine is {turbine.status} now')

