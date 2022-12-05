import re

line = input()

search_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

result = re.findall(search_pattern, line)

print(' '.join(result))