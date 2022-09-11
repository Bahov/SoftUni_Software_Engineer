import sys

count_of_numbers = int(input())

max_num = - sys.maxsize
sum_all = 0
for number in range(count_of_numbers):
    manual_enter_number = int(input())
    sum_all += manual_enter_number
    if manual_enter_number > max_num:
        max_num = manual_enter_number
    else:
        pass

if sum_all - max_num == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    difference = abs(max_num - (sum_all - max_num))
    print("No")
    print(f"Diff = {difference}")
