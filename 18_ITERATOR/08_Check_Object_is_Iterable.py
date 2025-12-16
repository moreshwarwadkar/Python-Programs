# Use iter() to check whether an object is iterable or not without using isinstance().

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


print(is_iterable([1, 2, 3]))   # True
print(is_iterable("Python"))   # True
print(is_iterable(100))        # False
print(is_iterable(10.5))       # False
