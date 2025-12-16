# Wap to check whether the given integer is single digit or two digits or three digits or more than three digits.

num = int(input('Enter Digit:'))

if len(str(num)) == 1:
    print('Number is Single Digit')
    
elif len(str(num)) == 2:
    print('Number is Two Digit')

elif len(str(num)) == 3:
    print('Number is Three Digit')
    
else:
    print('Number is More Than Three Digit')
