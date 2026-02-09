# SHALLOW COPY

import copy

a = [1,[10,20],3]
b = copy.copy(a)

print(a) # OP: [1, [10, 20], 3]
print(b) # OP: [1, [10, 20], 3]

b[1][0] = 1

print(a) # OP: [1, [1, 20], 3]
print(b) # OP: [1, [1, 20], 3]


b[0] = 10

print(a) # OP: [1, [1, 20], 3]
print(b) # OP: [10, [1, 20], 3]

'''
- The Nested collection stored in the same address.
- So if we modify the value from nested collection, it will affect for both variables.
'''
