line = input()

strength = 0
result = ''

for index in range(len(line)):
    if line[index] == '>':
        strength += int(line[index+1])
        result += '>'
    elif strength > 0:
        strength -= 1
    else:
        result += line[index]
print(result)