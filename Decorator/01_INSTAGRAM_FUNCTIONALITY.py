# DECORATOR PROGRAM - INSTAGRAM LOGIN, LOGOUT AND OTHER FUNCTIONALITY

def insta(func):

    def inner(*args, **kwargs):

        print('WWW.instagram.com')
        print('Login Successfull')
        func(*args,**kwargs)
        print('Logout Done')

    return inner

@insta
def post_reel():
    print('Reel Has been Posted')

@insta
def chat():
    print('You Are Chatting')

@insta
def call():
    print('You Are Calling')

print('----- **- 1 -** -----')
post_reel()
print('----- **- 2 -** -----')
chat()
print('----- **- 3 -** -----')
call()
print('----- ***** -----')
