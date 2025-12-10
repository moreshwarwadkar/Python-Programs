# Simple If:

# Scenario : A door opens only if the entered password is 9999.
# Output : 'Door Open'

password = int(input('Enter Password:'))
if password == 9999:
    print('Door Open..!')




# ====================================================
# SCENARIO : IF AT TRAFFIC SIGNAL, THE COLOR IS 'RED', PRINT: STOP IMMEDIATELY..!

signal_color = input('Enter Color:')
if signal_color == 'red':
    print('Stop Immediately..!')





# ====================================================
# Scenario : If Room temperature is Below 18, print 'Too Cold'

temperature = float(input('Enter Temperature:'))
if temperature < 18:
    print('Too Cold..!')




# ====================================================
# Scenario : If a Student Scored less than 10% of full marks then teacher prints 'Meet Me Now..'

total_marks = int(input('Enter Total Marks:'))
student_marks = int(input('Enter Student Marks:'))
per = (student_marks/total_marks)*100

if per < 10:
    print('Meet Me Now..!')




# ====================================================
# Scenario : If the sum of the 4 digit number is greater than 20 then security gate shows suspicious.

num = 5556

a = num%10
b = (num//10)%10
c = (num//100)%10
d = (num//1000)%10

sum = a+b+c+d

if sum > 20:
    print('Suspicious')




# ====================================================
# Scenario : Three Digit Number Extract Digits, Print which conditions are true:

# Middle Digit > First_Digit
# Middle Digit > Last_Digit
# Middle Digit > (First + Last)

# Use only simple if statement.

num = 184

last_d = num%10
middle_d = (num//10)%10
first_d = (num//100)%10

if middle_d > first_d:
    print('Middle Digit is Greater Than First Digit')

if middle_d > last_d:
    print('Middle Digit is Greater Than Last Digit')

if middle_d > (first_d+last_d):
    print('Middle Digit is Greater Than Sum of First and Last Digit')




# ====================================================
# Scenario : Check if sum of alternate digits of a 5 Digit number is Dominating.
# For a 5 Digit number:
# Compare (d1+d3+d5) and (d2+d4)
# Print which is larger using Simple if.

num = 12345

d5 = num%10
d4 = (num//10)%10
d3 = (num//100)%10
d2 = (num//1000)%10
d1 = (num//10000)%10

if (d1+d3+d5) > (d2+d4):
    print('Hello')

if (d1+d3+d5) < (d2+d4):
    print('Good Morning')

if (d1+d3+d5) == (d2+d4):
    print('Both Are Equal')

# Check if Digit Square sum is greater than square of digit sum.
# for a 4 digit number, comput

