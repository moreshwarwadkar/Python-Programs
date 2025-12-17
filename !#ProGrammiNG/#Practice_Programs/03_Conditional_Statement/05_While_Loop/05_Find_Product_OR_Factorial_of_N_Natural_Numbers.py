# Wap to find the product of n natural numbers or factorial of a number

i = 1
num = int(input('Enter Number:'))
fact = 1
product = 1

while i<=num:
    
    product *= i
    fact *= i
    i+=1

print('Product:',product)
print('Factorial:',fact)
