# Wap to find the smallest of 4 numbers

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))
d = int(input("Enter Number 4: "))

if a <= b and a <= c and a <= d:
    smallest = a
elif b <= a and b <= c and b <= d:
    smallest = b
elif c <= a and c <= b and c <= d:
    smallest = c
else:
    smallest = d

print("Smallest Number =", smallest)
