# WITH CONDITION ( IF - ELSE )

gen = ('EVEN' if n%2==0 else 'ODD' for n in range(1,6))
print(list(gen))
