# Wap to extract all the key value pairs from the dictionary only if the keys are of string datatype and values are integers.

dict = {'a':1, 2:'b', 'c':3, 4:'d'}
new = {}

key = dict.keys()
value = dict.values()

for i,j in zip(key,value):

    if type(i) == str and type(j) == int:
        print(f'{i}:{j}')
        
# Another Way To Extract:
        
d = {'a':1, 2:'b', 'c':3, 4:'d'}
new = {}

for i, j in d.items():
    if type(i) == str and type(j) == int:
        print(f'{i}:{j}')
