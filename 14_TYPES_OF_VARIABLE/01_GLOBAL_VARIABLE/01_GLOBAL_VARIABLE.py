# GLOBAL_VARIABLE

'''
IF WE WANT TO MODIFY VARIABLE INSIDE FUNCTION, THEN
WE USE 'global' KEYWORD.
'''

a = 10

def sample():

    global a

    print('Inside The Function:',a)  # 10

    a = a+30
    print('Modified Inside The Function:',a)  # 40

sample()

print('Outside The Function:',a)  # 40

a = a+30
print('Modified Inside The Function:',a)  # 70


'''
Inside The Function: 10
Modified Inside The Function: 40
Outside The Function: 40
Modified Inside The Function: 70
'''
