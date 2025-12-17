# Wap to check the given number is prime or not.

num = int(input('Enter Number: '))
i = 2

if num > 1:
    while i < num:
        
        if num % i == 0:
            print('Not a Prime Number')
            break
        
        i += 1
    else:
        print('Prime Number')
else:
    print('Not a Prime Number')
