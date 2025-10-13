#Give me practice programming question which is related to split()

import re
a = 'apple,banana;cherry,grape'
sp = re.split(r'[;,]', a)
print(sp)
