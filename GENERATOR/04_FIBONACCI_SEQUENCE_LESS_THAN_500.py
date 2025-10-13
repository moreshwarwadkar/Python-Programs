'''
4. Write a generator function that yields the next Fibonacci number on each iteration without storing 
whole sequence. Then print only numbers less than 500.
'''

def fib():
    
    f1, f2 = 0, 1

    while True:            # infinite generator

        yield f1           # yield one number at a time
        f1, f2 = f2, f1+f2 # update values


for num in fib():

    if num < 500:          # stop condition

        print(num)

    else:

        break              # stop when number ≥ 500
