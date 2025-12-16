# "Before function" before and "After function" after the function runs. Apply it to a function that prints "Processing".

def deco(func):
    def wrapper():
        
        print('Before Function..')
        func()
        print('After Function..')
        
    return wrapper

@deco
def a():
    
    print('Processing..')

a()

'''
OUTPUT:

Before Function..
Processing..
After Function..

'''
