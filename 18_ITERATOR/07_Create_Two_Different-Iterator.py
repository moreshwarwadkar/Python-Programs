# Create two different iterators from the same list and prove that they work independently using next().

li = [1,2,3,4,5]

a = iter(li)
b = iter(li)

print(next(a)) # 1
print(next(a)) # 2

print(next(b)) # 1
print(next(b)) # 2
print(next(b)) # 3

'''
OUTPUT : 

1
2
1
2
3
'''
