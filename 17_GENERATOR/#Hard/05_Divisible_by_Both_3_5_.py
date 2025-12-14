# Write a generator that yields numbers divisible by both 3 and 5 between 1 and 100..

def gen():
    
    for i in range(1,101):
        
        if i%3 == 0 and i%5 == 0:
            yield i
        
for i in gen():
    print(i)
