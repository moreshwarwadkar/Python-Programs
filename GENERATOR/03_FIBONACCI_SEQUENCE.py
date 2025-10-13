#Create A Generator That Yields The First N Fibonacci Numbers.

def fib(n):

    f1,f2 = 0,1

    for i in range(n):

        yield f1

        f1, f2 = f2,f1+f2    

for i in fib(8):

    print(i)
