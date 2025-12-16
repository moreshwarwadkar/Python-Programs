# Consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercase, if it is digit print the reminder when it is divided by 3 else if it is special character print it’s ASCII value.

ch = input('Enter Character:')

if 'A' <= ch <= 'Z':    
    ch = chr(ord(ch)+32)
    print(ch)

elif 'a' <= ch <= 'z':
    ch = chr(ord(ch)-32)
    print(ch)

elif '0' <= ch <= '9':
    print(int(ch)%3)    

else:
    print('Ascii Value of Special Character:',ord(ch))
