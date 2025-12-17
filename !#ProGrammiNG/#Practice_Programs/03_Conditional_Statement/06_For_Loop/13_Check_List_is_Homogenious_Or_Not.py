# Wap to check whether the list is homogenous or not.

li = [1,'Two',(3),{4}]

for i in li:
    
    if type(li[0]) != type(i):
        print('List is Not Homogenious')
        break

else:
    print('List is Homogenious')
