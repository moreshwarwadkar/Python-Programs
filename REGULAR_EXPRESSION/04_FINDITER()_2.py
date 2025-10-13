import re

text = "GFG, O, B, GFG, O"
pattern = "GFG"

matches = re.finditer(pattern, text)

for match in matches:
    print('Match:',match.group(),'Start:',match.start(),'End:',match.end(), match.span())
