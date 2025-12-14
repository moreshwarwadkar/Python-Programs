# Write a generator that yields the square of numbers from 1 to 10.

def gen():
    
    for i in range(1,11):
        
        yield i**2

a = gen()
        
for i in a:
    print(i)
