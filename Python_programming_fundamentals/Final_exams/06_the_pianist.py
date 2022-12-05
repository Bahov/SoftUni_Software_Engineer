start_number = int(input())

dictionary = {}

for _ in range(start_number):
    line = input().split('|')
    piece = line[0]
    composer = line[1]
    key = line[2]
    dictionary.update({piece:{composer:key}})

command = input()
while command != 'Stop':
    command_list = command.split('|')
    action = command_list[0]
    piece = command_list[1]
    if action == 'Add':
        composer = command_list[2]
        key = command_list[3]
        if piece in dictionary.keys():
            print(f'{piece} is already in the collection!')
        else:
            dictionary.update({piece:{composer:key}})
            print(f'{piece} by {composer} in {key} added to the collection!')
    elif action == 'Remove':
        if piece in dictionary.keys():
            del dictionary[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif action == 'ChangeKey':
        new_key = command_list[2]
        if piece in dictionary.keys():
            for composer, key in dictionary[piece].items():
                dictionary[piece][composer] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    command = input()

for piece, info in dictionary.items():
    print(f'{piece} -> ' , end='')
    for composer, key in info.items():
        print(f'Composer: {composer}, Key: {key}')
