class Laptop:

    def __init__(self):
        self.brand = input('Enter Brand Name:')
        self.ram = input('Enter RAM:')
        self.price = int(input('Enter Price:'))

    def details(self):
        print('Brand:',self.brand)
        print('RAM:',self.ram)
        print('Price:',self.price)

obj1 = Laptop()
obj2 = Laptop()

obj1.details()
obj2.details()
