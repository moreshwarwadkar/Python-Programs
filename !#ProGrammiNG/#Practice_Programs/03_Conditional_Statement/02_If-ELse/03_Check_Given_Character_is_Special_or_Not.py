# Wap to check whether the given character is special or not.

ch = input('Enter Any Character:')

if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9'):
    print('Given Character is Special Character')

else:
    print('Given Character is Not a Special Character')
