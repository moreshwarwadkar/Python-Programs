# Wap to count the number of occurrence of a specified character.

s = input('Enter String:')
ch = input('Enter Character To Count:')
count = 0

for i in s:
    
    if i == ch:
        count+=1
print(f'Occurance of "{ch}" is {count}')
