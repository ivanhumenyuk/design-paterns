from abc import ABC, abstractmethod


class Subscriber(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_new(self, new):
        pass


class XiaomiSubscriber(Subscriber):

    def get_new(self, new):
        return f"Breaking news: {new}"


class SamsungSubscriber(Subscriber):
    def get_new(self, new):
        return f"***SOUND*** \n Today: {new}"


class News:
    def __init__(self):
        self.new = None
        self.subscribers = []

    def set_new(self, text: str):
        self.new = text
        return 'Today\'s news'

    def follow(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)
        return f'User {subscriber.name} follows news channel.'

    def notify_subscribers(self):
        for s in self.subscribers:
            print(f'\n{s.get_new(self.new)}\n')


if __name__ =='__main__':
    news = News()
    new1 = "CRYPTO IN TRENDS TODAY. \n Read more..."

    sub1 = SamsungSubscriber('Tim Send')
    sub2 = XiaomiSubscriber('Radjav Bhagar')

    print(news.follow(sub1))
    print(news.follow(sub2))

    print(news.set_new(new1))

    news.notify_subscribers()



