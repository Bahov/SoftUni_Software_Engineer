import re

line = input()

pattern = r'(\:{2}|\*{2})([A-Z]{1}[a-z]{2,})(\1)'

cool_treshold = 1

for char in line:
    if char.isdigit():
        cool_treshold *= int(char)

print(f'Cool threshold: {cool_treshold}')

matches = re.findall(pattern, line)

cool_list = []
if matches:
    for match in matches:
        emoji = match[1]
        sum_emoji = 0
        for char in emoji:
            sum_emoji += ord(char)
        if sum_emoji > cool_treshold:
            cool_list.append(match[0]+match[1]+match[2])

print(f'{len(matches)} emojis found in the text. The cool ones are:')
for item in cool_list: print(item)