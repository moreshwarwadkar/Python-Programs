from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass


class UPIPayment(Payment):

    def pay(self):
        print('UPI Payment Successfull..!!')

    def refund(self):
        print('UPI Payment Refund\n')
        

class CardPayment(Payment):

    def pay(self):
        print('Card Payment Successfull..!!')

    def refund(self):
        print('Card Payment Refund\n')


class WalletPayment(Payment):

    def pay(self):
        print('Wallet Payment Successfull..!!')

    def refund(self):
        print('Wallet Payment Refund\n')


obj1 = UPIPayment()
obj2 = CardPayment()
obj3 = WalletPayment()

obj1.pay()
obj1.refund()

obj2.pay()
obj2.refund()

obj3.pay()
obj3.refund()

'''
OUTPUT : 

UPI Payment Successfull..!!
UPI Payment Refund

Card Payment Successfull..!!
Card Payment Refund

Wallet Payment Successfull..!!
Wallet Payment Refund
'''
