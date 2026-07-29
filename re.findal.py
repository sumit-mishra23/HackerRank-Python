import re
matches = re.finditer(r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])", input())
found = False

for word in matches:
    print(word.group(1))
    found = True
if(not found):
    print(-1)
