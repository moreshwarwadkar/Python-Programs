'''
Write a generator that keeps producing natural numbers starting from 1.
(It will keep generating numbers until you stop it.)

Example Usage:

gen = infinite_numbers()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
'''

def gen():

    i=1
    
    while True:

        yield i
        i+=1

print(next(gen()))
print(next(gen()))
