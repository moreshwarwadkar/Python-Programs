# Create a generator that yields only positive numbers from a given list.

def gen():
    
    li = [1,2,-3,4,-5]
    
    for i in li:
 
        if i>=0:
            yield i
        
for i in gen():
    print(i)
