distance_list = list(map(int, input().split(' ')))

command = int(input())

sum_removed_elements = 0

while True:

    if command < 0:
        removed_element = distance_list[0]
        distance_list[0] = distance_list[-1]
    elif command >= len(distance_list):
        removed_element = distance_list[-1]
        distance_list[-1] = distance_list[0]
    else:
        removed_element = distance_list.pop(command)
    
    sum_removed_elements += removed_element

    for index in range(len(distance_list)):
        if distance_list[index] <= removed_element:
            distance_list[index] += removed_element
        else:
            distance_list[index] -= removed_element
    
    if len(distance_list) == 0:
        break

    command = int(input())

print(sum_removed_elements)