# Create an iterator that iterates over a string character by character.

# First Way :

s = 'UNiK'
a = iter(s)

print(next(a))
print(next(a))
print(next(a))
print(next(a))

# Second Way : Most Prefered When we have large data.

li = 'UNiK'
a = iter(li)

while True:
    try:
        print(next(a))
    except StopIteration:
        break
