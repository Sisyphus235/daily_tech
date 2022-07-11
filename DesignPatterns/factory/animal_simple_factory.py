
from abc import ABCMeta, abstractclassmethod


class Animal(metaclass=ABCMeta):
    @abstractclassmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print('Bhowm, Bhow!')


class Cat(Animal):
    def do_say(self):
        print('Meow, Meow!')


class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    animal = input('which animal should make sound, Dog or Cat?\n')
    ff.make_sound(animal)
