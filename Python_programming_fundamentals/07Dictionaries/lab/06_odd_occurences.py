input_list = [x.lower() for x in input().split(' ')]

result_list = []

for element in input_list:
    if input_list.count(element) % 2 != 0 and element not in result_list:
        result_list.append(element)

print(' '.join(result_list))