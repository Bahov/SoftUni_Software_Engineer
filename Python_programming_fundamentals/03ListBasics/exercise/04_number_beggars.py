integer_string = input().split(', ')
count_beggars = int(input())

int_string_conv = list(map(int, integer_string))

sum_money = 0
start_index = 0

result_list = []

for beggar in range(count_beggars):
    for i in range(start_index, len(int_string_conv), count_beggars):
        sum_money += int_string_conv[i]
    result_list.append(sum_money)
    start_index += 1
    sum_money = 0

print(result_list)
