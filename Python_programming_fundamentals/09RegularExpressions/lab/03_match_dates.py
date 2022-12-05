import re

line = input()

search_pattern = r'(\d{2})([\/.-])([A-Z]{1}[a-z]{2})\2(\d{4})'

result = re.findall(search_pattern, line)

for match in result:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')