# Wap to print all the characters present at even index of a string.

s = 'UNiK'
i = 0

while i < len(s):
    
    if i % 2 == 0:
        print(s[i])
        
    i+=1
