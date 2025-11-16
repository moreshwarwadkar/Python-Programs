# ABTRACTION

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print('Dog Barks')

class Cat(Animal):

    def sound(self):
        print('Cat Meows')

d = Dog()
c = Cat()

d.sound()
c.sound()

'''
OUTPUT:

Dog Barks
Cat Meows
'''
