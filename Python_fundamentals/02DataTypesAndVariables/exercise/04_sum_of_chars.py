number_of_lines = int(input())

sum_codes = 0

for line in range(number_of_lines):
    letter = input()
    sum_codes += ord(letter)

print(f'The sum equals: {sum_codes}')