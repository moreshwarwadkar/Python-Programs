# CONSTRUCTOR

class TCS:

    c_loc = 'Pune'
    c_ceo = 'Unik'

    def __init__(self,ename,esal):

        self.ename = ename
        self.esal = esal

emp = TCS('Rohit', 99500)

print(emp.ename)
print(emp.esal)

'''
OP:

Rohit
99500
'''
