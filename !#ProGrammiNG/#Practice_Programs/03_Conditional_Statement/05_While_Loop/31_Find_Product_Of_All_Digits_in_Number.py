# Wap to find the product of all the digits present in a number.

num = int(input('Enter Number: '))
prod = 1

while num > 0:
    rem = num % 10
    prod = prod * rem
    num = num // 10

print("Product of digits:", prod)
