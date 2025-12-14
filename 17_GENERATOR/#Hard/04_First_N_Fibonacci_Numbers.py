# Write a generator to generate the first n Fibonacci numbers.

def gen():
    
    n = int(input('Enter Any Number:'))
    
    fib1, fib2 = 0,1
    
    for i in range(n):
        
        yield fib1
        fib1, fib2 = fib2, fib1+fib2

for i in gen():
    print(i)
