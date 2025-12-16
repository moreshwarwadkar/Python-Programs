# Wap to find the smallest of 3 numbers.

num1 = int(input('Enter Number 1:'))
num2 = int(input('Enter Number 2:'))
num3 = int(input('Enter Number 3:'))

if num1 < num2 and num1 < num3:
    print('Number 1 is Smallest')

elif num2 < num1 and num2 < num3:
    print('Number 2 is Smallest')
    
else:
    print('Number 3 is Smallest')
