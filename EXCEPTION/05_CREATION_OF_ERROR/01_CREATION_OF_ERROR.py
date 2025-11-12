class NumberError(Exception):

    pass

def div():

    try:

        no1 = int(input('Enter Number 1:'))
        no2 = int(input('Enter Number 2:'))

        d = no1/no2
        print(d)

    except ZeroDivisionError:

        raise NumberError('Number Should Not Be Zero')

    except ValueError:

        raise NumberError('The Value Should Be Always a Number')

div()
