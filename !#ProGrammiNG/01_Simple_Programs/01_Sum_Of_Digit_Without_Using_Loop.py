# This Example For 3 Digit Number ( Sum Of Digits Without Using Loop or Functions )

a = int(input('Enter Any Number:')) 
b = a%10 
c = (a//10)%10
d = (a//100)%10

print('Sum:',b+c+d)


# This Example For 4 Digit Number ( Sum Of Digits Without Using Loop or Functions )

a = int(input('Enter Any Number:')) # 1234
b = a%10 # b = 1234%10                    : 4
c = (a//10)%10 # b = (1234//10):123 % 10  : 3 
d = (a//100)%10 # b = (1234//100):12 % 10 : 2
e = (a//1000)%10 # b = (1234//1000):1%10  : 1

print('Sum:',b+c+d+e) # 10

