# Wap to print the middle value of a list only if it is string.

li = [1,2,'Unik',4,5]

if len(li) % 2 != 0:
    
    if type(li[len(li)//2]) == str:
        print(li[len(li)//2])
        
    else:
        print('Middle Value is Not a String')

else:
    print('List Does Not Consist Middle Value')
