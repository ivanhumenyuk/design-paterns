from abc import ABC, abstractmethod


class VkMusic(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def download(self):
        pass


class MusicList(VkMusic):
    def __repr__(self):
        return self.__class__.__name__

    def play(self):
        return 'Playing your choosing track'

    def download(self):
        return 'Downloading your track'


class CacheMusic(VkMusic):

    def __init__(self, music_list: MusicList):
        self.music_list = music_list

    def play(self):
        return f'Checking of music in cache list...' \
               f'{self.music_list.play()}'

    def download(self):
        return f'Checking of music in cache list... \n'\
               f'Adding it from {MusicList()}...\n' \
               f'{self.music_list.play()}'


if __name__ == '__main__':
    print('\n')
    print('-' * 40)
    real_music_list = MusicList()
    print(real_music_list.play())
    print(real_music_list.download())
    print('-'*40)
    print('\n')

    cache_list = CacheMusic(real_music_list)
    print('-' * 40)
    print(cache_list.play())
    print(cache_list.download())
    print('-' * 40)
    print('\n')