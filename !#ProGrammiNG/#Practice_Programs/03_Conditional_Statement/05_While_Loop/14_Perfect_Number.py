# Wap to check whether the number is perfect or not.

# 6 → factors: 1, 2, 3 → sum = 6 → perfect ✔️
# 28 → factors: 1, 2, 4, 7, 14 → sum = 28 → perfect ✔️

num = int(input('Enter Number:'))
i = 1
sum = 0
while i<num:
    
    if num % i == 0:    
        sum = sum + i
    i+=1
    
if num == sum:
    print('Number is Perfect')

else:
    print('Number is Not Perfect')
