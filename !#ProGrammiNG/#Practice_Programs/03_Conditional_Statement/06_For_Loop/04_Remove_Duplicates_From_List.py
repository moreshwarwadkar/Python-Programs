# Wap to remove duplicates from list 

li = [1,2,2,3,4,4,5]
new = []

for i in li:
    
    if i not in new:
        new.append(i)
print(new)
