# Write a decorator that measures and prints the execution time of a function.
# Apply it to a function that runs a simple loop.

import time

def deco(func):
    def wrapper():
        
        start_time = time.time()
        func()
        end_time = time.time()
        
        print('Execution Time:',end_time - start_time)
    return wrapper
        
@deco
def a():
    
    for i in range(1,6):
        print(i)

a()
