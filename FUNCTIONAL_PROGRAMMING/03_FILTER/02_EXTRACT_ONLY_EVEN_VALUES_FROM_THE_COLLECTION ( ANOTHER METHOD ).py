#WAP TO EXTRACT ONLY EVEN VALUES FROM THE COLLECTION.

li = [1,2,3,4,5]

even = lambda n : n%2==0
sq = lambda n : n**2

a = filter(even,li)
b = map(sq,list(a))

print(list(b))
