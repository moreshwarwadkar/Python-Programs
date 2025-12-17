# Wap to toggle a string.

s = input('Enter String:')
i = 0

while i < len(s):
    
    if 'A' <= s[i] <= 'Z':
        
        ch = chr(ord(s[i])+32)
        print(ch, end = '')
        
    elif 'a' <= s[i] <= 'z':
        
        ch = chr(ord(s[i])-32)
        print(ch, end = '')
        
    else:
        print(s[i], end = '')
    
    i+=1
