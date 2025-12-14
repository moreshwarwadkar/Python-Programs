# Write a generator that yields elements of a list one by one.

def gen():
    
    li = [1,2,3,4,5]
    
    for i in li:
        
        yield i
        
for i in gen():
    print(i)
