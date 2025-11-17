#Use map() to reverse each string in a list.

str = ['UNIK','BABA']

a = map(lambda s: s[::-1],str)
print(tuple(a))
