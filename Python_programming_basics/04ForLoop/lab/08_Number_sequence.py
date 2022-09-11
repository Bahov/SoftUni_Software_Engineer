count_of_numbers = int(input())

max_number = 0
min_number = 0
for number in range(1, count_of_numbers + 1, 1):
    manual_enter_number = int(input())
    if number == 1:
        max_number = manual_enter_number
        min_number = manual_enter_number
    else:
        if manual_enter_number > max_number:
            max_number = manual_enter_number
        if manual_enter_number < min_number:
            min_number = manual_enter_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
