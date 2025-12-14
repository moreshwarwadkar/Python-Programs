# Convert the following list comprehension into a generator expression:
# [i**2 for i in range(1, 11)]

gen = (i**2 for i in range(1, 11))

for i in gen:
    print(i)
