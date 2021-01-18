# Component class
class Button:
    def press(self):
        pass


# wrappee instance
class SelectButton(Button):
    def name(self):
        return self.__class__.__name__

    def press(self):
        return f'--You\'ve pressed {self.name()}--'


# wrappee instance
class DeleteButton(Button):
    def name(self):
        return self.__class__.__name__

    def press(self):
        return f'--You\'ve pressed {self.name()}--'


# Decorator Interface
class HeroWeapon():
    def __init__(self, sel_button: Button, del_button: Button):
        self.sel_button = sel_button
        self.del_button = del_button

    def weapon_name(self):
        return self.__class__.__name__

    def delete_weapon(self):
        return self.del_button.press()

    def select_weapon(self):
        return self.sel_button


class Ak74(HeroWeapon):
    def delete_weapon(self):
        return f'{self.del_button.press()} \n' \
               f'{self.weapon_name()} has been successfully deleted!'

    def select_weapon(self):
        return f'{self.del_button.press()} \n' \
               f'{self.weapon_name()} has been successfully taken!'


# decorator instance
class M16(HeroWeapon):
    def delete_weapon(self):
        return f'{self.del_button.press()} \n' \
               f'{self.weapon_name()} has been successfully deleted!'

    def select_weapon(self):
        return f'{self.sel_button.press()} \n' \
               f'{self.weapon_name()} has been successfully taken!'

    def take_muffler(self):
        return f'{self.sel_button.press()} \n' \
               f'{self.weapon_name()} has been successfully mounted on your rifle!'


if __name__ == '__main__':
    select_b = SelectButton()
    delete_b = DeleteButton()

    m16_interface = M16(select_b, delete_b)
    ak74_interface = Ak74(select_b, delete_b)

    print(m16_interface.select_weapon())
    print('\n')
    print(m16_interface.take_muffler())
    print('\n\n')

    print(m16_interface.delete_weapon())
    print('\n')
    print(ak74_interface.select_weapon())
