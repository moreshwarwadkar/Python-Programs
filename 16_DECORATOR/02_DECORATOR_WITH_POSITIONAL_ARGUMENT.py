# DECORATOR WITH POSITIONAL ARGUMENT:


def my_decorator(func):
    def wrapper(*args):  # Only POSITIONAL ARGUMENT

        print('Before Functin')
        result = func(*args)
        print('After Function')
        return result
    return wrapper

@my_decorator
def multiply(a,b,c):
    return a*b*c

print(multiply(2,3,4))

'''
OUTPUT:

Before Functin
After Function
24
'''


# ----- ANOTHER METHOD -----

def my_decorator(func):
    def wrapper(*args):  

        print('Before Functin')
        return func(*args)
        print('After Function')  # But it will not display.
    return wrapper

@my_decorator
def multiply(a,b,c):
    return a*b*c

print(multiply(2,3,4))

'''
OUTPUT:

Before Functin
24
'''
