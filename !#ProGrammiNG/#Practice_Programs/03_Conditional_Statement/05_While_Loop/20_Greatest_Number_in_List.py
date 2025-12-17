# Wap to find the greatest number in a given list of integers.

li = [1,2,5,3,4]
i = 1
greatest = li[0]

while i<len(li):
    
    if li[i] > greatest:
        greatest = li[i]
        
    i+=1
print(greatest)
