# Wap to print Ascii value of a character only if it is upper case.

ch = input('Enter Any Character:')

ch_val = ord(ch)

if ch_val >= 65 and ch_val <= 90:
    print(f'Ascii Value of {ch} is {ch_val}')
