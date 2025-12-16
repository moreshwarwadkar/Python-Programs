# Write a decorator that prints "Function ended" after a function executes. Apply it to a function that prints "Bye".

def deco(func):
    def wrapper():
        
        func()
        print('Function Ended..')
        
    return wrapper

@deco
def greet():
    
    print('Byeee..')
    
greet()

'''
OUTPUT :

Byeee..
Function Ended..
'''
