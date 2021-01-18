from collections.abc import Iterator, Iterable
import random


class RandomIterator(Iterator):
    def __init__(self, collection: Iterable):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            random_int = random.randint(1, 2)
            self.index += random_int
            output = (self.collection[self.index])/2
        except IndexError:
            raise StopIteration
        return output

if __name__ == '__main__':
    collection = [2, 3, 45, 563, 54643, 34534, 4543, 564, 456, 456, 45, 56, 66, 546435, 34553, 53453, 4, 53, 54, ]
    iterator = RandomIterator(collection)

    for i in iterator:
        print(i)

