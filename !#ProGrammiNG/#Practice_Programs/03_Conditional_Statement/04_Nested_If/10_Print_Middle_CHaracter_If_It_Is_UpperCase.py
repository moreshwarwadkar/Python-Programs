# Write a program to print middle Character of the given string only if it is upperCase Character.

s = 'RoHan'

middle_char = s[len(s)//2]

if len(s)%2 != 0:
    
    if 'A' <= middle_char <= 'Z':

        print(middle_char)
    
    else:
        print('Middle Character is Not UpperCase')
    
else:
    print('There is No Middle Character')
