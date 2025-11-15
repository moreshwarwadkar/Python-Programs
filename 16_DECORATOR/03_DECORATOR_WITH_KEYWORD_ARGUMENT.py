# DECORATOR WITH KEYWORD ARGUMENT:

def my_decorator(func):
    def wrapper(**kwargs):  # KEYWORD ARGUMENT

        print('Before Function')
        return func(**kwargs)
    return wrapper

@my_decorator
def info(name, age, city):
    return f'{name},{age},{city}'

print(info(name = 'Unik', age = 22, city = 'Pune'))

'''
OUTPUT:

Before Function
Unik,22,Pune

'''
