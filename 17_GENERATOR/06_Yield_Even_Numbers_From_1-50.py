# Write a generator that yields even numbers between 1 and 50.

def gen():
    
    for i in range(1,51):
        
        if i%2 == 0:
            yield i
            
for i in gen():
    print(i)
