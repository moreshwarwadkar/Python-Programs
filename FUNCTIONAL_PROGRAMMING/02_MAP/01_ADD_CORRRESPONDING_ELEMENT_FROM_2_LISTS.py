#WAP TO ADD 10 TO EVERY VALUE IN THE COLLECTION.

li = [1,2,3,4,5]

def add(n):

    return n+10

a = map(add,li)
print(tuple(a))
