# METHOD OVERLOADING

def add(a,b):
    sum = a+b
    return sum
temp1 = add # Storing the address of the function inside the variable called 'Monkey Patching'.

def add(a,b,c):
    sum = a+b+c
    return sum
temp2 = add # Monkey Patching

def add(a,b,c,d):
    sum = a+b+c+d
    return sum

print(temp1(10,20)) # 30
print(temp2(10,20,30))  # 60
print(add(10,20,30,40)) # 100
