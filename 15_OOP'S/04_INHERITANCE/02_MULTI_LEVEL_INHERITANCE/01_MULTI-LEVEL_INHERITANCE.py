# INHERITANCE: MULTI-LEVEL INHERITANCE

class Grandfather:

    def feature1(self):
        print('Grandfather Feature')

class Father(Grandfather):

    def feature2(self):
        print('Father Feature')

class Son(Father):
    def feature3(self):
        print('Son Feature')

s = Son()

s.feature1()
s.feature2()
s.feature3()

'''
OUTPUT:

Grandfather Feature
Father Feature
Son Feature

'''
