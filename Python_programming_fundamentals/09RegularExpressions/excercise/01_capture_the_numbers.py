import re

search_pattern = r'\d+'
line = input()

while line:
    result = re.findall(search_pattern, line)
    if result: # avoid empty list (result)
        print(' '.join(result), end = ' ')
    line = input()