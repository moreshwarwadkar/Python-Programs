# Create an iterator from a dictionary and print only its keys using iter() and next().

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

a = iter(d)  # To Display Only Key
#a = iter(d.values())  # To Display Values Only..
#a = iter(d.items())  # To Display Key-Value Pair

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
