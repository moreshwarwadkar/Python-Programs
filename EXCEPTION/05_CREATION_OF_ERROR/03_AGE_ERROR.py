class AgeError(Exception):

    pass

def div():

    age = int(input('Enter Age:'))

    if age >= 18:

        print('You Are Eligible For Vote')

    else:

        raise AgeError('You Are Not Eligible For Vote')

div()
