# wap to print the last value of a list only if it is palindrome string starting with vowel.

s = ['hello','apple','madam']

last_val = s[-1]
rev = last_val[::-1]

if last_val == rev:
    
    if last_val[0] in 'aeiouAEIOU':
        print(last_val)
    
    else:
        print('Does Not Start With Vowel')
        
else:
    print('String is Not Palindrome')
