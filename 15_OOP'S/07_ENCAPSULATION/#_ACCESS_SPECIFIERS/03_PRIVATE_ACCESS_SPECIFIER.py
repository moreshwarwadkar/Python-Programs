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

class a:
    
    __name = 'UNiK'
    
    def __init__(self):
        
        self.__num = 0
        
    def dis(self):
        print(self.__num)
        
    def mod_num(self,n):
        self.__num = n

    @classmethod
    def d_cls(cls):
        print(cls.__name)
        
    @classmethod
    def __dis_cls(cls):
        print(cls.__name)
        
    @classmethod
    def mod_name(cls,n):
        cls.__name = n
        
obj = a()

obj.mod_num(100)
obj.dis() # 100

obj.d_cls() # UNiK
obj.mod_name('Rohan') 
obj.d_cls() # Rohan

print(obj._a__num) # 100
# print(obj.a__name) -> It Will Through The Error..
print(a._a__name) # Rohan


obj._a__dis_cls()  # Works only if method starts with __  : Rohan
# obj._a__dis() -> It Will Through The Error..

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
