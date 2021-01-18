from abc import ABC, abstractmethod


class Developer(ABC):
    def build_app(self):
        self.build_database_models()
        self.make_server_logic()
        self.make_ui_design()
        self.build_front_end()

    @abstractmethod
    def build_database_models(self):
        pass

    @abstractmethod
    def make_server_logic(self):
        pass

    @abstractmethod
    def make_ui_design(self):
        pass

    @abstractmethod
    def build_front_end(self):
        pass


class JavaReactDeveloper(Developer):

    def build_database_models(self):
        print("I build tables of my models using Oracle DB")

    def make_server_logic(self):
        print('Use Spring for back-end')

    def make_ui_design(self):
        print('I don\'t do this part, because it is for designers')

    def build_front_end(self):
        print('I use react in frontend')


class PythonVueDeveloper(Developer):

    def build_database_models(self):
        print("I build tables of my models using Postgres")

    def make_server_logic(self):
        print('I use Tornado framework in server')

    def make_ui_design(self):
        print('Build design in ANTD')

    def build_front_end(self):
        print('Build frontend using Vue.js')


if __name__ == "__main__":
    developer1 = PythonVueDeveloper()
    developer2 = JavaReactDeveloper()

    developer1.build_app()
    print('\n')
    developer2.build_app()