# Wap to find the HCF of two numbers. [ HCF : HIGHEST COMMON FACTOR ]

'''
Find HCF of 12 and 18

Factors:

12 → 1, 2, 3, 4, 6, 12
18 → 1, 2, 3, 6, 9, 18

Common factors → 1, 2, 3, 6
Highest = 6

So HCF = 6
'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

i = 1
hcf = 1

small = a if a < b else b

while i <= small:
    if a % i == 0 and b % i == 0:
        hcf = i 
    i += 1

print("HCF :", hcf)
