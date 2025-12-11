from abc import ABC, abstractmethod

class DeliveryPartner(ABC):

    @abstractmethod
    def deliver_order(self):
        pass

class Zomato(DeliveryPartner):

    def deliver_order(self):
        print('Food Delivered Successfully..!')

class Swiggy(DeliveryPartner):

    def deliver_order(self):
        print('Food Delivered Successfully..!')

obj1 = Zomato()
obj2 = Swiggy()

obj1.deliver_order()
obj2.deliver_order()

'''
OUTPUT :

Food Delivered Successfully..!
Food Delivered Successfully..!
'''
