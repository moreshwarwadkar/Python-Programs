# CLASS METHOD:

class product:

    tax_rate = 0.18

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def show_details(self,):
        print(f'Product: {self.name}')
        print(f'Price: {self.price}')

    @classmethod
    def update_tax(cls,new_tax):
        cls.tax_rate = new_tax

    @classmethod
    def show_tax(cls):
        print('Tax Rate: ',cls.tax_rate)

p1 = product('Mobile',15000)

p1.show_details()  

print('Current Tax: ',product.tax_rate)

product.show_tax()
product.update_tax(100)
product.show_tax()

#ALSO WE CAN ACCESS CLASS METHOD USING CLASS OBJECT.
'''
p1.show_tax()
p1.update_tax(100)
p1.show_tax()
'''


'''
OUTPUT:

Product: Mobile
Price: 15000
Current Tax:  0.18
Tax Rate:  0.18
Tax Rate:  100
'''
