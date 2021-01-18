class OrderState:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def __next__(self):
        return self.state()

    def cancel(self):
        if self.state().name == 'Waiting for payment':
            return 'Order is canceled.'
        else:
            'This order can be canceled'


class WaitingForPayment(OrderState):
    def __init__(self):
        super().__init__('Waiting for payment', OnWayToClient)


class OnWayToClient(OrderState):
    def __init__(self):
        super().__init__('In way to the client of order', DeliveredToTheClient)


class DeliveredToTheClient(OrderState):
    def __init__(self):
        super().__init__('Current order has been delivered to the client.', DeliveredToTheClient)


class Order:
    def __init__(self):
        self.state = WaitingForPayment()

    def __next__(self):
        self.state = next(self.state)


if __name__ == '__main__':
    order = Order()
    print(order.state.name)

    print('\n')
    next(order)
    print(order.state.name)

    print('\n')
    next(order)
    print(order.state.name)


