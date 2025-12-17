# Wap to count the number of words in a string.

s = input('Enter String:')
st = s.split()
i = 0
count = 0

while i<len(st):
    
    count+=1
    i+=1
    
print('Number of Words:',count)
