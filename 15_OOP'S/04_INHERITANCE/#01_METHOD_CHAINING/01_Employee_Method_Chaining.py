class Employee:

    def show_salary(self,base_salary):
        print(f'Base Salary: {base_salary} Rs.')

class Manager(Employee):

    def show_salary(self,base_salary):

        super().show_salary(base_salary) # METHOD CHAINING
        bonus = base_salary * 0.20

        print(f'Bonus: {bonus} Rs.')
        print(f'Total Salary: {base_salary + bonus} Rs.')

m = Manager()
m.show_salary(50000)

'''
OUTPUT :

Base Salary: 50000 Rs.
Bonus: 10000.0 Rs.
Total Salary: 60000.0 Rs.
'''
