# Wap to replace the space by * present in a string


s = 'UNi K'
new = ''

for i in s:
    
    if i == ' ':
        new += '*'
    else:
        new+= i
print(new)
 
