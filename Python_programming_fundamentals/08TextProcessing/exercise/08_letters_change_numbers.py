line = input().split()

result = 0

for item in line:
    if item != '':
        number = int(item[1:-1])
        if item[0].isupper():
            number /= (ord(item[0])-64)
        elif item[0].islower():
            number *= (ord(item[0])-96)
        if item[-1].isupper():
            number -= (ord(item[-1])-64)
        if item[-1].islower():
            number += (ord(item[-1])-96)
        result += number

print(f'{result:.2f}')