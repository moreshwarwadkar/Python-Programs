# TYPECASTING

a = 10

b = float(a)
print(b)  # OP : 10.0
print(type(b)) # OP : <class 'float'>

c = complex(a)
print(c) # OP : (10+0j)
print(type(c)) #OP : <class 'complex'>

d = complex(a,15)
print(d) # OP : (10+15j)

e = bool(a)
print(e) # OP : True

s = str(a)
print(s) # OP : 10
print(type(s)) # OP : <class 'str'>


'''

list(a)
tuple(a)
set(a)
dict(a)

TypeError: Object is not iterable

'''
