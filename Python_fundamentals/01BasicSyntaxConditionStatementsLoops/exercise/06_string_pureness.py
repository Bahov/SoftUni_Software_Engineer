

number_of_strings = int(input())

for string in range(number_of_strings):
    string = input()
    if string.count(',') + string.count('.') + string.count('_') > 0:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')