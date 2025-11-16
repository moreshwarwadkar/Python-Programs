# INHERITANCE: MULTIPLE INHERITANCE

class Father:

    def feature1(self):
        print('Father Feature')

class Mother:

    def feature2(self):
        print('Mother Feature')

class Child(Father, Mother):

    def feature3(self):
        print('Child Feature')

c = Child()

c.feature1()
c.feature2()
c.feature3()

'''
OUTPUT:

Father Feature
Mother Feature
Child Feature
'''
