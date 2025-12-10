# ACCESS SPECIFIER : PRIVATE 

# EXAMPLE 1:

class a:
    
    def __init__(self):
        
        self.__num = 100
        
    def display(self):
        print(self.__num)
        
obj = a()
obj.display()

# OP : 100

# =============================================





# EXAMPLE 2:

class Bank:
    def __init__(self):
        self.__balance = 0   # Private variable

    def add(self, amount):
        self.__balance = amount

    def show(self):
        print(self.__balance)


b = Bank()
b.add(500)
b.show()

# Direct access (NOT allowed)
# print(b.__balance)   # This will give an error

# OP: 500

# =============================================




