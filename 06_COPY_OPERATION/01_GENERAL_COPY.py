# GENERAL COPY

a = [1,2,3,4,5]
b = a

print(a) # OP: [1, 2, 3, 4, 5]
print(b) # OP: [1, 2, 3, 4, 5]

print(id(a)) # OP: 2966112392768
print(id(b)) # OP: 2966112392768

b[1] = 20

print(a) # OP: [1, 20, 3, 4, 5]
print(b) # OP: # OP: [1, 20, 3, 4, 5]


'''
The case of mutable values, if they are modify value
inside the collection, it will affect both the variables
'''
