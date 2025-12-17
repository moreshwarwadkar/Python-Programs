# Wap to remove duplicates from a list without converting into set.

li = [1,1,1,3,4,5,6,6,7,7,8,8,9]
i = 0
new = []

while i<len(li):
    
    if li[i] not in new:
        new.append(li[i])    
    
    i+=1
    
print(new)
