# DECORATOR WITH BOTH *ARGS AND **KWARGS

def my_decorator(func):
    def wrapper():

        print('Before Function')
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def details(name, age, city, coutry='India'):
    return f'{name},{age},{city},{country}'

print(details('Unik',22,'Pune',country='Bharat'))
