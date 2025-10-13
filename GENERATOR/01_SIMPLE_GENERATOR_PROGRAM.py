# GENERATOR

def add():

    print('Hie')
    yield 10

    print('Hello')
    yield 20

    print('Bye')
    yield 30

print(list(add()))
