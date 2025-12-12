class OrderProcess:

    def __init__(self,customer_name,order_amount,discount_code):
        self.customer_name = customer_name
        self.order_amount = order_amount
        self.discount_code = discount_code

    @staticmethod
    def validate_discount(order_amount,code):

        if code == 'NEW50':
            return order_amount-((50/100)*order_amount)

        elif code == 'SAVE10':
            return order_amount-((10/100)*order_amount)

        elif code == 'OFF5':
            return order_amount-((5/100)*order_amount)

        else:
            return order_amount

    def final_amount(self):

        final_amount = self.validate_discount(self.order_amount,self.discount_code)
        print('Final Amount:',final_amount)

ord1 = OrderProcess('Mandar',1000,'NEW50')
ord2 = OrderProcess('Ajay',800,'SAVE10')
ord3 = OrderProcess('Sandy',1200,'OFF5')

ord1.final_amount()
ord2.final_amount()
ord3.final_amount()

'''
OUTPUT : 

Final Amount: 500.0
Final Amount: 720.0
Final Amount: 1140.0

'''
