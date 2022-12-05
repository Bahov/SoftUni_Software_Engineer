items_list = input().split(', ')

command = input()

while command != 'Craft!':
    if 'Collect' in command:
        command_list = command.split(' - ')
        item = command_list[1]
        if item not in items_list:
            items_list.append(item)
    elif 'Drop' in command:
        command_list = command.split(' - ')
        item = command_list[1]
        if item in items_list:
            items_list.remove(item)
    elif 'Combine' in command:
        command = command[16:]
        command_list = command.split(':')
        old_item = command_list[0]
        new_item = command_list[1]
        if old_item in items_list:
            old_item_index = items_list.index(old_item)
            items_list.insert(old_item_index + 1, new_item)
    elif 'Renew' in command:
        command_list = command.split(' - ')
        item = command_list[1]
        if item in items_list:
            items_list.pop(items_list.index(item))
            items_list.append(item)
    command = input()

print(', '.join(items_list))
    
