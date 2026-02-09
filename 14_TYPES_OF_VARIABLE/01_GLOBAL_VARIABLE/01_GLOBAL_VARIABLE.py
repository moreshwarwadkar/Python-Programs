# GLOBAL_VARIABLE

'''
TO Modify the global variable inside the function we need to declare the variable with keyword called as "global" before modification.
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


