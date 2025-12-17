# Wap to check whether the number is Armstrong or not.
'''
153 → 1³ + 5³ + 3³ = 153 ✔
370 → 3³ + 7³ + 0³ = 370 ✔
9474 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 ✔
'''

num = int(input('Enter Number:'))
sum = 0
temp = num
count = len(str(num))

while num>0:
    
    rem = num % 10
    sum = sum+(rem**count)
    num = num // 10
    
if temp == sum:
    print('Given Number is Armstrong')

else:
    print('Given Number is Not Armstrong')
