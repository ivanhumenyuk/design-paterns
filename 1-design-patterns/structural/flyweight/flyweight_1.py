# Flyweight
class Actor:
    def __init__(self, name):
        self.name = name


# Flyweight Factory
class Theater:
    _actors = {}

    def get_actor(self, name):
        actor = self._actors.get(name)
        if not actor:
            new_actor = Actor(name)
            self._actors[name] = new_actor
            return new_actor
        else:
            return actor


class Scene:
    _character_list = {}

    def add_actor(self, name, character):
        actor = Theater().get_actor(name)
        self._character_list[character] = actor

    def get_character_list(self):
        for char, act in self._character_list.items():
            print(f'Role of {char} plays {act}')
        print(self._character_list)
        print(Theater()._actors)


if __name__ == '__main__':
    Iliad = Scene()
    Iliad.add_actor('Natalie Protsenko', 'Woman-hero1')
    Iliad.add_actor('Natalie Protsenko', 'Woman-hero2')
    Iliad.add_actor('David Lozinskiy', 'Achilles')
    Iliad.add_actor('Ivan Ignatov', 'Hector')
    Iliad.add_actor('Ihor Tolmachev', 'Aeneas')
    Iliad.add_actor('Ihor Tolmachev', 'Extras man')

    Iliad.get_character_list()
