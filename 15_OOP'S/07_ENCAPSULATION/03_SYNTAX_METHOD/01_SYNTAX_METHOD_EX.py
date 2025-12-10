# BY USING SYNTAX METHOD

# 1) OBJ/CLASS._CLASS_NAME__VAR/METHOD  : TO ACCESS
# 2) OBJ/CLASS._CLASS_NAME__VAR/METHOD = VALUE : TO MODIFY


class a:
    
    __name = 'UNiK'
    
    def __init__(self):
        self.__num = 100
        
    def dis_obj(self):
        print(self.__num)
        
    @classmethod
    def dis_cls(cls):
        print(cls.__name)
        
obj = a()
obj.dis_obj() # 100
print(obj._a__num) # 100
#print(a._a__num) --> It Will Through Error

obj.dis_cls() # UNiK
print(obj._a__name) # UNiK
print(a._a__name) # UNiK
