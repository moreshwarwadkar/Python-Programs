# GETTER, SETTER METHOD 

class Product:
    
    def __init__(self):
        self.__name = None
        self.__price = 0
        self.__quantity = 0
        
    def set_name(self,name):
        
        if len(name) >= 3:    
            self.__name = name
       
        else:
            print('Invalid Product Name..!!')
            
    def set_price(self,price):
        
        if price > 0:
            self.__price = price

        else:
            print('Invalid Price..!!')
            
    def set_quantity(self,qty):
        
        if qty > 0:
            self.__quantity = qty
        
        else:
            print('Invalid Quantity..!!')
            
    def get_name(self):
        print('Product Name:',self.__name)
        
    def get_price(self):
        print('Price:',self.__price)
    
    def get_quantity(self):
        print('Quantity:',self.__quantity)
        
    def get_total_value(self):
        print('Total Value:',self.__price*self.__quantity)
        
obj = Product()

obj.set_name('Parle-G')
obj.set_price(10)
obj.set_quantity(100)

obj.get_name()
obj.get_price()
obj.get_quantity()
obj.get_total_value()
