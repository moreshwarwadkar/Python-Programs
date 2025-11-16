# POLYMORPHISM: METHOD OVERLOADING

def add(a,b):

    sum = a+b
    return sum

def add(a,b,c):

    sum = a+b+c
    return sum

def add(a,b,c,d):

    sum = a+b+c+d
    return sum

#print(add(10,20))
'''
-> If We write above code then it will throw error becase.
-> Because Function replace First Function.
-> 
It is Throwing Error Because of Here we pass only two arguments.
But in last function it takes 4 argumnet. It means it will directly 

'''
print(add(10,20,30,40))  # FIRST IT WILL GO TO LAST FUNCION WE HAVE CREATE.
print(add(10,20,30))
print(add(10,20))

'''
OUTPUT:

100
'''
