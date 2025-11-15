def div():

    try:

        no1 = int(input('Enter Number 1:'))
        no2 = int(input('Enter Number 2:'))

        d = no1/no2

    except Exception:

        print('Value Should Be Valid')

    else:

        print('The Program Has No Exception')

    finally:

        print('Program is Executed Successfully')

div()
