#  Wap to check whether the char is uppercase, lowercase, digit or special char

ch = input('Enter Character:')

if 'A' <= ch <= 'Z':
    print('Character is Uppercase')

elif 'a' <= ch <= 'z':
    print('Character is Lowecase')

elif '0' <= ch <= '9':
    print('Character is Digit')
    
else:
    print('Special Character')
