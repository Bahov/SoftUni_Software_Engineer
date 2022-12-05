line = input()

result = ''

for index in range(len(line)):
    if index == 0:
        result += line[index]
    elif line[index] != line[index-1]:
        result += line[index]
print(result)