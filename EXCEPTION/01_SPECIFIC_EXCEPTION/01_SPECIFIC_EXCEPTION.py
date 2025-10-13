# SPECIFIC EXCEPTION

def div():

    try:

        no1 = int(input('Enter Number 1:'))
        no2 = int(input('Enter Number 2:'))

        d = no1/no2

    except ZeroDivisionError:

        print('Number Should Not Be Zero')

    except ValueError:

        print('The Value Should Be Always a Number')

    else:

        print('The Program Has No Exceptions')

    finally:

        print('The Program is Executed Successfully')

div()
