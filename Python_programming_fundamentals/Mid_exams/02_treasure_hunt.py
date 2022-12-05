treasure_chest = input().split('|')

command = input()
stolen_items = []
number_of_items = 0
sum_len = 0

while command != 'Yohoho!':
    command_list = command.split(' ')
    if command_list[0] == 'Loot':
        command_list.remove('Loot')
        for item in command_list:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
    elif command_list[0] == 'Drop':
        if 0 < int(command_list[1]) < len(treasure_chest):
            treasure_chest.append(treasure_chest[int(command_list[1])])
            treasure_chest.pop(int(command_list[1]))
    elif command_list[0] == 'Steal':
        treasure_chest.reverse()
        if len(treasure_chest) < int(command_list[1]):
            number_of_items = len(treasure_chest)
        else:
            number_of_items = int(command_list[1])
        for _ in range(number_of_items):
            stolen_items.append(treasure_chest.pop(0))
        stolen_items.reverse()
        print(', '.join(stolen_items))
        stolen_items.clear()
        treasure_chest.reverse()
    command = input()

if len(treasure_chest) == 0:
    print('Failed treasure hunt.')
else:
    for item in treasure_chest:
        sum_len += len(item)
    print(f'Average treasure gain: {sum_len/len(treasure_chest):.2f} pirate credits.')
