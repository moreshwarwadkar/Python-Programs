# ABSTRACT METHOD

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):

        self.radius = radius

    def area(self):

        return 3.14*self.radius * self.radius

class Square(Shape):

    def __init__(self,side):

        self.side = side

    def area(self):

        return self.side * self.side

c = Circle(2)
s = Square(4)

print('Area Of Circle: ',c.area())
print('Area Of Square: ',s.area())


'''
OUTPUT :

Area Of Circle:  12.56
Area Of Square:  16
'''
