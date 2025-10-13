# WAP TO CALCULATE THE TIME TAKEN FOR ADDING NUMBERS.
# time Module will be used.
# time.time will give the exact time in second.

import time

def time_c(func):

    def inner(*args,**kwargs):

        st = time.time()
        func(*args,**kwargs)
        et = time.time()
        tt = et-st

        print(tt)

    return inner

@time_c
def add(a,b):

    sum = a+b
    print(sum)
    time.sleep(5)

add(10,20)
