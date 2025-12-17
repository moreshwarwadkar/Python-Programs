# Wap to find the sum of individual digits of a number.

num = int(input('Enter Number:'))
sum = 0

while num>0:
    
    rem = num % 10
    sum = sum+rem
    num = num // 10
    
print('Sum:',sum)
