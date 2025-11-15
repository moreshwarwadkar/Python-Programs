# FETCH ONLY INETEGERS FROM THE LIST.


def gen():
    
    l = [10,20,30,'Hi','Unik',40,50]

    for i in l:

        if type(i) == int:
            yield i

print(list(gen()))
#print(tuple((gen())))  Also We can Write like this. OP: (10, 20, 30, 40, 50)


# OP: [10, 20, 30, 40, 50]
