'''

2️⃣ List Index Handling
Create a list of 5 elements.
Ask the user to enter an index number and print that element.

Handle:

IndexError if the user enters an invalid index.

ValueError if the input is not a number.

'''

def ind_error():

    li = [1,2,3,4,5]

    try:

        no = int(input('Enter Index:'))
        print(li[no])

    except IndexError:

        print('Index Not Found')

    except ValueError:

        print('The Value Should Be Always a Number')

ind_error()
