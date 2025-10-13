# Prime Numbers Generator

def prime(n):

    for i in range(2,n):

        for j in range(2,i):

            if i%j == 0:

                break
        else:

            yield i

# IT WILL PRINT DIRECTLY..

for i in prime(10):

    print(i)

# ANOTHER METHOD TO PRINT PRIME NUMBERS IN A LIST FORMATE..

print(list(prime(10)))
