# Wap to find the second greatest of 4 values.

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))
d = int(input("Enter Number 4: "))

if a >= b and a >= c and a >= d:
    greatest = a
elif b >= a and b >= c and b >= d:
    greatest = b
elif c >= a and c >= b and c >= d:
    greatest = c
else:
    greatest = d

if greatest == a:
    if b >= c and b >= d:
        second = b
    elif c >= b and c >= d:
        second = c
    else:
        second = d

elif greatest == b:
    if a >= c and a >= d:
        second = a
    elif c >= a and c >= d:
        second = c
    else:
        second = d

elif greatest == c:
    if a >= b and a >= d:
        second = a
    elif b >= a and b >= d:
        second = b
    else:
        second = d

else:
    if a >= b and a >= c:
        second = a
    elif b >= a and b >= c:
        second = b
    else:
        second = c

print("Second Greatest:", second)
