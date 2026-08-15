regex_pattern = r"(?!.*(I{4}|V{2,}|X{4}|L{2,}|C{4}|D{2,}|M{4})).*$"


import re
print(str(bool(re.match(regex_pattern, input()))))
