from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self._balance = balance
        
    @abstractmethod
    def display_account_details(self):
        pass

class SavingAccount(BankAccount):

    def __init__(self,account_holder,_balance):
        super().__init__(account_holder,_balance)
        self.__balance = _balance

    def get_balance(self):
        print('Saving Account Balance:',self.__balance)

    def set_balance(self,amt):

        if amt>=0:
            self.__balance += amt
            print(f'{amt} Added in Saving Account Successfully.')

        else:
            print('Invalid Amount..!')

    def __calculate_interest(self):
        interest = (self.__balance/100)*5
        print('Interest :',interest)

    def display_account_details(self):
        print('Account Holder:',self.account_holder)
        print('Bank Account Balance:',self._balance)

obj2 = SavingAccount('Sakshi',10000)

obj2.display_account_details()
obj2.set_balance(1000)
obj2.get_balance()
obj2._SavingAccount__calculate_interest()


'''
OUTPUT : 

Account Holder: Sakshi
Bank Account Balance: 10000
1000 Added in Saving Account Successfully.
Saving Account Balance: 11000
Interest : 550.0
'''
