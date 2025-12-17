# Wap to find the common elements in two sets

s1 = {1, 2, 3, 4, 5}
s2 = {5, 6, 7, 8, 9}

l1 = list(s1)
l2 = list(s2)

i = 0
common = []

while i < len(l1):
    j = 0
    while j < len(l2):
        if l1[i] == l2[j]:
            common.append(l1[i])
        j += 1
    i += 1

print("Common elements:", common)
