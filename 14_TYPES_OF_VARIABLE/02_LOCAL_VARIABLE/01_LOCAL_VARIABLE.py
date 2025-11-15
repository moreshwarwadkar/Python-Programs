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
