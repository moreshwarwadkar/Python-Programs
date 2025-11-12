'''
💥 5️⃣ Email Validation

Ask the user to input an email.
Raise a custom exception InvalidEmailError if the email doesn’t contain '@' or '.'.
Handle it and show "Invalid Email Format".
'''

class InvalidEmailError(Exception):

    pass


email = input('Enter Your Email:')

if '@' in email and '.' in email:

    print('Your Email:',email)

else:

    raise InvalidEmailError('Invalid Email Format')
