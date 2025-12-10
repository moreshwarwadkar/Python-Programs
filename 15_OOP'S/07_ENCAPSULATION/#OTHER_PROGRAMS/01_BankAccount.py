class BankAccount:
    
    def __init__(self):
        self.__balance = 0
        self.__account_holder = input('Enter Name:')
        
    def deposit(self):
        
        amt = int(input('Deposit Amount:'))
        self.__balance = self.__balance+amt
        print(f'{self.__balance} Amount Added Successfully')

    def withdraw(self):
        
        amt = int(input('Withdraw Amount:'))
        
        if amt <= self.__balance:
            self.__balance -= amt
            print(f'{amt} Amount Withdrawn Successfully')
        
        else:
            
            print('Add Amount First')
            
    def show_balance(self):
        print('Current Balance:',self.__balance)
        
    def __secret_message(self):
        return 'This is Black Mony..!'
        
    def reveal_secret(self):
        msg = self.__secret_message()
        return msg
    
obj = BankAccount()

obj.deposit()
obj.withdraw()
obj.show_balance()

print(obj._BankAccount__balance)
print(obj._BankAccount__secret_message())  # This is Black Mony..!

print(obj.reveal_secret()) # This is Black Mony..!
