initial_list = input().split(' ')
number_of_shuffles = int(input())

deck_middle = len(initial_list) // 2

for i in range(number_of_shuffles):
    shuffled_list = [] # if .clear() is used initial_list will also be cleared
    first_half = initial_list[:deck_middle]
    second_half = initial_list[deck_middle:]
    for k in range(deck_middle):
        shuffled_list.append(first_half[k])
        shuffled_list.append(second_half[k])
    initial_list = shuffled_list

print(shuffled_list)