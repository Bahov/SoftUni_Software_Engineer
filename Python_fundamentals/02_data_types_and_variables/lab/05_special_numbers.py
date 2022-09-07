upper_limit = int(input())

str_number = ''
sum_digits = 0
for number in range(1, upper_limit + 1):

    str_number = str(number)

    for digit in range(0, len(str_number)):
        sum_digits += int(str_number[digit])

    if sum_digits in [5,7,11]:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')

    sum_digits = 0
