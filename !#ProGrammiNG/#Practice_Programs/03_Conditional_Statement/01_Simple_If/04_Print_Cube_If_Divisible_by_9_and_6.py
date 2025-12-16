# Wap to print the cube of a number only if it is divisible by 9 or 6.

num = int(input('Enter Any Number:'))

if num%9 == 0 and num%6 == 0:
    print(num**3)
    
