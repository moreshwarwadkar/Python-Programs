# Wap to get the following output.
# S=’always keep smiling’
# Out-‘syawla peek gnilims’

# First Method --

s = 'always keep smiling'
sp = s.split()
new = ''
word = ''

for i in range(0,len(s)):
    
    if s[i] != ' ':
        
        word = s[i]+word

    else:
        
        new = new + word + ' '
        word = ''

new = new + word

print(new)


# But This Method is Not Recommended

'''
s = 'always keep smiling'
sp = s.split()
new = ''

for i in sp:
    
    new = new+i[::-1] + ' '
    
print(new.strip()) # strip() Will remove extra spaces at the end
'''
