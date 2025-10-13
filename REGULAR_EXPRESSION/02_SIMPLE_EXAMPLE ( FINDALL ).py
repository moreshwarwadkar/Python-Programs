import re

text = "My age is 25 a12"
result = re.findall(r'\{2}d+', text)
print(result)
