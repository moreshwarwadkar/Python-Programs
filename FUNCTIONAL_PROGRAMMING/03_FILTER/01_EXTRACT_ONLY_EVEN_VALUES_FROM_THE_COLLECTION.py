#WAP TO EXTRACT ONLY EVEN VALUES FROM THE COLLECTION.

li = [1,2,3,4,5]

def even(n):

    if n%2==0:
        return n

def sq(n):

    return n**2

c = filter(even,li)

d = map(sq, list(c))
print(list(d))
