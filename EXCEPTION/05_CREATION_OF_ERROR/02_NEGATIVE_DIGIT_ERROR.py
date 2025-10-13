class NegativeDigit(Exception):

    pass

def div():

        
    no1 = int(input('Enter Number 1:'))
    no2 = int(input('Enter Number 2:'))

    if no1 > 0 and no2 > 0:

        add = no1+no2
        print('Addition Of Positive Number is:',add)

    else:
        
        raise NegativeDigit('Enter Positive Numbers Only')

div()
