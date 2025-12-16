# Write a decorator that prints "Function started" before a function executes. Apply it to a function say_hello() that prints "Hello".

def deco(func):
    def wrapper():
        
        print('Function Started..')
        func()
    return wrapper
        
@deco
def greet():
    print('Hello..')
greet()

'''
OUTPUT :

Function Started..
Hello..
'''
