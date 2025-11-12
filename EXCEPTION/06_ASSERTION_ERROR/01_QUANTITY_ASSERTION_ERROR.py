stock = 10

qty = int(input('Enter The Quantity:'))

assert qty <= stock , 'Out Of Stock'
print('Order Placed')
