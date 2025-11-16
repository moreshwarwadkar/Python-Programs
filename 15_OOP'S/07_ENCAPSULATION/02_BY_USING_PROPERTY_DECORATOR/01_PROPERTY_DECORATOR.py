# ENCAPSULATION : BY USING @PROPERTY DECORATOR

class Student:

    def __init__(self,marks):

        self.__marks = marks

    @property   # @property converts this method into a getter
    def marks(self):

        return self.__marks

    @marks.setter   # @marks.setter Converts method into setter
    def marks(self,value):

        if value >=0:
            self.__marks = value

        else:
            print('Invalid Marks')

s = Student(80)

print(s.marks)  # 80 (Access Like Variable)

s.marks = 95    # (Modify Like Variable)
print(s.marks)  # 95
