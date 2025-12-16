# Consider a tuple of length 2 and check whether the tuple is homogenous or not

t = (1,2)

if type(t[0]) == type(t[1]):
    print('Tuple is Homogenous')
    
else:
    print('Tuple is Not Homogenious')
