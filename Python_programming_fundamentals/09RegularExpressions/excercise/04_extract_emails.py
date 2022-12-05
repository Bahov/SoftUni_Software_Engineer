import re

line = input()

pattern = r'(?<=\s)(([a-zA-Z0-9]+[\-\.\_a-zA-Z0-9]*)@[a-zA-Z\-]+(\.[a-z]+)+)\b'

result = re.findall(pattern, line)

for item in result:
    print(item[0])