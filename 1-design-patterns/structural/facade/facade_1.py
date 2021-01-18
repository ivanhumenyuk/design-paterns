from __future__ import annotations

from abc import ABC, abstractmethod


# Facade class
class UserInterface:
    def __init__(self,
                 full_face_analyzer: PhotoAnalyzer,
                 profile_face_analyzer: PhotoAnalyzer,
                 full_photo: PhotoLoader,
                 profile_photo: PhotoLoader):
        self.full_face_analyzer = full_face_analyzer
        self.profile_face_analyzer = profile_face_analyzer
        self.full_photo = full_photo
        self.profile_photo = profile_photo

    def upper_half_type(self):
        processing = [self.full_photo.load_photo(),
                      self.profile_photo.load_photo(),
                      self.full_face_analyzer.eyes_type_detector(),
                      self.full_face_analyzer.frontal_lobes_type_detector(),
                      self.profile_face_analyzer.frontal_lobes_type_detector(),
                      self.profile_face_analyzer.eyes_type_detector()]
        print('-' * 30)
        print("\n".join(processing))
        print('Your upper half has ... type')
        print('-' * 30)

    def bottom_half_type(self):
        initialization = [
            self.full_photo.load_photo(),
            self.profile_photo.load_photo(),
            self.profile_face_analyzer.jaw_chin_classifier(),
            self.full_face_analyzer.jaw_chin_classifier()
        ]
        print('-' * 30)
        print("\n".join(initialization))
        print('Your bottom half has ... type')
        print('-' * 30)

    def physiognomy_type(self):
        print('You are typical bottom half has ... type')


class PhotoLoader:
    def __init__(self, path: str):
        self.path = path

    def load_photo(self):
        return f'Loading photo from {self.path}'


class PhotoAnalyzer(ABC):
    @abstractmethod
    def frontal_lobes_type_detector(self):
        pass

    @abstractmethod
    def jaw_chin_classifier(self):
        pass

    @abstractmethod
    def eyes_type_detector(self):
        pass


class FaceInProfileAnalyzer(PhotoAnalyzer):
    """This class implements logic of CV model that studies the face in profile"""

    def frontal_lobes_type_detector(self):
        return 'Detecting of profile face forehead type...'

    def jaw_chin_classifier(self):
        return 'Classification of profile face jaws line and chin...'

    def eyes_type_detector(self):
        return 'Eyes cut classification...'


class FullFaceAnalyzer(PhotoAnalyzer):
    """This class implements logic of CV model that studies the full face"""

    def frontal_lobes_type_detector(self):
        return 'Superciliary arches detecting...'

    def jaw_chin_classifier(self):
        return 'Classification of full face jaws line and chin...'

    def eyes_type_detector(self):
        return 'Color and type detecting of eyes in full face ...'


if __name__ == '__main__':
    analyzer1 = FullFaceAnalyzer()
    analyzer2 = FaceInProfileAnalyzer()
    loader = PhotoLoader(r'D:\user\photo')
    facade = UserInterface(analyzer1, analyzer2, loader, loader)

    facade.bottom_half_type()
    facade.upper_half_type()
