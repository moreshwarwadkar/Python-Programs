# SIMPLE DECORATOR PROGRAM

def my_decorator(func):
    def wrapper():  # WITHOUT PASSING ANY ARGUMENTS

        print('Before Function Runs')
        func()
        print('After Function Runs')

    return wrapper

@my_decorator
def say_hello():
    print('Hello!')

say_hello()

'''
OUTPUT :

Before Function Runs
Hello!
After Function Runs
'''
