whole_number = int(input())

is_special = True
for number in range(1111, 9999 + 1):
    number_to_str = str(number)
    for index, digit in enumerate(number_to_str):
        if int(digit) == 0:
            is_special = False
            break
        elif whole_number % int(digit) != 0:
            is_special = False
    if is_special:
        print(str(number) + ' ', end = '')
    is_special = True
