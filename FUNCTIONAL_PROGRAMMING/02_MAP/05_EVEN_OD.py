# CHECK NUMBER IS EVEN OR ODD

li = [1,2,3,4,5]

a = map(lambda n : f'{n} is Even' if n%2==0 else f'{n} is Odd',li)
print(list(a))
