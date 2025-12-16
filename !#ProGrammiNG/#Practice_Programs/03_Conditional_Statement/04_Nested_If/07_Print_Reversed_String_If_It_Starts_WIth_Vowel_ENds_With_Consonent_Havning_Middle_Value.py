# Wap to print the reversed string only if it is starting with vowel ,ending with consonant and having a middle value.

s = input('Enter Any String:')

if s[0] in 'aeiouAEIOU' and s[-1] not in 'aeiouAEIOU' and len(s) % 2 != 0 :
    
    print(s[::-1])
