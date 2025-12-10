class Student:
    
    def __init__(self):
        self.__name = None
        self.__age = None
        self.__marks = []
        
    def set_details(self,name,age):
        
        if age >= 5:
            self.__age = age
            self.__name = name
        
        else:
            print('Invalid Age..!!')    
    
    def add_marks(self,m1,m2,m3):
        
        if all(0 < a <= 100 for a in [m1,m2,m3]):
            self.__marks = [m1,m2,m3]
            # self.__marks.append(m1)
            # self.__marks.append(m2)
            # self.__marks.append(m3)
            
        else:
            print('Invalid Marks..!!')
            
    def show_details(self):
        
        print('Name: ',self.__name)
        print('Age: ',self.__age)
        print('Marks: ',self.__marks)

        avg = self.__calculate_average()        
        print('Average: ',avg)
        
    def __calculate_average(self):
        
        if len(self.__marks) == 0:
            return 0
        
        avg = sum(self.__marks)/len(self.__marks)
        return avg
    
    def get_average(self):
        
        return  self.__calculate_average()
    
obj = Student()

obj.set_details('Rohan',21)
obj.add_marks(99,95,100)
obj.show_details()

print(obj._Student__marks)
print(obj._Student__calculate_average())
obj.get_average()

'''
OUTPUT : 

Name:  Rohan
Age:  21
Marks:  [99, 95, 100]
Average:  98.0
[99, 95, 100]
98.0

'''
