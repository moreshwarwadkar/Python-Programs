# SIMPLE EXAMPLE : PROTECTED ACCESS SPECIFIER


# EXAMPLE 1:

class Person:
    def __init__(self):
        self._age = 20   # Protected variable


p = Person()

# Accessing protected variable (allowed but not recommended)
print(p._age)

# OP : 20
# ==========================================================





# EXAMPLE 2 :

class BankAccount:
    def __init__(self, balance):
        self._balance = balance     # Protected variable

    def show_balance(self):
        print("Balance (inside class):", self._balance)


class SavingsAccount(BankAccount):
    def display_balance(self):
        print("Balance (inside child class):", self._balance)


# Creating object of child class
account = SavingsAccount(5000)

# Accessing protected variable through class methods
account.show_balance()
account.display_balance()

# Accessing protected variable directly (possible but NOT recommended)
print("Balance (outside class):", account._balance)

'''
OUTPUT :
Balance (inside class): 5000
Balance (inside child class): 5000
Balance (outside class): 5000
'''
# ==========================================================




