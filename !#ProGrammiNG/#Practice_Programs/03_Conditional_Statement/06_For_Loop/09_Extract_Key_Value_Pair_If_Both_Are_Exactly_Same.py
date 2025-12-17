# Wap to extract key value pairs from the dictionary only if both keys and values are exactly same

dict = {'a':1, 2:'b', 'c':'c', 4:'d'}

for i,j in dict.items():
    
    if i == j:
        print(f'{i}:{j}')
