# Wap to check whether the number is palindrome or not.

num  = int(input('Enter Number:'))
temp = num
rev = 0

while num > 0:
    
    rem = num % 10
    rev = rev*10+rem
    num = num // 10
    
if temp == rev:
    print('Number is Palindrome')

else:
    print('Number is Not Palindrome')
