# Wap to extract all the vowels present in a string.

s = 'UNiK'
i = 0

while i < len(s):
    
    if s[i] in 'aeiouAEIOU':
        print(s[i])
    i+=1
