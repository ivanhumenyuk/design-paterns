from __future__ import annotations
from abc import ABC, abstractmethod


class Manager(ABC):

    @abstractmethod
    def handle_call(self, call):
        pass

    @abstractmethod
    def forwarding(self, next: Manager):
        pass


class AbstractManager(Manager):
    _next_manager = None

    @abstractmethod
    def handle_call(self, call):
        if self._next_manager:
            return self._next_manager.handle_call(call)

    def forwarding(self, next: Manager):
        self._next_manager = next
        return next


class SalesManager(AbstractManager):
    def handle_call(self, call):
        if call == 'Sales':
            return 'I\'ll help you with your question'
        else:
            return super().handle_call(call)


class PurchasingManager(AbstractManager):
    def handle_call(self, call):
        if call == 'Procurement and Delivery':
            return 'Ok. I can help you!!!'
        else:
            return super().handle_call(call)


class CommercialManager(AbstractManager):
    def handle_call(self, call):
        if call == 'Advertising':
            return 'Good day! Of course, lets talk!'
        else:
            return super().handle_call(call)


def app(manager):
    for theme in ['Sales', 'WebApp', 'Procurement and Delivery', 'Advertising']:
        response = manager.handle_call(theme)
        print(f'Theme of call: {theme}')
        if response:
            print(f'{response} \n')
        else:
            print('Sorry, choose another theme of call.\n')


if __name__ == '__main__':
    manager1 = SalesManager()
    manager2 = PurchasingManager()
    manager3 = CommercialManager()

    manager1.forwarding(manager2).forwarding(manager3)
    app(manager1)
