# OUTPUT_STATEMENT : print()

'''
1) Syntax:

--> print(val1, val2, val3,...)

This Function have 2 Attribute:
1) Seperator
2) End
'''

# 1) Seperator ---------------------------

a = 10
b = 20
c = 30

print(a,b,c) # OP: 10 20 30
print(a,b,c, sep='&') # OP: 10&20&30
print(a,b,c, sep='\n')
'''
OP:
10
20
30
'''

# 2) END ---------------------------

print(a, end=' ')
print(b, end=' ')
print(c, end=' ')

# OP: 10 20 30 

