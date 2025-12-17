# Wap to convert binary to decinaml.

'''
Binary number = powers of 2

Example:
1011
= 1×2³ + 0×2² + 1×2¹ + 1×2⁰
= 8 + 0 + 2 + 1 = 11
'''

binary = input("Enter Binary Number: ")
i = len(binary) - 1
power = 0
decimal = 0

while i >= 0:
    if binary[i] == '1':
        decimal += 2 ** power
    power += 1
    i -= 1

print("Decimal:", decimal)
