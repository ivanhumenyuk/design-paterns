import copy
from abc import ABC, abstractmethod


class Cloneable(ABC):
    @abstractmethod
    def clone(self):
        pass


class Connection:
    def __init__(self, host, port, login, password):
        self.is_open = False
        self.host = host
        self.port = port
        self.login = login
        self.password = password

    def open(self):
        self.is_open = True
        print(f'Current {self.host}:{self.port} is opened')


class Config:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2


class User(Cloneable):
    def __init__(self, connection: Connection, config: Config):
        self.connection = connection
        self.config = config

    def clone(self):
        return User(self.connection, copy.deepcopy(self.config))

    def start(self):
        if not self.connection.is_open:
            self.connection.open()
        print(f"Consuming from param_1: {self.config.param_1},"
              f" param_2: {self.config.param_2}")


if __name__ == '__main__':

    connection = Connection('localhost', '5000', 'root', '*****')
    config = Config("23", "80")
    user = User(connection, config)
    user.start()
    # print(consumer)

    user_clone_1 = user.clone()
    user_clone_1.config.param_2 = "567"
    user_clone_1.start()
    # print(consumer_clone_1)






