import re

text = "I have 2 apples and 5 bananas"
matches = re.finditer(r'\d+', text)

for match in matches:
    print(match.group())
