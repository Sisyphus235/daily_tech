from abc import ABCMeta, abstractclassmethod


class Section(metaclass=ABCMeta):
    @abstractclassmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print('Personal section')


class AlbumSection(Section):
    def describe(self):
        print('Album section')


class PatentSection(Section):
    def describe(self):
        print('Patent section')


class PublicationSection(Section):
    def describe(self):
        print('Publication section')


class Profile(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.sections = []
        self.createProfile()

    @abstractclassmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = input(
        'which profile you like to create? LinkedIn or Facebook \n')
    profile = eval(profile_type.lower())()
    print('creating profiles...', type(profile).__name__)
    print('profiles sections: ')
    [section.describe() for section in profile.getSections()]
