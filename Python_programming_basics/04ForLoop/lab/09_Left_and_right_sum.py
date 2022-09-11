count_of_numbers = int(input())

left_sum = 0
right_sum = 0

for number in range(count_of_numbers * 2):
    manual_enter_number = int(input())
    if number < count_of_numbers:
        left_sum = left_sum + manual_enter_number
    else:
        right_sum = right_sum + manual_enter_number

diff = 0
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
