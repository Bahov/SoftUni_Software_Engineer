import re

line = input()

search_pattern = r'(^|(?<=\s))-?(\d+)(\.?)(\d+)?($|(?=\s))'

result = re.finditer(search_pattern, line)

for match in result:
    print(match.group(), end=' ')