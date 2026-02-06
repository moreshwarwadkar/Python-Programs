# COUNT NUMBER OF OCCURANCE OF WORDS

s = 'dog cat dog'
d = {}

for i in s.split():

    if i in d:
        d[i] += 1

    else:
        d[i] = 1

print(d)
