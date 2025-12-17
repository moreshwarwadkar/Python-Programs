# wap to extract all the non default values from a list.

li = [1,(),False,True,3.5,(5)]

for i in li:
    
    if bool(i) == True:
        print(i)

# Similar [ Here We Directly Check ]

li = [1,(),False,True,3.5,(5)]

for i in li:
    
    if i:
        print(i)
