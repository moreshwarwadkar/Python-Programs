# Wap to login to phonepe by entering correct otp.

correct_otp = 123456
attempts = 3

while attempts > 0:
    
    otp = int(input('Enter OTP:'))
    
    if correct_otp == otp:
        print('Login Successfull')
        break
        
    else:
        print('Please Enter Valid OTP..!!')
        attempts-=1
        
if attempts == 0:
    print('Account Locked..!!')
