from abc import ABC, abstractmethod

class Payment(ABC):

    def transaction_status(self,msg):
        print('Status:',msg)

    @abstractmethod
    def pay(self,amt):
        pass

    @abstractmethod
    def refund(self,amt):
        pass

class UPI(Payment):

    def pay(self,amt):
        print(f'UPI Payment of {amt}Rs.')

    def refund(self,amt):
        print(f'UPI Refund of {amt}Rs.')

class CreaditCard(Payment):

    def pay(self,amt):
        print(f'CreaditCard Payment of {amt}Rs.')

    def refund(self,amt):
        print(f'CreaditCard Refund of {amt}Rs.')

u = UPI()
u.pay(500)
u.refund(200)
u.transaction_status('UPI Transaction Completed\n')

c = CreaditCard()
c.pay(1000)
c.refund(300)
c.transaction_status('CreaditCard Transaction Completed')

'''
OUTPUT : 

UPI Payment of 500Rs.
UPI Refund of 200Rs.
Status: UPI Transaction Completed

CreaditCard Payment of 1000Rs.
CreaditCard Refund of 300Rs.
Status: CreaditCard Transaction Completed
'''
