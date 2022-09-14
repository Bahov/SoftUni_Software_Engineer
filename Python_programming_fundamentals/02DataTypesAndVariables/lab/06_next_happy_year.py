number = int(input())

is_happy = False
str_number = ''

# Option 1
# while not is_happy:
#     number += 1
#     str_number = str(number)
#     for digit in range(0, len(str_number)):
#         if digit == 0:
#             check_string = str_number[digit]
#         else:
#             if str_number[digit] in check_string:
#                 break
#             else:
#                 check_string += str_number[digit]
#
#         if digit == len(str_number) - 1:
#             is_happy = True

# Option 2
while not is_happy:
    number += 1
    set_year = set()

    for digit in range(len(str(number))):
        set_year.add(str(number)[digit])

    is_happy = len(str(number)) == len(set_year)

print(number)