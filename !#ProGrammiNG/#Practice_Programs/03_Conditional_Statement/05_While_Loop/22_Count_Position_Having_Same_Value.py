# Wap to get the following output:
# A=’10011100’ B=’00110101’ out=4(count of positions having same values)

a = '10011100'
b = '00110101'

i = 0
count = 0

while i<len(a):
    
    if a[i] == b[i]:
        count += 1
    i+=1
print('Count:',count)
