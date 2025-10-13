#WAP TO EXTRACT ONLY EVEN VALUES FROM THE COLLECTION.

a = [1,2,3,4,5]

m = map(lambda n: n**2, list(filter(lambda n: n%2==0,a)))
print(list(m))
