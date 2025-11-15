# SIMPLE GENERATOR:

'''
def gen():
    yield 1
    yield 2
    yield 3

for num in gen():  # Here we directly use Function
    print(num)
'''

'''
OUTPUT:
1
2
3
'''

# ----- ANOTHER METHOD -----

def gen():
    yield 1
    yield 2
    yield 3
    
a = gen()  # Store the Generator in a Variable

for num in a:
    print(num)

'''
OUTPUT:
1
2
3
'''
