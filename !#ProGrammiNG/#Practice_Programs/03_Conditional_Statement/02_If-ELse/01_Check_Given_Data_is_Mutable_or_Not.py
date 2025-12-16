# Wap to check whether the data is mutable or not.

data = eval(input('Enter Data:'))

if isinstance(data,(str,tuple)):
    print('Given Data is Mutable')

else:
    print('Given Data is Not Mutable')
