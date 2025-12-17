# Wap to extaract all the even integers present in a tuple at odd index.

t = (1,22,21,23,45,3,5,4,5,6,6,7,7,42)
i = 0

while i<len(t):
    
    if i % 2 != 0:
        
        if t[i] % 2 == 0:
            print(t[i])
    i+=1
