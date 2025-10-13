# PRINT FIRST 5 EVEN NUMBERS 


def ev(n):

    for i in range(1,n+1):

        yield 2*i

for i in ev(5):

    print(i)



def ev(n):

    for i in range(1,n+1):

        yield 2*i

a = ev(5)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

