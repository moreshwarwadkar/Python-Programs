import re
text = "Python easy is easy"
result = re.search(r'easy', text)
print(result.group())
