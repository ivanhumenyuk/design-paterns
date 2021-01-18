from abc import ABC, abstractmethod


class SalesSystem(ABC):
    @abstractmethod
    def discount(self, amount: float):
        pass


class BaseSalesSystem(SalesSystem):
    def discount(self, amount: float):
        return amount * 0.92


class GoldSalesSystem(SalesSystem):
    def discount(self, amount: float):
        return amount * 0.75


class PremiumSalesSystem(SalesSystem):
    def discount(self, amount: float):
        return amount * 0.8


class NextYearSubscription:
    def __init__(self, sale: SalesSystem):
        self.price = 0
        self.sale = sale

    def set_price(self, price):
        self.price = price

    def calculate_discount(self):
        return f'Discount is {self.sale.discount(self.price)}'


if __name__ == '__main__':
    base_client = NextYearSubscription(BaseSalesSystem())
    base_client.set_price(1000)
    print(base_client.calculate_discount())
