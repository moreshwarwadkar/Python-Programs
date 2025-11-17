import re
result = re.sub(r'\d', '*', 'A1B2C3')
print(result)   # 'A*B*C*'
