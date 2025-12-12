class Employee:

    company = 'Google'

    def __init__(self,name,salary):

        self.name = name
        self.salary = salary

    def show(self):                # -- Object Method
        print('\nName:',self.name)
        print('Salary:',self.salary)
        print('Company:',Employee.company)

    #def update_comp(company):
    #   Employee.company = company

    #@classmethod
    #def change_com(cls,company):  # -- Class Method
    #    cls.company = company

emp1 = Employee('Pranav',45000)
emp2 = Employee('Atharv',35000)

emp1.show()
emp2.show()

#emp1.update_comp('EduPluse')  --> Method 1
#emp1.show()

#emp1.change_comp('EduPluse')  --> Method 2
#emp1.show()

Employee.company = 'EduPluse' #--> Method 3 : With help of that we can change class variable for all object.

emp1.show()
emp2.show()
