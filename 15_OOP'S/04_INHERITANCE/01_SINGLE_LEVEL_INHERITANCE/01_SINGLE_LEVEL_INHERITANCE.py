# INHERITANCE: SINGLE LEVEL INHERITANCE

class Animal:

    def sound(self):  # INSTANCE METHOD
        print('Animal Making Sound')

class Dog(Animal):

    def bark(self):  # INSTANCE METHOD
        print('Dog Barks')

d = Dog()

d.sound()
d.bark()

'''
OUTPUT:

Animal Making Sound
Dog Barks
'''
