# Wap to find the greatest of 4 numbers.

num1 = int(input('Enter Number 1: '))
num2 = int(input('Enter Number 2: '))
num3 = int(input('Enter Number 3: '))
num4 = int(input('Enter Number 4: '))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print('Number 1 is Greatest')

elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print('Number 2 is Greatest')

elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print('Number 3 is Greatest')

else:
    print('Number 4 is Greatest')
