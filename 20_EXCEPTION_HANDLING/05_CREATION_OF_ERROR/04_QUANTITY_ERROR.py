class QuantityError(Exception):

    pass

stock = 10

qty = int(input('Enter Quantity:'))

if qty <= stock:

    print('Order Placed')

else:

    raise QuantityError('Out Of Stock')
