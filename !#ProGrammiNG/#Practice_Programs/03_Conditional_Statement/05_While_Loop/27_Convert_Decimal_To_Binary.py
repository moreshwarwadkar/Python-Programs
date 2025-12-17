# Wap to convert decimal to binary.

num = int(input("Enter Decimal Number: "))
n = num
binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        rem = num % 2
        binary = str(rem) + binary   # add at front
        num = num // 2

print("Binary:", binary)
