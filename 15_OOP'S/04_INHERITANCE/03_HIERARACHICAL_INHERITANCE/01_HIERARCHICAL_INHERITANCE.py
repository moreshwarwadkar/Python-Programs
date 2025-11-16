# INHERITANC: HIERARCHICAL INHERITANCE

class Animal:

    def sound(self):
        print('Animal Make Sound')

class Dog(Animal):

    def bark(self):
        print('Dog Bark')

class Cat(Animal):

    def meow(self):
        print('Cat Meows')

d = Dog()
c = Cat()

d.sound()
c.sound()

d.bark()
c.meow()


'''
OUTPUT:

Animal Make Sound
Animal Make Sound
Dog Bark
Cat Meows
'''
