# SIMPLE GENERATOR PROGRAM

def add():

    print('Hii')
    yield 10

    print('Hello')
    yield 20

    print('Good Day!')
    yield 30

print(list(add()))

'''
OUTPUT:

Hii
Hello
Good Day!
[10, 20, 30]
'''
