import re

count_of_strings = int(input())

validation_pattern = r'(\!{1})([A-Z]{1}[a-z]{2,})(\1)(\:{1})(\[{1})([A-Za-z]{8,})(\]{1})'

for _ in range(count_of_strings):
    line = input()
    results = re.findall(validation_pattern, line)
    if len(results) == 0:
        print('The message is invalid')
    else:
        command = results[0][1]
        to_translate = results[0][5]
        ascii_numbers = []
        for char in to_translate:
            ascii_numbers.append(ord(char))
        print(f"{command}: {' '.join(str(num) for num in ascii_numbers)}")