import re

text = "My phone number is 9876543210"

# Find all digits
print(re.findall(r'\d+', text))  # ['9876543210']

# Check if string starts with "My"
if re.match(r'^My', text):
    print("Starts with 'My'")

# Replace digits with X
print(re.sub(r'\d', 'X', text))  # 'My phone number is XXXXXXXXXX'
