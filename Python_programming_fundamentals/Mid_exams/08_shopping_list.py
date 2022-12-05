shopping_list = input().split('!')

command = input()

while command != 'Go Shopping!':
    command_list = command.split(' ')
    action = command_list[0]
    item = command_list[1]
    if item not in shopping_list:
        if action == 'Urgent':
            shopping_list.insert(0,item)
    if item in shopping_list:
        if action == 'Correct':
            new_item = command_list[2]
            index_old_item = shopping_list.index(item)
            shopping_list[index_old_item] = new_item
        elif action == 'Unnecessary':
            shopping_list.remove(item)
        elif action == 'Rearrange':
            shopping_list.remove(item)
            shopping_list.append(item)
    command = input()

print(', '.join(shopping_list))