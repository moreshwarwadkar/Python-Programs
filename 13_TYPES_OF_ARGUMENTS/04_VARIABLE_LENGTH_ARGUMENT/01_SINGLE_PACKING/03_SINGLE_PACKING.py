# SINGLE_PACKING

def show_names(*names):
    for n in names:
        print("Hello", n)

# taking input as multiple names
user_input = input("Enter names separated by space: ").split()
show_names(*user_input)

'''
OP :

Hello Unik
Hello Rohan
Hello Rohit
'''



# IN SIMPLIFIED FOROM

def names(*names):
    
    print(names)

uinput = input("Enter names separated by space: ").split()
names(*uinput)

# OP: ('Unik', 'Rohan', 'Rohit')
