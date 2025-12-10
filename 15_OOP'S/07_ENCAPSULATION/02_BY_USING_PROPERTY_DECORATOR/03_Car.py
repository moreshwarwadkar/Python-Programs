class Car:
    
    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__year = 0
        self.__price = 0
        
    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model
    
    @property
    def year(self):
        return self.__year
    
    @property
    def price(self):
        return self.__price
    
    @brand.setter
    def brand(self,brand):
        self.__brand = brand

    @model.setter
    def model(self,model):
        self.__model = model

    @year.setter
    def year(self,year):
        self.__year = year

    @price.setter
    def price(self,price):
        self.__price = price

obj = Car()

obj.brand = 'BMW'
obj.model = 'BMW 7 Series (Sedan)'
obj.year = 2026
obj.price = 17900000

print('Brand Name:',obj.brand)
print('Model Name:',obj.model)
print('Year:',obj.year)
print('Price:',obj.price)

'''
OUTPUT :

Brand Name: BMW
Model Name: BMW 7 Series (Sedan)
Year: 2026
Price: 17900000
'''
