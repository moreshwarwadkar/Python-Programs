# DEEP COPY

import copy

a = [1,[10,20],3]
b = copy.deepcopy(a)

print(a) # OP: [1, [10, 20], 3]
print(b) # OP: [1, [10, 20], 3]

b[0] = 10
print(a) # OP: [1, [10, 20], 3]
print(b) # OP: [10, [10, 20], 3]

b[1][0] = 1
print(a) # OP: [1, [10, 20], 3]
print(b) # OP: [10, [1, 20], 3]
