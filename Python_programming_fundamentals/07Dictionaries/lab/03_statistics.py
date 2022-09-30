
inventory = {}

while True:
    command = input()

    if command == 'statistics':
        print('Products in stock:')
        for key,value in inventory.items():
            print(f'- {key}: {value}')
        print(f'Total Products: {len(inventory)}')
        print(f'Total Quantity: {sum(inventory.values())}')
        break

    command_list = command.split(': ')

    if command_list[0] in inventory.keys():
        inventory[command_list[0]] += int(command_list[1])
    else:
        inventory[command_list[0]] = int(command_list[1])
