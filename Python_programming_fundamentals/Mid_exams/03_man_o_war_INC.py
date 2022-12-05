
pirateship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
health_cap = int(input())

def man_o_war(pirateship:list, warship:list, health_cap:int):

    command = input()

    while command != 'Retire':
        command_list = command.split(' ')
        if command_list[0] == 'Fire':
            index = int(command_list[1])
            damage = int(command_list[2])
            if 0 <= index < len(warship):
                if damage >= warship[index]:
                    return print('You won! The enemy ship has sunken.')
                else:
                    warship[index] -= damage
        elif command_list[0] == 'Defend':
            start_index = int(command_list[1])
            end_index = int(command_list[2])
            damage = int(command_list[3])
            if 0 <= end_index < len(pirateship) and 0 <= start_index <= end_index:
                for i in range(start_index, end_index + 1):
                    if pirateship[i] <= damage:
                        return print('You lost! The pirate ship has sunken.')
                    else:
                        pirateship[i] -= damage
        elif command_list[0] == 'Repair':
            index = int(command_list[1])
            health_add = int(command_list[2])
            if 0 <= index <= len(pirateship):
                if pirateship[index] + health_add < health_cap:
                    pirateship[index] += health_add
                else:
                    pirateship[index] = health_cap
        elif command_list[0] == 'Status':
            repair_section = list(filter(lambda x: x < 0.2 * health_cap, pirateship))
            print(f'{len(repair_section)} sections need repair.')
        command = input()

    if command == 'Retire':
        print(f'Pirate ship status: {sum(pirateship)}')
        print(f'Warship status: {sum(warship)}')

man_o_war(pirateship, warship, health_cap)