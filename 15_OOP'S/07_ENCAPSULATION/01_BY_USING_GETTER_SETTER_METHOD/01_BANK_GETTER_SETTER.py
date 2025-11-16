# ENCAPSULATION : GETTER AND SETTER METHOD

class BankAccount:

    def __init__(self,bal):
        self.__bal = bal    # Here we create Privete Variable


    #Getter
    def get_bal(self):
        print('Current Balance:',self.__bal)


    #Setter
    def deposit(self,amt):

        if amt > 0:

            self.__bal = self.__bal+amt

        else:

            print('Invalid Amount')

acc = BankAccount(100)

acc.get_bal()
acc.deposit(500)

print('\n--- After Deposit ---')
acc.get_bal()


'''
OUTPUT:

Current Balance: 100

--- After Deposit ---
Current Balance: 600
'''
