string_list = input().split(', ')

integer_list = list(map(int, string_list))

count_zeros = integer_list.count(0)

for i in range(count_zeros):
    integer_list.remove(0)
    integer_list.append(0)

print(integer_list)
