# LOCAL_VARIABLE

def sample():

    a = 20
    print('Inside The Function:',a)  # 20

    a = a+20
    print('Modified Inside The Function:',a)  # 40

    def sum():

        nonlocal a
        print('Inside The Nested Function:',a)  # 40

        a = a+20
        print('Modified Inside The Function:',a)  # 60
    sum()
sample()


'''
- To Modify the local vraiable inside the nested function we have to declare the variable with keyword called as "nonlocal".
'''
