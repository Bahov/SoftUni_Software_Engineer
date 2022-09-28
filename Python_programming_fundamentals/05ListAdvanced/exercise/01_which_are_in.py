first_list = input().split(', ')
second_list = input().split(', ')

result_list = []

for i in first_list:
    for j in second_list:
        if i in j:
            result_list.append(i)
            break

print(result_list)
