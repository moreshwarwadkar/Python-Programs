# Wap to print ‘Fizz’ if the given number is multiple of three 
# print ‘buzz’ if the given number is multiple of 5 and 
# print ‘Fizzbuzz’ if the number is multiple of both 3 and 5.

num = int(input('Enter Any Number:'))
    
if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')

elif num % 3 == 0:
    print('Fizz')

elif num % 5 == 0:
    print('Buzz')
    
else:
    print('Not Divisible by Both')
