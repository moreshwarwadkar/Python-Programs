# Write a generator that yields numbers from 1 to n.

def gen():
    
    n = int(input('Enter Any Number:'))
    for i in range(1,n+1):
        yield i

for i in gen():
    print(i)
