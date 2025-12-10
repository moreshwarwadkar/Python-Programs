'''
Account Lock System

Create a class LoginAccount with private attributes:

username
password
failed_attempts

Rules:

After 3 wrong login attempts, account becomes locked.
Provide method to reset password (only when unlocked).
Use getters/setters where needed.
'''

class LoginAccount:

    def __init__(self):
        self.__username = '@unik'
        self.__password = 'unik@123'
        self.__failed_attempts = 0

    def login(self):
        
        while True:

            if self.__failed_attempts < 3:

                username = input('Enter Username:')
                password = input('Enter Password:')
                
                if self.__username == username and self.__password == password:
                    print('\nLogin Successfull..!!')
                    self.__failed_attempts = 0
                    return

                else:
                    print('\nPlease Try AGain..!!')
                    print('------------------------------------')
                    self.__failed_attempts += 1
                    

            else:
                print('------------------------------------')
                print('\nYour Account Has Been Locked..!!')
                self.reset()

    def reset(self):

        new_uname = input('Enter Username:')

        if self.__username == new_uname:  

            new_pass = input('Enter New Password:')
            self.__password = new_pass
            self.__failed_attempts = 0
            print("\nPassword Reset Successful! Please Login Again.\n")

        else:
            print('\nUser Does Not Exits..!!')    
        
obj = LoginAccount()

obj.login()
