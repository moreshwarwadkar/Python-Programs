class BankAccount:

    def __init__(self):
        self.__name = 'Vinu'
        self.__balance = 0

    def get_name(self):
        print('Name:',self.__name)

    def get_balance(self):
        print('Balance:',self.__balance)

    def set_balance(self,amt):

        if amt >= 0:
            self.__balance += amt

        else:
            print('Invalid Amount..!!')

cust = BankAccount()

cust.set_balance(45000)
cust.get_name()
cust.get_balance()

'''
OUTPUT :

Name: Vinu
Balance: 45000
'''
