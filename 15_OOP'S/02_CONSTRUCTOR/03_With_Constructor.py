class Student:

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def show(self):
        print('Name:',self.name)
        print('Age:',self.age)

st1 = Student('Unik',21)
st1.show()
#OutPut
#Name: Unik
#Age: 21

st2 = Student('ROhan',20)
st2.show()
#OutPut
#Name: ROhan
#Age: 20
