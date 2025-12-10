class Employee:
    
    def __init__(self):
        
        self.__name = None
        self.__salary = 0 
        self.__experience = 0
        
    @property
    def name(self):
        return self.__name
   
    @property
    def salary(self):
        return self.__salary
    
    @property
    def experience(self):
        return self.__experience
    
    @name.setter
    def name(self, name):
        
        if len(name) >= 3:
            self.__name = name

    @salary.setter
    def salary(self,sal):
        
        if sal > 10000:
            self.__salary = sal

    @experience.setter
    def experience(self,exp):
        
        if exp >= 0:
            self.__experience = exp

obj = Employee()

obj.name = 'UNiK'
obj.salary = 12000
obj.experience = 3

print('Name:',obj.name)
print('Salary:',obj.salary)
print('Experience:',obj.experience)


'''
OUTPUT :

Name: UNiK
Salary: 12000
Experience: 3
'''
