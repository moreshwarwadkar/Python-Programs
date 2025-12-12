class Vehicle:

    def __init__(self,brand,model):
        
        self.brand = brand
        self.model = model

    def info(self):
        print('Brand:',self.brand)
        print('Model:',self.model)

class Car(Vehicle):

    def __init__(self,brand,model,price):
        super().__init__(brand,model)   
        self.price = price

    def car_details(self):
        print(f'Price: {self.price}Rs.')

c = Car('Toyota','Fortuner',4800000)

c.info()
c.car_details()

'''
OUTPUT : 
Brand: Toyota
Model: Fortuner
Price: 4800000Rs.
'''
