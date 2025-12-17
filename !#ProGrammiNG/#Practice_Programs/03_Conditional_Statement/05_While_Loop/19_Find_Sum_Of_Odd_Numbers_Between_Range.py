# Wap to find the sum of all the odd numbers between the given range.

s_range = int(input('Enter Starting Range:'))
e_range = int(input('Enter Ending Range:'))
sum = 0

if e_range < s_range:
    print('Invalid Range..!!')

else:
    
    while s_range <= e_range:
        
        if s_range % 2 != 0:
            sum+= s_range

        s_range+=1

    print('Sum:',sum)
