# Wap to login into the Instagram with valid username and password.(enter password only if the user name is valid)

username = 'unik'
password = 123

uname = input('Enter Username:')

if username == uname:
    
    pwd = int(input('Enter Password:'))
    if password == pwd:
        print(f'Hey..! {username} Login Successfull..')
    
    else:
        print('Invalid Password..!')

else:
    print('Invalid Username..!')
