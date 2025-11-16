# STATIC METHOD

class bank:

    b_name = 'IDBI'
    b_branch = 'Satara'

    def __init__(self, c_name, c_add, c_bal=1000):
        self.c_name = c_name
        self.c_add = c_add
        self.c_bal = c_bal

    def show_cust(self):
        print('\nCustomer Name:',self.c_name)
        print('Customer Address:',self.c_add)
        print('Customer Balance:',self.c_bal)


    @classmethod
    def show_bank(cls):
        print('Bank Name:',cls.b_name)
        print('Bank Branch:',cls.b_branch)

    def deposit(self,amt):
        self.c_bal = self.add(self.c_bal,amt)

    @staticmethod
    def add(a,b):
        return a+b

c1 = bank('Unik','Satara')

c1.show_bank()
c1.show_cust()
c1.deposit(4000)
c1.show_cust()

'''
OUTPUT:

Bank Name: IDBI
Bank Branch: Satara

Customer Name: Unik
Customer Address: Satara
Customer Balance: 1000

Customer Name: Unik
Customer Address: Satara
Customer Balance: 5000
'''
