from abc import ABC, abstractmethod


# Product class
class App2048():
    def __init__(self):
        self.front_end = None
        self.back_end = None
        self.database = None
        self.stack = []

    def add(self, technology):
        self.stack.append(technology)

    def __str__(self):
        return "2048 application built on a stack of technologies: " + str(self.stack)


# builder class
class Developer(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def front_end(self):
        pass

    @abstractmethod
    def back_end(self):
        pass

    @abstractmethod
    def database(self):
        pass


# Director class for management
class Customer:
    def __init__(self):
        self.developer = None

    def developer(self):
        return self.developer()

    def build_full_stack_app(self):
        self.developer.back_end()
        self.developer.database()
        self.developer.front_end()
        print(self.developer.product)

    def build_server_part(self):
        self.developer.back_end()
        self.developer.database()
        print(self.developer.product)

    def build_ui_part(self):
        self.developer.front_end()
        print(self.developer.product)


class IosDeveloper(Developer):
    def __init__(self):
        self.product = App2048()

    def reset(self):
        self.product = App2048()

    def back_end(self):
        self.product.add(SwiftNIO())

    def database(self):
        self.product.add(Realm())

    def front_end(self):
        self.product.add(Xamarin())


class AndroidDeveloper(Developer):
    def __init__(self):
        self.product = App2048()

    def reset(self):
        self.product = App2048()

    def front_end(self):
        self.product.add(ReactNative())

    def back_end(self):
        self.product.add(Back4App())

    def database(self):
        self.product.add(Sqlite())


class WebDeveloper(Developer):
    def __init__(self):
        self.product = App2048()

    def reset(self):
        self.product = App2048()

    def front_end(self):
        self.product.add(Angular())

    def back_end(self):
        self.product.add(FastAPI())

    def database(self):
        self.product.add(Postgres())


# Database class to inherit
class Database(object):
    def __repr__(self):
        return 'Database: ' + str(self.__class__.__name__)


class Realm(Database):
    pass


class Postgres(Database):
    pass


class Sqlite(Database):
    pass


# Front-end class to inherit
class FrontEnd(object):
    def __repr__(self):
        return 'Front-end(UI) framework: ' + str(self.__class__.__name__)


class ReactNative(FrontEnd):
    pass


class Angular(FrontEnd):
    pass


class Xamarin(FrontEnd):
    pass


# Back-end class to inherit
class BackEnd(object):
    def __repr__(self):
        return 'Back-end framework: ' + str(self.__class__.__name__)


class FastAPI(BackEnd):
    pass


class SwiftNIO(BackEnd):
    pass


class Back4App(BackEnd):
    pass


dev = AndroidDeveloper()
owner = Customer()

owner.developer = dev
owner.build_server_part()








