# Wap to check whether the given data is mutable or immutable.

data = eval(input('Enter Data:'))

if isinstance(data,(str,tuple)):
    print('Data is Immutable')
    
else:
    print('Data is Mutable')
