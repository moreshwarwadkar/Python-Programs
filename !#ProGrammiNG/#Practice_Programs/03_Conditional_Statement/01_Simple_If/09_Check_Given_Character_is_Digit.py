#  Wap to check whether the given character is digit or not.

ch = eval(input('Enter Any Number:'))

if isinstance(ch,(int,float)):
    print('Given Character is Digit')
    
# Another Way ---

if '0' <= ch <= '9':
    print("Given Character is Digit")
