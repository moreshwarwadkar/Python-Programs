# GENERATOR : RIGHT AND WRONG WAYS


# ----- RIGHT WAY -----

def gen():

    i = 1

    while True:

        yield i
        i+=1

obj = gen()

print(next(obj))
print(next(obj))
print(next(obj))


'''
OPTPUT:

1
2
3
'''


# ----- WRONG WAY -----

def gen():

    i = 1

    while True:

        yield i
        i+=1

print(next(gen()))
print(next(gen()))
print(next(gen()))

'''
OUTPUT:

1
1
1
'''
