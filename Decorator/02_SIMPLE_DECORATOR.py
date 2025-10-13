# SIMPLE DECORATOR PROGRAM

def decor(func):
    def inner():
        print("Before function")
        func(*args)
        print("After function")
    return inner

@decor
def show(a,b):
    print("Hello World")
    print("Hello World")
    print("Hello World")

show()
