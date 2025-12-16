# Create an iterator from a tuple and print all its elements using iter() and next() with proper exception handling.

t = (10,20,30,40,50)

a = iter(t)

while True:
    
    try:
        print(next(a))
    
    except StopIteration:
        break
    
