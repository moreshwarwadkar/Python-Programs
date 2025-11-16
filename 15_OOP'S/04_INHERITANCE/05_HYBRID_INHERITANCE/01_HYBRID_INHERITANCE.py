# INHERITANCE: HYBRID INHERITANCE


class Animal:

    def sound(self):
        print('Animal Make Sound')

class Dog(Animal):  #SINGLE LEVEL

    def bark(self):
        print('Dog Barks')

class Cat(Animal):  #SINGLE LEVEL

    def meow(self):
        print('Cat Meows')

class PetDog(Dog,Cat):  #MULTIPLE INHERITANCE

    def pet_name(self):
        print('This is Pet Dog')

p = PetDog()

p.sound()
p.bark()
p.meow()
p.pet_name()

'''
OUTPUT:

Animal Make Sound
Dog Barks
Cat Meows
This is Pet Dog
'''
