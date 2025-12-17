# wap to extract all the lowercase characters in a string only if the ascii value is even.

s = input('Enter String:')

for i in s:
    
    if 'a' <= i <= 'z':
        
        if ord(i) % 2 == 0:
            print(i, end=' ')
