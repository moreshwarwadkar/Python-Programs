# Wap to check whether the data is single value data.

data = eval(input('Enter Data:'))

if type(data) in (int,float,bool,complex):
    print('Given Data is Single Value Data')
