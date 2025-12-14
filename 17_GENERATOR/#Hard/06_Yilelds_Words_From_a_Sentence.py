# Write a generator that yields words from a given sentence one by one.

def gen():
    
    s = 'I am Mr Unik'
    
    st = s.split(' ')
    
    for i in st:
        yield i
        
for i in gen():
    print(i)
