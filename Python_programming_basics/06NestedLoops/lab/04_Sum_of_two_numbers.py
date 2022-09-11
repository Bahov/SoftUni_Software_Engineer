
start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combination_exists = False
count_combinations = 0
n1 = 0
n2 = 0
for first_num in range(start_interval, end_interval + 1):
    for second_num in range(start_interval, end_interval + 1):
        count_combinations += 1
        n1 = first_num
        n2 = second_num
        if first_num + second_num == magic_number:
            combination_exists = True
            break
    if combination_exists:
        break

if combination_exists:
    print(f"Combination N:{count_combinations} ({n1} + {n2} = {magic_number})")
else:
    print(f"{count_combinations} combinations - neither equals {magic_number}")
