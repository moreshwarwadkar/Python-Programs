# Wap to run infinite loop until user enters the correct password.

username = 'unik'
correct_pwd = 123

uname = input('Enter Username:')

if username == uname:
    
    while True:
        
        pwd = int(input('Enter Password:'))
        
        if correct_pwd == pwd:
            print('Login Successfull..!!')
            break
        
        else:
            print('Invalid Password..!!')
else:
    print('Invalid Username..!!')
