# Wap to find the sum of cube of a number in a string.

data = input('Enter String:')
i = 0
sum = 0

while i<len(data):
    
    if '0' <= data[i] <= '9':
        sum = sum + int(data[i])**3
    i+=1
    
print('Sum:',sum)
