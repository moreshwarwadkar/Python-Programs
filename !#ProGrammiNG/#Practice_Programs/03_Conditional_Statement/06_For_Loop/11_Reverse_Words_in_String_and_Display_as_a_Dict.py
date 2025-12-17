# Wap to get the following output.
# S=’power star’
# Out={‘power’:’rewop’,’star’:’rats’}

s = 'Power Star'
sp = s.split()
dict = {}

for i in sp:
    
    dict[i] = i[::-1]
    
print(dict)
