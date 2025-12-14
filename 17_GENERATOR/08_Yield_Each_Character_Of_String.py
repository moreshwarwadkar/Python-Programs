# Write a generator that yields each character of a given string one by one.

def gen():
    
    s = 'UNiK'
    for i in s:
        
        yield i
        
for i in gen():
    print(i)
