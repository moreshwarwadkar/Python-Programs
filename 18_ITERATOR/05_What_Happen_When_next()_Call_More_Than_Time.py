# Create an iterator from a list and show what happens when next() is called more times than the number of elements.

li = [1,2,3,4,5]

a = iter(li)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

'''
OUTPUT : 

1
2
3
4
5
Traceback (most recent call last):
  File "m:\!\01_SAMPLE_unik.py", line 12, in <module>
    print(next(a))
          ^^^^^^^
StopIteration
'''
