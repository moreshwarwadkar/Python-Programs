# Wap to get the following output using len function.
# S=’power star’
# Out={‘power’:5,’star’:4}

s = 'Power Star'
sp = s.split()

for i in sp:
    print(f'{i} : {len(i)}')
