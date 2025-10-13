# EXTRACT ONLY INTEGER FROM COLLECTION.

def collection():

    li = [1,2,3,4,5,'Hie',5,6,4,5]

    for i in li:

        if type(i) == int:

            yield i

print(list(collection()))
