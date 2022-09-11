count_of_numbers = int(input())

even_sum = 0
odd_sum = 0
for number in range(1, count_of_numbers + 1):
    manual_enter_number = int(input())
    if number % 2 == 0:
        even_sum += manual_enter_number
    else:
        odd_sum += manual_enter_number

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    difference = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {difference}")
