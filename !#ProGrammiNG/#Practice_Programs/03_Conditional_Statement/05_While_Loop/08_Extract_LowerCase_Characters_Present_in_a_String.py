# Wap to extract all the lowercase characters present in a string.

s = 'UNiK'
i = 0

while i<len(s):
    
    if 'a' <= s[i] <= 'z':
        
        print(s[i])
        
    i+=1
