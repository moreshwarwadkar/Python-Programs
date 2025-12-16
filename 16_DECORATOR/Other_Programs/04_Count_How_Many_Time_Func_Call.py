# Write a decorator that counts how many times a function is called and prints the count each time the function runs. 
# Apply it to a function that prints "Hello".

def deco(func):

    count = 0
    
    def wrapper():
        
        nonlocal count
        func()
        count+=1
        print(count)
        
    return wrapper        

@deco
def greet():
    
    print('Hello..')
    
greet()
greet()
