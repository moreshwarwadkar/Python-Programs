import re
text = "Python is fun"
result = re.match(r'Python', text)
print(result.group())
